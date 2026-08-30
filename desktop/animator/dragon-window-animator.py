#!/usr/bin/env python3
"""
Ultra-Optimized Dragon Window Open & Close Animator (0% CPU Idle)
Uses X11 event-driven spy stream for instantaneous zero-latency window detection
with zero polling overhead, ensuring silky smooth performance on Kali Linux.
"""

import sys
import os
import time
import math
import random
import signal
import subprocess
import re
import threading

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, pyqtSignal, QObject
from PyQt6.QtGui import QPainter, QPixmap, QColor, QPen, QRadialGradient, QBrush

TARGET_WIDTH = 960
TARGET_HEIGHT = 620

DRAGON_PATH = os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")

IGNORED_CLASSES = {
    "xfce4-panel",
    "xfdesktop",
    "xfce4-notifyd",
    "xfce4-screensaver",
    "wrapper-2.0",
    "whisker",
    "whiskermenu",
    "conky",
    "polybar",
    "tint2",
    "plank",
    "dock",
    "slop",
    "screenkey",
    "gcr-prompter",
    "polkit-gnome-authentication-agent-1",
    "dragon-window-animator"
}

IGNORED_TYPES = {
    "_NET_WM_WINDOW_TYPE_DOCK",
    "_NET_WM_WINDOW_TYPE_DESKTOP",
    "_NET_WM_WINDOW_TYPE_NOTIFICATION",
    "_NET_WM_WINDOW_TYPE_TOOLTIP",
    "_NET_WM_WINDOW_TYPE_POPUP_MENU",
    "_NET_WM_WINDOW_TYPE_DROPDOWN_MENU",
    "_NET_WM_WINDOW_TYPE_COMBO",
    "_NET_WM_WINDOW_TYPE_DND",
    "_NET_WM_WINDOW_TYPE_SPLASH"
}


def get_client_list():
    try:
        out = subprocess.check_output(["xprop", "-root", "_NET_CLIENT_LIST"], stderr=subprocess.DEVNULL).decode()
        match = re.search(r"# (.*)", out)
        if match:
            return [int(x.strip(), 16) for x in match.group(1).split(",") if x.strip()]
    except Exception:
        pass
    return []

def get_screen_size():
    try:
        out = subprocess.check_output(["xdotool", "getdisplaygeometry"], stderr=subprocess.DEVNULL).decode().split()
        return int(out[0]), int(out[1])
    except Exception:
        return 1280, 800

def get_window_properties(wid):
    try:
        out = subprocess.check_output(
            ["xprop", "-id", str(wid), "WM_CLASS", "_NET_WM_WINDOW_TYPE", "WM_TRANSIENT_FOR"],
            stderr=subprocess.DEVNULL
        ).decode()
        
        wm_class = ""
        wm_type = ""
        is_transient = "WM_TRANSIENT_FOR" in out and "not found" not in out
        
        class_match = re.search(r'WM_CLASS\(STRING\) = "(.*?)", "(.*?)"', out)
        if class_match:
            wm_class = class_match.group(1).lower() + " " + class_match.group(2).lower()
            
        type_match = re.search(r'_NET_WM_WINDOW_TYPE\(ATOM\) = (.*)', out)
        if type_match:
            wm_type = type_match.group(1).strip()
            
        return {
            "class": wm_class,
            "type": wm_type,
            "is_transient": is_transient
        }
    except Exception:
        return None

def is_app_window(wid):
    props = get_window_properties(wid)
    if not props:
        return False
    for ig in IGNORED_CLASSES:
        if ig in props["class"]:
            return False
    if props["type"] in IGNORED_TYPES:
        return False
    if props["is_transient"] and "_NET_WM_WINDOW_TYPE_NORMAL" not in props["type"]:
        return False
    return True

def get_window_geometry(wid):
    try:
        out = subprocess.check_output(["xdotool", "getwindowgeometry", str(wid)], stderr=subprocess.DEVNULL).decode()
        lines = out.strip().split("\n")
        pos_line = [l for l in lines if "Position:" in l][0]
        geom_line = [l for l in lines if "Geometry:" in l][0]
        
        pos_parts = pos_line.split("Position:")[1].split("(")[0].strip().split(",")
        geom_parts = geom_line.split("Geometry:")[1].strip().split("x")
        
        return int(pos_parts[0]), int(pos_parts[1]), int(geom_parts[0]), int(geom_parts[1])
    except Exception:
        return None

