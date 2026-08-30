#!/usr/bin/env python3
"""
🐉 Dragon Window Spawn & Close Cinematic Animator (Multi-Color Edition)
Event-Driven X11 Window Tracker with Plasma Ribbon & Border Morphing
"""

import sys, os, time, math, random, threading, subprocess, re, signal
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, QObject, pyqtSignal
from PyQt6.QtGui import QPainter, QPixmap, QColor, QPen, QBrush, QRadialGradient

TARGET_WIDTH = 960
TARGET_HEIGHT = 620

def get_color_config():
    config_path = os.path.expanduser("~/.local/share/dragon-anim/color_config.json")
    if os.path.exists(config_path):
        try:
            import json
            with open(config_path, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "color_name": "red",
        "glow": [255, 23, 68],
        "core": [236, 1, 1],
        "dark": [180, 10, 25],
        "highlight": [255, 120, 140]
    }

COLOR_CFG = get_color_config()
GLOW_RGB = tuple(COLOR_CFG.get("glow", [255, 23, 68]))
CORE_RGB = tuple(COLOR_CFG.get("core", [236, 1, 1]))
DARK_RGB = tuple(COLOR_CFG.get("dark", [180, 10, 25]))
HI_RGB = tuple(COLOR_CFG.get("highlight", [255, 120, 140]))

DRAGON_PATH = os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")
if not os.path.exists(DRAGON_PATH):
    DRAGON_PATH = "/home/gr/Escritorio/Kali-Red-Dragon-Suite/assets/dragon_sprite.png"