def set_window_opacity(wid, opacity_float):
    try:
        if opacity_float >= 1.0:
            subprocess.run(["xprop", "-id", str(wid), "-remove", "_NET_WM_WINDOW_OPACITY"], stderr=subprocess.DEVNULL)
        else:
            val = int(opacity_float * 0xffffffff)
            hex_val = f"0x{val:08x}"
            subprocess.run(
                ["xprop", "-id", str(wid), "-f", "_NET_WM_WINDOW_OPACITY", "32c", "-set", "_NET_WM_WINDOW_OPACITY", hex_val],
                stderr=subprocess.DEVNULL
            )
    except Exception:
        pass

def enforce_window_geometry(wid, target_w, target_h, pos_x, pos_y):
    if not is_app_window(wid):
        return

    try:
        hints = subprocess.check_output(["xprop", "-id", str(wid), "WM_NORMAL_HINTS"], stderr=subprocess.DEVNULL).decode()
        if "maximum size" in hints or "max_width" in hints:
            subprocess.run(["xprop", "-id", str(wid), "-remove", "WM_NORMAL_HINTS"], stderr=subprocess.DEVNULL)
    except Exception:
        pass

    try:
        subprocess.run(["xdotool", "windowstate", "--remove", "MAXIMIZED_VERT", str(wid)], stderr=subprocess.DEVNULL)
        subprocess.run(["xdotool", "windowstate", "--remove", "MAXIMIZED_HORZ", str(wid)], stderr=subprocess.DEVNULL)
        subprocess.run(["xdotool", "windowsize", str(wid), str(target_w), str(target_h)], stderr=subprocess.DEVNULL)
        subprocess.run(["xdotool", "windowmove", str(wid), str(pos_x), str(pos_y)], stderr=subprocess.DEVNULL)
    except Exception:
        pass

class DragonOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowTransparentForInput
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self.dragon_pixmap = QPixmap(DRAGON_PATH)
        self.anim_progress = 0.0
        self.is_animating = False
        self.anim_mode = "OPEN"

        self.target_wid = None
        self.tx = 160
        self.ty = 90
        self.tw = TARGET_WIDTH
        self.th = TARGET_HEIGHT

        self.trail = []
        self.particles = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)

    def start_open_animation(self, wid, x, y, w, h):
        self.anim_mode = "OPEN"
        self.target_wid = wid
        self.tx = x
        self.ty = y
        self.tw = w
        self.th = h
        self.anim_progress = 0.0
        self.is_animating = True
        self.trail = []
        self.particles = []

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        self.show()
        self.timer.start(16)
        self.update()

    def start_close_animation(self, x, y, w, h):
        self.anim_mode = "CLOSE"
        self.target_wid = None
        self.tx = x
        self.ty = y
        self.tw = w
        self.th = h
        self.anim_progress = 0.0
        self.is_animating = True
        self.trail = []
        self.particles = []

        cx = x + w / 2.0
        cy = y + h / 2.0
        for _ in range(35):
            angle = random.uniform(0, 2 * math.pi)
            dist = random.uniform(min(w, h) * 0.3, max(w, h) * 0.55)
            self.particles.append({
                "x": cx + math.cos(angle) * dist,
                "y": cy + math.sin(angle) * dist,
                "target_x": cx,
                "target_y": cy,
                "alpha": random.uniform(0.7, 1.0),
                "size": random.uniform(2.5, 5.5),
                "speed": random.uniform(0.05, 0.09)
            })

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        self.show()
        self.timer.start(16)
        self.update()

    def update_animation(self):
        # Progress step ~0.034 (~470ms snappy pace)
        self.anim_progress += 0.034
        t = self.anim_progress

        if self.anim_mode == "OPEN":
            if self.target_wid:
                if t < 0.60:
                    pass
                elif t < 0.85:
                    fade = (t - 0.60) / 0.25
                    set_window_opacity(self.target_wid, fade)
                else:
                    set_window_opacity(self.target_wid, 1.0)

        if self.anim_progress >= 1.0:
            self.anim_progress = 1.0
            self.is_animating = False
            self.timer.stop()
            if self.target_wid:
                set_window_opacity(self.target_wid, 1.0)
                self.target_wid = None
            self.hide()

        self.update()

    def get_flight_state(self, flight_t, is_reverse=False):
        cx = self.tx + self.tw / 2.0
        cy = self.ty + self.th / 2.0

        if not is_reverse:
            rx = (self.tw / 2.0 + 80) * (1.0 - math.pow(flight_t, 1.4))
            ry = (self.th / 2.0 + 60) * (1.0 - math.pow(flight_t, 1.4))
            theta = -math.pi * 0.5 + flight_t * 2.5 * math.pi
            base_scale = 0.42 + 0.58 * flight_t
        else:
            rx = (self.tw / 2.0 + 120) * math.pow(flight_t, 1.3)
            ry = (self.th / 2.0 + 90) * math.pow(flight_t, 1.3)
            theta = flight_t * 2.5 * math.pi
            base_scale = max(0.2, 1.0 - 0.7 * flight_t)

        px = cx + rx * math.cos(theta)
        py = cy + ry * math.sin(theta)

        dt = 0.01
        t_next = min(1.0, flight_t + dt)
        if not is_reverse:
            rx_n = (self.tw / 2.0 + 80) * (1.0 - math.pow(t_next, 1.4))
            ry_n = (self.th / 2.0 + 60) * (1.0 - math.pow(t_next, 1.4))
            th_n = -math.pi * 0.5 + t_next * 2.5 * math.pi
        else:
            rx_n = (self.tw / 2.0 + 120) * math.pow(t_next, 1.3)
            ry_n = (self.th / 2.0 + 90) * math.pow(t_next, 1.3)
            th_n = t_next * 2.5 * math.pi

        px_n = cx + rx_n * math.cos(th_n)
        py_n = cy + ry_n * math.sin(th_n)

        vx = px_n - px
        vy = py_n - py
        angle_deg = math.degrees(math.atan2(vy, vx)) if (abs(vx) > 0.001 or abs(vy) > 0.001) else 0.0

        return px, py, angle_deg, base_scale

    def paintEvent(self, event):
        if not self.is_animating:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        t = self.anim_progress
        cx = self.tx + self.tw / 2.0
        cy = self.ty + self.th / 2.0

        if self.anim_mode == "OPEN":
            self.paint_open(painter, t, cx, cy)
        else:
            self.paint_close(painter, t, cx, cy)

    def paint_open(self, painter, t, cx, cy):
        if t <= 0.52:
            flight_t = t / 0.52
            px, py, angle_deg, scale = self.get_flight_state(flight_t, is_reverse=False)

            self.trail.append((px, py, t))
            if len(self.trail) > 24:
                self.trail.pop(0)

            if random.random() < 0.85:
                tail_rad = math.radians(angle_deg + 180 + random.uniform(-25, 25))
                self.particles.append({
                    "x": px + math.cos(tail_rad) * (30 * scale),
                    "y": py + math.sin(tail_rad) * (30 * scale),
                    "vx": math.cos(tail_rad) * random.uniform(1.0, 3.5),
                    "vy": math.sin(tail_rad) * random.uniform(1.0, 3.5),
                    "alpha": 1.0,
                    "size": random.uniform(2.5, 5.5)
                })

            if len(self.trail) > 2:
                for i in range(len(self.trail) - 1):
                    p1 = self.trail[i]
                    p2 = self.trail[i + 1]
                    ratio = i / float(len(self.trail))
                    trail_alpha = int(ratio * 220)
                    trail_width = max(1.5, ratio * 6.0 * scale)
                    
                    pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], trail_alpha), trail_width)
                    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                    painter.setPen(pen)
                    painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

            wobble = math.sin(flight_t * 14.0) * 0.12
            sw = self.tw * 0.75 * scale * (1.0 + wobble)
            sh = self.th * 0.75 * scale * (1.0 - wobble)

            painter.save()
            painter.translate(px, py)
            painter.rotate(angle_deg)

            glow_rad = 65 * scale
            glow_radial = QRadialGradient(QPointF(0, 0), glow_rad)
            glow_radial.setColorAt(0.0, QColor(255, 40, 80, 180))
            glow_radial.setColorAt(0.6, QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], 90))
            glow_radial.setColorAt(1.0, QColor(20, 0, 0, 0))
            painter.setBrush(QBrush(glow_radial))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(0, 0), glow_rad, glow_rad)

            painter.setOpacity(min(1.0, flight_t * 3.5))
            painter.drawPixmap(QRectF(-sw / 2.0, -sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.restore()

        painter.setPen(Qt.PenStyle.NoPen)
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["alpha"] = max(0.0, p["alpha"] - 0.045)
            if p["alpha"] > 0:
                p_alpha = int(p["alpha"] * 255)
                painter.setBrush(QColor(255, random.randint(30, 100), 30, p_alpha))
                painter.drawEllipse(QPointF(p["x"], p["y"]), p["size"], p["size"])
        self.particles = [p for p in self.particles if p["alpha"] > 0]

        if 0.50 <= t <= 0.82:
            impact_t = (t - 0.50) / 0.32
            burst_alpha = int(max(0, math.sin(impact_t * math.pi) * 210))
            burst_radius = 120 + impact_t * 320
            burst = QRadialGradient(QPointF(cx, cy), burst_radius)
            burst.setColorAt(0.0, QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], burst_alpha))
            burst.setColorAt(0.5, QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], int(burst_alpha * 0.6)))
            burst.setColorAt(1.0, QColor(20, 0, 0, 0))
            painter.setBrush(QBrush(burst))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

            if impact_t < 0.60:
                dragon_alpha = 1.0
            else:
                dragon_alpha = max(0.0, 1.0 - (impact_t - 0.60) / 0.40)

            scale_pop = 1.0 + math.sin(impact_t * math.pi) * 0.15
            dw = self.tw * 0.88 * scale_pop
            dh = self.th * 0.88 * scale_pop

            painter.setOpacity(dragon_alpha)
            painter.drawPixmap(QRectF(cx - dw / 2.0, cy - dh / 2.0, dw, dh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.setOpacity(1.0)

        if t >= 0.55:
            box_t = min(1.0, (t - 0.55) / 0.38)
            ease = 1.0 - math.pow(1.0 - box_t, 3)

            bw = self.tw * (0.65 + 0.35 * ease)
            bh = self.th * (0.65 + 0.35 * ease)
            bx = cx - bw / 2.0
            by = cy - bh / 2.0

            frame_alpha = int(min(255, ease * 255))
            glow_thickness = max(2.0, (1.0 - ease) * 10.0)

            outer_pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int(frame_alpha * 0.7)), glow_thickness + 2.0)
            painter.setPen(outer_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

            core_pen = QPen(QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], frame_alpha), 2.0)
            painter.setPen(core_pen)
            painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

            if box_t > 0.70:
                corner_alpha = int((1.0 - (t - 0.70) / 0.30) * 255) if t > 0.70 else 255
                corner_len = 22.0
                spark_pen = QPen(QColor(255, 255, 255, max(0, min(255, corner_alpha))), 2.5)
                painter.setPen(spark_pen)
                painter.drawLine(QPointF(bx, by + corner_len), QPointF(bx, by))
                painter.drawLine(QPointF(bx, by), QPointF(bx + corner_len, by))
                painter.drawLine(QPointF(bx + bw - corner_len, by), QPointF(bx + bw, by))
                painter.drawLine(QPointF(bx + bw, by), QPointF(bx + bw, by + corner_len))
                painter.drawLine(QPointF(bx, by + bh - corner_len), QPointF(bx, by + bh))
                painter.drawLine(QPointF(bx, by + bh), QPointF(bx + corner_len, by + bh))
                painter.drawLine(QPointF(bx + bw - corner_len, by + bh), QPointF(bx + bw, by + bh))
                painter.drawLine(QPointF(bx + bw, by + bh), QPointF(bx + bw, by + bh - corner_len))

    def paint_close(self, painter, t, cx, cy):
        if t <= 0.45:
            imp_t = t / 0.45
            ease_in = math.pow(imp_t, 2.2)

            bw = max(10.0, self.tw * (1.0 - ease_in))
            bh = max(10.0, self.th * (1.0 - ease_in))
            bx = cx - bw / 2.0
            by = cy - bh / 2.0

            frame_alpha = int((1.0 - imp_t * 0.5) * 255)
            glow_thickness = max(2.0, imp_t * 8.0)

            outer_pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int(frame_alpha * 0.8)), glow_thickness + 2.0)
            painter.setPen(outer_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

            core_pen = QPen(QColor(255, 255, 255, frame_alpha), 2.5)
            painter.setPen(core_pen)
            painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

            painter.setPen(Qt.PenStyle.NoPen)
            for p in self.particles:
                p["x"] += (p["target_x"] - p["x"]) * p["speed"] * 2.5
                p["y"] += (p["target_y"] - p["y"]) * p["speed"] * 2.5
                p_alpha = int(p["alpha"] * 255 * (1.0 - imp_t * 0.3))
                painter.setBrush(QColor(255, random.randint(40, 120), 40, max(0, min(255, p_alpha))))
                painter.drawEllipse(QPointF(p["x"], p["y"]), p["size"], p["size"])

        if 0.35 <= t <= 0.70:
            summon_t = (t - 0.35) / 0.35
            burst_alpha = int(max(0, math.sin(summon_t * math.pi) * 230))
            burst_radius = 60 + summon_t * 260
            burst = QRadialGradient(QPointF(cx, cy), burst_radius)
            burst.setColorAt(0.0, QColor(255, 40, 80, burst_alpha))
            burst.setColorAt(0.5, QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], int(burst_alpha * 0.7)))
            burst.setColorAt(1.0, QColor(20, 0, 0, 0))
            painter.setBrush(QBrush(burst))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

            dragon_scale = min(1.0, summon_t * 1.8) * (min(self.tw, self.th) / 620.0)
            dw = TARGET_WIDTH * 0.85 * dragon_scale
            dh = TARGET_HEIGHT * 0.85 * dragon_scale

            painter.setOpacity(min(1.0, summon_t * 2.0))
            painter.drawPixmap(QRectF(cx - dw / 2.0, cy - dh / 2.0, dw, dh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.setOpacity(1.0)

        if t >= 0.60:
            takeoff_t = (t - 0.60) / 0.40
            px, py, angle_deg, scale = self.get_flight_state(takeoff_t, is_reverse=True)

            self.trail.append((px, py, t))
            if len(self.trail) > 24:
                self.trail.pop(0)

            if len(self.trail) > 2:
                for i in range(len(self.trail) - 1):
                    p1 = self.trail[i]
                    p2 = self.trail[i + 1]
                    ratio = i / float(len(self.trail))
                    trail_alpha = int(ratio * (1.0 - takeoff_t) * 220)
                    trail_width = max(1.5, ratio * 6.0 * scale)
                    
                    pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], max(0, min(255, trail_alpha))), trail_width)
                    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                    painter.setPen(pen)
                    painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

            wobble = math.sin(takeoff_t * 16.0) * 0.15
            sw = self.tw * 0.75 * scale * (1.0 + wobble)
            sh = self.th * 0.75 * scale * (1.0 - wobble)

            painter.save()
            painter.translate(px, py)
            painter.rotate(angle_deg)

            glow_rad = 75 * scale
            glow_radial = QRadialGradient(QPointF(0, 0), glow_rad)
            glow_radial.setColorAt(0.0, QColor(255, 40, 80, int((1.0 - takeoff_t) * 200)))
            glow_radial.setColorAt(1.0, QColor(20, 0, 0, 0))
            painter.setBrush(QBrush(glow_radial))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(0, 0), glow_rad, glow_rad)

            painter.setOpacity(max(0.0, 1.0 - takeoff_t * 1.1))
            painter.drawPixmap(QRectF(-sw / 2.0, -sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.restore()

class ClientEventBridge(QObject):
    clients_changed = pyqtSignal(list)

class EventDrivenWindowManager:
    def __init__(self, overlay):
        self.overlay = overlay
        self.bridge = ClientEventBridge()
        self.bridge.clients_changed.connect(self.on_clients_changed)

        self.known_windows = {} # wid -> (x, y, w, h)
        
        # Initial populate
        clients = get_client_list()
        for wid in clients:
            if is_app_window(wid):
                geo = get_window_geometry(wid)
                if geo and geo[2] > 150 and geo[3] > 120:
                    self.known_windows[wid] = (geo[0], geo[1], geo[2], geo[3])

        # Start event-driven background spy thread (0.0% CPU idle)
        self.spy_thread = threading.Thread(target=self._spy_worker, daemon=True)
        self.spy_thread.start()

    def _spy_worker(self):
        try:
            proc = subprocess.Popen(
                ["xprop", "-root", "-spy", "_NET_CLIENT_LIST"],
                stdout=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            for line in proc.stdout:
                if "_NET_CLIENT_LIST" in line:
                    match = re.search(r"# (.*)", line)
                    if match:
                        client_list = [int(x.strip(), 16) for x in match.group(1).split(",") if x.strip()]
                        self.bridge.clients_changed.emit(client_list)
        except Exception:
            pass

    def on_clients_changed(self, current_clients):
        current_set = set(current_clients)
        known_set = set(self.known_windows.keys())

        # 1. New Windows
        new_windows = current_set - known_set
        for wid in new_windows:
            if not is_app_window(wid):
                continue

            geo = get_window_geometry(wid)
            if not geo or geo[2] < 150 or geo[3] < 120:
                continue

            sw, sh = get_screen_size()
            pos_x = max(0, (sw - TARGET_WIDTH) // 2)
            pos_y = max(30, (sh - TARGET_HEIGHT) // 2)

            self.known_windows[wid] = (pos_x, pos_y, TARGET_WIDTH, TARGET_HEIGHT)

            # Instantly hide and set 960x620
            set_window_opacity(wid, 0.0)
            enforce_window_geometry(wid, TARGET_WIDTH, TARGET_HEIGHT, pos_x, pos_y)

            # Launch OPEN animation
            self.overlay.start_open_animation(wid, pos_x, pos_y, TARGET_WIDTH, TARGET_HEIGHT)

            # Background one-shot verification after 200ms and 500ms
            def verify_later(w_id, px, py):
                time.sleep(0.20)
                enforce_window_geometry(w_id, TARGET_WIDTH, TARGET_HEIGHT, px, py)
                time.sleep(0.30)
                enforce_window_geometry(w_id, TARGET_WIDTH, TARGET_HEIGHT, px, py)

            threading.Thread(target=verify_later, args=(wid, pos_x, pos_y), daemon=True).start()

        # 2. Closed Windows
        closed_windows = known_set - current_set
        for wid in closed_windows:
            last_geo = self.known_windows.pop(wid, None)
            if last_geo:
                lx, ly, lw, lh = last_geo
                if lw > 150 and lh > 120:
                    self.overlay.start_close_animation(lx, ly, lw, lh)

        # 3. Update tracked geometries
        for wid in current_set.intersection(set(self.known_windows.keys())):
            if is_app_window(wid):
                geo = get_window_geometry(wid)
                if geo and geo[2] > 150 and geo[3] > 120:
                    self.known_windows[wid] = (geo[0], geo[1], geo[2], geo[3])

def main():
    pid_file = "/tmp/dragon-animator.pid"
    if os.path.exists(pid_file):
        try:
            with open(pid_file, "r") as f:
                old_pid = int(f.read().strip())
            os.kill(old_pid, signal.SIGTERM)
            time.sleep(0.2)
        except Exception:
            pass
    with open(pid_file, "w") as f:
        f.write(str(os.getpid()))

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    overlay = DragonOverlay()
    manager = EventDrivenWindowManager(overlay)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