def clean_window_opacity(wid):
    try:
        subprocess.run(["xprop", "-id", str(wid), "-remove", "_NET_WM_WINDOW_OPACITY"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=0.15)
        subprocess.run(["xprop", "-id", str(wid), "-f", "_NET_WM_WINDOW_OPACITY", "32c", "-set", "_NET_WM_WINDOW_OPACITY", "0xffffffff"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=0.15)
    except Exception:
        pass

def clean_all_window_opacities():
    try:
        out = subprocess.check_output(["xprop", "-root", "_NET_CLIENT_LIST"], stderr=subprocess.DEVNULL, timeout=0.3).decode()
        match = re.search(r"# (.*)", out)
        if match:
            wids = [int(x.strip(), 16) for x in match.group(1).split(",") if x.strip()]
            for wid in wids:
                clean_window_opacity(wid)
    except Exception:
        pass

def set_window_opacity(wid, alpha):
    if not wid:
        return
    try:
        if alpha >= 0.98:
            clean_window_opacity(wid)
            return
        opacity_val = int(max(0.0, min(1.0, alpha)) * 0xFFFFFFFF)
        subprocess.run(
            ["xprop", "-id", str(wid), "-f", "_NET_WM_WINDOW_OPACITY", "32c", "-set", "_NET_WM_WINDOW_OPACITY", hex(opacity_val)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=0.15
        )
    except Exception:
        pass

def get_client_list():
    try:
        out = subprocess.check_output(["xprop", "-root", "_NET_CLIENT_LIST"], stderr=subprocess.DEVNULL, timeout=0.3).decode()
        match = re.search(r"# (.*)", out)
        if match:
            return [int(x.strip(), 16) for x in match.group(1).split(",") if x.strip()]
    except Exception:
        pass
    return []

def get_window_geometry(wid):
    try:
        out = subprocess.check_output(["xdotool", "getwindowgeometry", "--shell", str(wid)], stderr=subprocess.DEVNULL, timeout=0.3).decode()
        x, y, w, h = 0, 0, 0, 0
        for line in out.splitlines():
            if line.startswith("X="): x = int(line.split("=")[1])
            elif line.startswith("Y="): y = int(line.split("=")[1])
            elif line.startswith("WIDTH="): w = int(line.split("=")[1])
            elif line.startswith("HEIGHT="): h = int(line.split("=")[1])
        return (x, y, w, h)
    except Exception:
        return None

def is_app_window(wid):
    try:
        wtype = subprocess.check_output(["xprop", "-id", str(wid), "_NET_WM_WINDOW_TYPE"], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        if "_NET_WM_WINDOW_TYPE_DESKTOP" in wtype or "_NET_WM_WINDOW_TYPE_DOCK" in wtype or "_NET_WM_WINDOW_TYPE_NOTIFICATION" in wtype:
            return False
        
        wclass = subprocess.check_output(["xprop", "-id", str(wid), "WM_CLASS"], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        if "xfdesktop" in wclass or "xfce4-panel" in wclass or "wrapper-" in wclass or "desktop" in wclass.lower():
            return False

        wstate = subprocess.check_output(["xprop", "-id", str(wid), "_NET_WM_STATE"], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        if "_NET_WM_STATE_STICKY" in wstate or "_NET_WM_STATE_SKIP_TASKBAR" in wstate:
            return False

        return True
    except Exception:
        return False

def get_screen_size():
    try:
        out = subprocess.check_output(["xrandr", "--current"], stderr=subprocess.DEVNULL, timeout=0.3).decode()
        match = re.search(r"current (\d+) x (\d+)", out)
        if match:
            return int(match.group(1)), int(match.group(2))
    except Exception:
        pass
    return 1920, 1080

def enforce_window_geometry(wid, target_w, target_h, pos_x, pos_y):
    if not is_app_window(wid):
        return
    try:
        hints = subprocess.check_output(["xprop", "-id", str(wid), "WM_NORMAL_HINTS"], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        if "maximum size" in hints or "max_width" in hints:
            subprocess.run(["xprop", "-id", str(wid), "-remove", "WM_NORMAL_HINTS"], stderr=subprocess.DEVNULL, timeout=0.2)
    except Exception:
        pass
    try:
        subprocess.run(["xdotool", "windowstate", "--remove", "MAXIMIZED_VERT", str(wid)], stderr=subprocess.DEVNULL, timeout=0.2)
        subprocess.run(["xdotool", "windowstate", "--remove", "MAXIMIZED_HORZ", str(wid)], stderr=subprocess.DEVNULL, timeout=0.2)
        subprocess.run(["xdotool", "windowsize", str(wid), str(target_w), str(target_h)], stderr=subprocess.DEVNULL, timeout=0.2)
        subprocess.run(["xdotool", "windowmove", str(wid), str(pos_x), str(pos_y)], stderr=subprocess.DEVNULL, timeout=0.2)
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

        self.reload_assets()

        self.anim_progress = 0.0
        self.is_animating = False
        self.anim_mode = "OPEN"

        self.active_wid = None
        self.tx = 160
        self.ty = 90
        self.tw = TARGET_WIDTH
        self.th = TARGET_HEIGHT

        self.trail = []
        self.particles = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)

    def reload_assets(self):
        global COLOR_CFG, GLOW_RGB, CORE_RGB, DARK_RGB, HI_RGB, DRAGON_PATH
        COLOR_CFG = get_color_config()
        GLOW_RGB = tuple(COLOR_CFG.get("glow", [255, 23, 68]))
        CORE_RGB = tuple(COLOR_CFG.get("core", [236, 1, 1]))
        DARK_RGB = tuple(COLOR_CFG.get("dark", [180, 10, 25]))
        HI_RGB = tuple(COLOR_CFG.get("highlight", [255, 120, 140]))

        DRAGON_PATH = os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")
        if not os.path.exists(DRAGON_PATH):
            DRAGON_PATH = "/home/gr/Escritorio/Kali-Red-Dragon-Suite/assets/dragon_sprite.png"
        self.dragon_pixmap = QPixmap(DRAGON_PATH)

    def start_open_animation(self, wid, x, y, w, h):
        self.reload_assets()
        self.anim_mode = "OPEN"
        self.active_wid = wid
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

        # Start with window hidden and guarantee full restoration at 750ms watchdog
        set_window_opacity(wid, 0.0)
        QTimer.singleShot(750, lambda: clean_window_opacity(wid))

        self.show()
        self.timer.start(16)
        self.update()

    def start_close_animation(self, x, y, w, h):
        self.reload_assets()
        self.anim_mode = "CLOSE"
        self.active_wid = None
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
                "size": random.uniform(2.5, 6.5),
                "speed": random.uniform(0.08, 0.20),
                "alpha": random.uniform(0.7, 1.0)
            })

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.show()
        self.timer.start(16)
        self.update()

    def get_flight_state(self, t, is_reverse=False):
        cx = self.tx + self.tw / 2.0
        cy = self.ty + self.th / 2.0
        radius_x = (self.tw / 2.0) + 70.0
        radius_y = (self.th / 2.0) + 50.0

        if not is_reverse:
            prog = t
            angle = -math.pi * 0.8 + prog * (math.pi * 2.2)
            cur_rx = radius_x * (1.35 - 0.45 * prog)
            cur_ry = radius_y * (1.35 - 0.45 * prog)
            tilt_offset_x = (1.0 - prog) * 260.0
            tilt_offset_y = (1.0 - prog) * -160.0
            scale = 0.45 + 0.65 * math.sin(prog * math.pi)
        else:
            prog = t
            angle = math.pi * 0.2 + prog * (math.pi * 2.5)
            cur_rx = radius_x * (0.3 + 1.2 * prog)
            cur_ry = radius_y * (0.3 + 1.2 * prog)
            tilt_offset_x = prog * 280.0
            tilt_offset_y = prog * -220.0
            scale = 1.0 - 0.70 * prog

        px = cx + math.cos(angle) * cur_rx + tilt_offset_x
        py = cy + math.sin(angle) * cur_ry + tilt_offset_y

        dt = 0.015
        if not is_reverse:
            angle_next = -math.pi * 0.8 + (prog + dt) * (math.pi * 2.2)
            p_next_x = cx + math.cos(angle_next) * cur_rx + ((1.0 - (prog + dt)) * 260.0)
            p_next_y = cy + math.sin(angle_next) * cur_ry + ((1.0 - (prog + dt)) * -160.0)
        else:
            angle_next = math.pi * 0.2 + (prog + dt) * (math.pi * 2.5)
            p_next_x = cx + math.cos(angle_next) * cur_rx + ((prog + dt) * 280.0)
            p_next_y = cy + math.sin(angle_next) * cur_ry + ((prog + dt) * -220.0)

        vx = p_next_x - px
        vy = p_next_y - py
        angle_deg = math.degrees(math.atan2(vy, vx))
        return px, py, angle_deg, scale

    def update_animation(self):
        if not self.is_animating:
            return

        self.anim_progress += 0.022

        # Smooth window fade-in from 0.50 to 0.85
        if self.anim_mode == "OPEN" and self.active_wid:
            if self.anim_progress >= 0.50:
                fade_alpha = min(1.0, (self.anim_progress - 0.50) / 0.35)
                set_window_opacity(self.active_wid, fade_alpha)

        if self.anim_progress >= 1.0:
            self.anim_progress = 1.0
            self.is_animating = False
            self.timer.stop()
            if self.active_wid:
                clean_window_opacity(self.active_wid)
            self.hide()
            self.update()
            return

        self.update()

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

        painter.end()

    def paint_open(self, painter, t, cx, cy):
        # 1. Flying Dragon Orbit (0.0 to 0.70)
        if t <= 0.70:
            flight_t = t / 0.70
            px, py, angle_deg, scale = self.get_flight_state(flight_t)

            self.trail.append((px, py, t))
            if len(self.trail) > 24:
                self.trail.pop(0)

            # Fiery plasma ribbon trail
            if len(self.trail) > 2:
                for i in range(len(self.trail) - 1):
                    p1 = self.trail[i]
                    p2 = self.trail[i + 1]
                    ratio = i / float(len(self.trail))
                    trail_alpha = int(ratio * (1.0 - flight_t * 0.4) * 230)
                    trail_width = max(1.5, ratio * 7.5 * scale)
                    
                    pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], max(0, min(255, trail_alpha))), trail_width)
                    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                    painter.setPen(pen)
                    painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

            # Dragon sprite
            wobble = math.sin(flight_t * 14.0) * 0.12
            sw = self.tw * 0.75 * scale * (1.0 + wobble)
            sh = self.th * 0.75 * scale * (1.0 - wobble)

            painter.save()
            painter.translate(px, py)
            painter.rotate(angle_deg)

            glow_rad = 80 * scale
            glow_radial = QRadialGradient(QPointF(0, 0), glow_rad)
            glow_radial.setColorAt(0.0, QColor(255, 255, 255, int((1.0 - flight_t * 0.3) * 220)))
            glow_radial.setColorAt(0.3, QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int((1.0 - flight_t * 0.3) * 180)))
            glow_radial.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(glow_radial))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(0, 0), glow_rad, glow_rad)

            painter.drawPixmap(QRectF(-sw / 2.0, -sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.restore()

        # 2. Central Impact Burst (0.50 to 0.90)
        if 0.50 <= t <= 0.90:
            impact_t = (t - 0.50) / 0.40
            burst_alpha = int(max(0, math.sin(impact_t * math.pi) * 220))
            burst_radius = 100 + impact_t * 300
            burst = QRadialGradient(QPointF(cx, cy), burst_radius)
            burst.setColorAt(0.0, QColor(255, 255, 255, burst_alpha))
            burst.setColorAt(0.4, QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int(burst_alpha * 0.7)))
            burst.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(burst))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

        # 3. Glowing Frame Expansion (0.60 to 1.0)
        if t >= 0.60:
            frame_t = (t - 0.60) / 0.40
            frame_alpha = int(math.sin(frame_t * math.pi) * 255)
            glow_thickness = max(1.0, (1.0 - frame_t) * 6.0)

            # Outer glow
            outer_pen = QPen(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int(frame_alpha * 0.75)), glow_thickness + 2.0)
            painter.setPen(outer_pen)
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawRoundedRect(QRectF(self.tx, self.ty, self.tw, self.th), 6.0, 6.0)

            # Core sharp 2px line
            core_pen = QPen(QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], frame_alpha), 2.0)
            painter.setPen(core_pen)
            painter.drawRoundedRect(QRectF(self.tx, self.ty, self.tw, self.th), 6.0, 6.0)

    def paint_close(self, painter, t, cx, cy):
        # 1. Inward Frame Implosion (0.0 to 0.45)
        if t <= 0.45:
            imp_t = t / 0.45
            scale_frame = 1.0 - imp_t * 0.85
            bw = self.tw * scale_frame
            bh = self.th * scale_frame
            bx = cx - bw / 2.0
            by = cy - bh / 2.0

            frame_alpha = int((1.0 - imp_t) * 255)
            glow_thickness = max(1.0, (1.0 - imp_t) * 5.0)

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
                painter.setBrush(QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], max(0, min(255, p_alpha))))
                painter.drawEllipse(QPointF(p["x"], p["y"]), p["size"], p["size"])

        # 2. Summon shockwave (0.35 to 0.70)
        if 0.35 <= t <= 0.70:
            summon_t = (t - 0.35) / 0.35
            burst_alpha = int(max(0, math.sin(summon_t * math.pi) * 230))
            burst_radius = 60 + summon_t * 260
            burst = QRadialGradient(QPointF(cx, cy), burst_radius)
            burst.setColorAt(0.0, QColor(255, 255, 255, burst_alpha))
            burst.setColorAt(0.5, QColor(CORE_RGB[0], CORE_RGB[1], CORE_RGB[2], int(burst_alpha * 0.7)))
            burst.setColorAt(1.0, QColor(0, 0, 0, 0))
            painter.setBrush(QBrush(burst))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

            dragon_scale = min(1.0, summon_t * 1.8) * (min(self.tw, self.th) / 620.0)
            dw = TARGET_WIDTH * 0.85 * dragon_scale
            dh = TARGET_HEIGHT * 0.85 * dragon_scale
            painter.setOpacity(min(1.0, summon_t * 2.0))
            painter.drawPixmap(QRectF(cx - dw / 2.0, cy - dh / 2.0, dw, dh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
            painter.setOpacity(1.0)

        # 3. Takeoff Spiral (0.60 to 1.0)
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
            glow_radial.setColorAt(0.0, QColor(255, 255, 255, int((1.0 - takeoff_t) * 200)))
            glow_radial.setColorAt(0.4, QColor(GLOW_RGB[0], GLOW_RGB[1], GLOW_RGB[2], int((1.0 - takeoff_t) * 180)))
            glow_radial.setColorAt(1.0, QColor(0, 0, 0, 0))
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

        self.known_windows = {}

        clean_all_window_opacities()

        clients = get_client_list()
        for wid in clients:
            if is_app_window(wid):
                geo = get_window_geometry(wid)
                if geo and geo[2] > 150 and geo[3] > 120:
                    self.known_windows[wid] = (geo[0], geo[1], geo[2], geo[3])

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

            enforce_window_geometry(wid, TARGET_WIDTH, TARGET_HEIGHT, pos_x, pos_y)
            self.overlay.start_open_animation(wid, pos_x, pos_y, TARGET_WIDTH, TARGET_HEIGHT)

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

def cleanup_and_exit(signum, frame):
    clean_all_window_opacities()
    sys.exit(0)

def main():
    signal.signal(signal.SIGTERM, cleanup_and_exit)
    signal.signal(signal.SIGINT, cleanup_and_exit)

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

    clean_all_window_opacities()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
