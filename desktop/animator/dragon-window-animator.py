#!/usr/bin/env python3
"""
🐉 KALI DRAGON SUITE - MASTER 60 FPS WINDOW ANIMATOR (PROPORTIONAL 1:1 SPRITE)
- Strict 1:1 Natural Aspect Ratio Preservation (Zero squish, flattening or distortion).
- 100% Contained within window interior bounds.
- Silk-smooth organic easing, tangent banking, resplandor shockwave & window crystallization.
"""

import sys, os, time, math, random, json, signal, subprocess, threading, re
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPainter, QColor, QRadialGradient, QBrush, QPen, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget

MY_PID = os.getpid()

def get_color_config():
    cfg_path = os.path.expanduser("~/.local/share/dragon-anim/color_config.json")
    if os.path.exists(cfg_path):
        try:
            with open(cfg_path, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"primary": "#ffab00", "glow": "rgba(255, 171, 0, 0.45)", "hex": "#ffd700", "rgb": [255, 215, 0]}

def clean_window_opacity(wid):
    if not wid:
        return
    try:
        subprocess.run(["xprop", "-id", str(wid), "-remove", "_NET_WM_WINDOW_OPACITY"], stderr=subprocess.DEVNULL, timeout=0.15)
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
        out = subprocess.check_output(["xdotool", "getwindowgeometry", "--shell", str(wid)], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        x, y, w, h = 0, 0, 0, 0
        for line in out.strip().split("\n"):
            if line.startswith("X="): x = int(line.split("=")[1])
            elif line.startswith("Y="): y = int(line.split("=")[1])
            elif line.startswith("WIDTH="): w = int(line.split("=")[1])
            elif line.startswith("HEIGHT="): h = int(line.split("=")[1])
        if w > 100 and h > 80:
            return (x, y, w, h)
    except Exception:
        pass
    return None

def is_normal_app_window(wid):
    try:
        pid_out = subprocess.check_output(["xprop", "-id", str(wid), "_NET_WM_PID"], stderr=subprocess.DEVNULL, timeout=0.15).decode()
        m_pid = re.search(r"= (\d+)", pid_out)
        if m_pid and int(m_pid.group(1)) == MY_PID:
            return False

        out = subprocess.check_output(["xprop", "-id", str(wid), "_NET_WM_WINDOW_TYPE", "WM_CLASS", "_NET_WM_STATE"], stderr=subprocess.DEVNULL, timeout=0.15).decode()
        out_lower = out.lower()
        if any(skip in out_lower for skip in ["_dock", "_desktop", "_notification", "_tooltip", "_menu", "_splash", "_hidden", "combobox"]):
            return False
        if any(skip in out_lower for skip in ["xfce4-panel", "plank", "conky", "desktop", "wrapper", "dragon", "python"]):
            return False
        return True
    except Exception:
        return False

class AnimationBridge(QObject):
    open_signal = pyqtSignal(int, int, int, int, int)
    close_signal = pyqtSignal(int, int, int, int)

class DragonOverlay(QWidget):
    def __init__(self, bridge):
        super().__init__()
        self.bridge = bridge
        self.bridge.open_signal.connect(self.start_open_animation)
        self.bridge.close_signal.connect(self.start_close_animation)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.X11BypassWindowManagerHint
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self.reload_assets()

        self.anim_progress = 0.0
        self.is_animating = False
        self.anim_mode = "OPEN"

        self.active_wid = None
        self.tx = 200
        self.ty = 150
        self.tw = 800
        self.th = 500

        self.trail = []
        self.particles = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)

    def reload_assets(self):
        self.color_cfg = get_color_config()
        self.rgb = tuple(self.color_cfg.get("rgb", [255, 215, 0]))
        self.primary_hex = self.color_cfg.get("primary", "#ffab00")
        self.core_hex = self.color_cfg.get("hex", "#ffd700")

        sprite_path = os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")
        if not os.path.exists(sprite_path):
            sprite_path = "/home/gr/Escritorio/Kali-Red-Dragon-Suite/variants/gold/desktop/animator/dragon_sprite.png"
        self.dragon_pixmap = QPixmap(sprite_path)
        
        # Calculate natural aspect ratio (Width / Height)
        pw = float(self.dragon_pixmap.width())
        ph = float(self.dragon_pixmap.height())
        self.aspect_ratio = (pw / ph) if ph > 0 else 1.46

    @pyqtSlot(int, int, int, int, int)
    def start_open_animation(self, wid, x, y, w, h):
        self.reload_assets()
        self.anim_mode = "OPEN"
        self.active_wid = wid
        self.tx = x
        self.ty = y
        self.tw = max(260, w)
        self.th = max(180, h)
        self.anim_progress = 0.0
        self.is_animating = True
        self.trail = []
        self.particles = []

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        set_window_opacity(wid, 0.0)
        QTimer.singleShot(700, lambda: clean_window_opacity(wid))

        if not self.isVisible():
            self.show()
        if not self.timer.isActive():
            self.timer.start(16)
        self.update()

    @pyqtSlot(int, int, int, int)
    def start_close_animation(self, x, y, w, h):
        self.reload_assets()
        self.anim_mode = "CLOSE"
        self.active_wid = None
        self.tx = x
        self.ty = y
        self.tw = max(260, w)
        self.th = max(180, h)
        self.anim_progress = 0.0
        self.is_animating = True
        self.trail = []
        self.particles = []

        cx = x + w / 2.0
        cy = y + h / 2.0
        for _ in range(35):
            angle = random.uniform(0, 2 * math.pi)
            dist = random.uniform(min(w, h) * 0.20, min(w, h) * 0.45)
            self.particles.append({
                "x": cx + math.cos(angle) * dist,
                "y": cy + math.sin(angle) * dist,
                "target_x": cx,
                "target_y": cy,
                "size": random.uniform(2.5, 5.5),
                "speed": random.uniform(0.12, 0.22),
                "alpha": random.uniform(0.7, 1.0)
            })

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        if not self.isVisible():
            self.show()
        if not self.timer.isActive():
            self.timer.start(16)
        self.update()

    def get_contained_flight_state(self, t, is_reverse=False):
        cx = self.tx + self.tw / 2.0
        cy = self.ty + self.th / 2.0
        
        prog = t * t * (3.0 - 2.0 * t)
        rx = self.tw * 0.38
        ry = self.th * 0.38

        if not is_reverse:
            angle = -math.pi * 0.75 + prog * (math.pi * 2.0)
            cur_rx = rx * (1.0 - prog * 0.85)
            cur_ry = ry * (1.0 - prog * 0.85)
            scale = 0.50 + 0.50 * math.sin(t * math.pi)
        else:
            angle = math.pi * 0.25 + prog * (math.pi * 1.8)
            cur_rx = rx * (0.2 + prog * 0.65)
            cur_ry = ry * (0.2 + prog * 0.65)
            scale = 1.0 - 0.70 * prog

        px = cx + math.cos(angle) * cur_rx
        py = cy + math.sin(angle) * cur_ry

        dt = 0.02
        prog_next = (t + dt) * (t + dt) * (3.0 - 2.0 * (t + dt))
        if not is_reverse:
            angle_next = -math.pi * 0.75 + prog_next * (math.pi * 2.0)
            p_next_x = cx + math.cos(angle_next) * (rx * (1.0 - prog_next * 0.85))
            p_next_y = cy + math.sin(angle_next) * (ry * (1.0 - prog_next * 0.85))
        else:
            angle_next = math.pi * 0.25 + prog_next * (math.pi * 1.8)
            p_next_x = cx + math.cos(angle_next) * (rx * (0.2 + prog_next * 0.65))
            p_next_y = cy + math.sin(angle_next) * (ry * (0.2 + prog_next * 0.65))

        vx = p_next_x - px
        vy = p_next_y - py
        angle_deg = math.degrees(math.atan2(vy, vx))
        return px, py, angle_deg, scale

    def update_animation(self):
        if not self.is_animating:
            return

        self.anim_progress += 0.024

        if self.anim_mode == "OPEN" and self.active_wid:
            if self.anim_progress >= 0.45:
                fade_alpha = min(1.0, (self.anim_progress - 0.45) / 0.35)
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
        r, g, b = self.rgb

        if self.anim_mode == "OPEN":
            # 1. Flying Dragon Smooth Inner Orbit (0.0 to 0.70)
            if t <= 0.70:
                flight_t = t / 0.70
                px, py, angle_deg, scale = self.get_contained_flight_state(flight_t)

                self.trail.append((px, py, t))
                if len(self.trail) > 20:
                    self.trail.pop(0)

                # Fiery plasma ribbon trail
                if len(self.trail) > 2:
                    for i in range(len(self.trail) - 1):
                        p1 = self.trail[i]
                        p2 = self.trail[i + 1]
                        ratio = i / float(len(self.trail))
                        trail_alpha = int(ratio * (1.0 - flight_t * 0.4) * 230)
                        trail_width = max(1.5, ratio * 6.5 * scale)
                        
                        pen = QPen(QColor(r, g, b, max(0, min(255, trail_alpha))), trail_width)
                        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                        painter.setPen(pen)
                        painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

                # 100% Proportional, un-squished Dragon Sprite
                sw = min(170.0, min(self.tw, self.th) * 0.50) * scale
                sh = sw / self.aspect_ratio

                painter.save()
                painter.translate(px, py)
                painter.rotate(angle_deg)

                glow_rad = (sw / 2.0) * 1.1
                glow_radial = QRadialGradient(QPointF(0, 0), glow_rad)
                glow_radial.setColorAt(0.0, QColor(255, 255, 255, int((1.0 - flight_t * 0.3) * 220)))
                glow_radial.setColorAt(0.35, QColor(r, g, b, int((1.0 - flight_t * 0.3) * 180)))
                glow_radial.setColorAt(1.0, QColor(0, 0, 0, 0))
                painter.setBrush(QBrush(glow_radial))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPointF(0, 0), glow_rad, glow_rad)

                painter.drawPixmap(QRectF(-sw / 2.0, -sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
                painter.restore()

            # 2. Central Resplandor Shockwave & Window Frame Crystallization (0.45 to 0.95)
            if 0.45 <= t <= 0.95:
                impact_t = (t - 0.45) / 0.50
                burst_alpha = int(max(0, math.sin(impact_t * math.pi) * 230))
                burst_radius = 60 + impact_t * min(self.tw, self.th) * 0.45
                burst = QRadialGradient(QPointF(cx, cy), burst_radius)
                burst.setColorAt(0.0, QColor(255, 255, 255, burst_alpha))
                burst.setColorAt(0.4, QColor(r, g, b, int(burst_alpha * 0.7)))
                burst.setColorAt(1.0, QColor(0, 0, 0, 0))
                painter.setBrush(QBrush(burst))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

                frame_scale = 0.92 + impact_t * 0.08
                bw = self.tw * frame_scale
                bh = self.th * frame_scale
                bx = cx - bw / 2.0
                by = cy - bh / 2.0
                frame_alpha = int(max(0, math.sin(impact_t * math.pi) * 240))

                glow_thickness = max(2.0, (1.0 - impact_t) * 8.0)
                outer_pen = QPen(QColor(r, g, b, int(frame_alpha * 0.8)), glow_thickness + 2.0)
                painter.setPen(outer_pen)
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawRoundedRect(QRectF(bx, by, bw, bh), 8.0, 8.0)

                core_pen = QPen(QColor(255, 255, 255, frame_alpha), 2.0)
                painter.setPen(core_pen)
                painter.drawRoundedRect(QRectF(bx, by, bw, bh), 8.0, 8.0)

        elif self.anim_mode == "CLOSE":
            # 1. Inward Implosion strictly within the window boundaries
            if t <= 0.65:
                imp_t = t / 0.65
                frame_scale = 1.0 - imp_t * 0.20
                bw = self.tw * frame_scale
                bh = self.th * frame_scale
                bx = cx - bw / 2.0
                by = cy - bh / 2.0
                frame_alpha = int(max(0, (1.0 - imp_t) * 240))

                glow_thickness = max(1.5, (1.0 - imp_t) * 6.0)
                outer_pen = QPen(QColor(r, g, b, int(frame_alpha * 0.8)), glow_thickness + 2.0)
                painter.setPen(outer_pen)
                painter.setBrush(Qt.BrushStyle.NoBrush)
                painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

                core_pen = QPen(QColor(255, 255, 255, frame_alpha), 2.0)
                painter.setPen(core_pen)
                painter.drawRoundedRect(QRectF(bx, by, bw, bh), 6.0, 6.0)

                painter.setPen(Qt.PenStyle.NoPen)
                for p in self.particles:
                    p["x"] += (p["target_x"] - p["x"]) * p["speed"] * 2.2
                    p["y"] += (p["target_y"] - p["y"]) * p["speed"] * 2.2
                    p_alpha = int(p["alpha"] * 255 * (1.0 - imp_t * 0.3))
                    painter.setBrush(QColor(r, g, b, max(0, min(255, p_alpha))))
                    painter.drawEllipse(QPointF(p["x"], p["y"]), p["size"], p["size"])

            # 2. Central Dragon Summon & Disintegration (0.35 to 0.70)
            if 0.35 <= t <= 0.70:
                summon_t = (t - 0.35) / 0.35
                burst_alpha = int(max(0, math.sin(summon_t * math.pi) * 230))
                burst_radius = 40 + summon_t * min(self.tw, self.th) * 0.35
                burst = QRadialGradient(QPointF(cx, cy), burst_radius)
                burst.setColorAt(0.0, QColor(255, 255, 255, burst_alpha))
                burst.setColorAt(0.5, QColor(r, g, b, int(burst_alpha * 0.7)))
                burst.setColorAt(1.0, QColor(0, 0, 0, 0))
                painter.setBrush(QBrush(burst))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPointF(cx, cy), burst_radius, burst_radius)

                # 100% Proportional Dragon Sprite
                dragon_scale = min(1.0, summon_t * 1.6) * (min(self.tw, self.th) / 550.0)
                sw = min(180.0, min(self.tw, self.th) * 0.55) * dragon_scale
                sh = sw / self.aspect_ratio
                painter.setOpacity(min(1.0, summon_t * 2.0))
                painter.drawPixmap(QRectF(cx - sw / 2.0, cy - sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
                painter.setOpacity(1.0)

            # 3. Takeoff & Dissolution at Center (0.60 to 1.0)
            if t >= 0.60:
                takeoff_t = (t - 0.60) / 0.40
                px, py, angle_deg, scale = self.get_contained_flight_state(takeoff_t, is_reverse=True)

                self.trail.append((px, py, t))
                if len(self.trail) > 20:
                    self.trail.pop(0)

                if len(self.trail) > 2:
                    for i in range(len(self.trail) - 1):
                        p1 = self.trail[i]
                        p2 = self.trail[i + 1]
                        ratio = i / float(len(self.trail))
                        trail_alpha = int(ratio * (1.0 - takeoff_t) * 220)
                        trail_width = max(1.5, ratio * 5.5 * scale)
                        
                        pen = QPen(QColor(r, g, b, max(0, min(255, trail_alpha))), trail_width)
                        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                        painter.setPen(pen)
                        painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

                # 100% Proportional Dragon Sprite
                sw = min(160.0, min(self.tw, self.th) * 0.48) * scale
                sh = sw / self.aspect_ratio

                painter.save()
                painter.translate(px, py)
                painter.rotate(angle_deg)

                glow_rad = (sw / 2.0) * 1.1
                glow_radial = QRadialGradient(QPointF(0, 0), glow_rad)
                glow_radial.setColorAt(0.0, QColor(255, 255, 255, int((1.0 - takeoff_t) * 200)))
                glow_radial.setColorAt(0.4, QColor(r, g, b, int((1.0 - takeoff_t) * 180)))
                glow_radial.setColorAt(1.0, QColor(0, 0, 0, 0))
                painter.setBrush(QBrush(glow_radial))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawEllipse(QPointF(0, 0), glow_rad, glow_rad)

                painter.setOpacity(max(0.0, 1.0 - takeoff_t * 1.1))
                painter.drawPixmap(QRectF(-sw / 2.0, -sh / 2.0, sw, sh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
                painter.restore()

class EventDrivenWindowManager:
    def __init__(self, bridge):
        self.bridge = bridge
        self.known_windows = {}

        clean_all_window_opacities()

        for wid in get_client_list():
            if is_normal_app_window(wid):
                geo = get_window_geometry(wid)
                if geo:
                    self.known_windows[wid] = geo

        self.spy_thread = threading.Thread(target=self._spy_worker, daemon=True)
        self.spy_thread.start()

    def _spy_worker(self):
        try:
            proc = subprocess.Popen(
                ["xprop", "-root", "-spy", "_NET_CLIENT_LIST"],
                stdout=subprocess.PIPE,
                text=True
            )
            for line in iter(proc.stdout.readline, ''):
                if "_NET_CLIENT_LIST" in line:
                    match = re.search(r"# (.*)", line)
                    if match:
                        client_list = [int(x.strip(), 16) for x in match.group(1).split(",") if x.strip()]
                        self.on_clients_changed(client_list)
        except Exception:
            pass

    def on_clients_changed(self, current_clients):
        current_set = set(current_clients)
        known_set = set(self.known_windows.keys())

        # 1. New Windows Opened
        new_windows = current_set - known_set
        for wid in new_windows:
            if not is_normal_app_window(wid):
                continue

            set_window_opacity(wid, 0.0)
            self.known_windows[wid] = (0, 0, 0, 0)
            
            def handle_new_win(w_id):
                geo = None
                for _ in range(6):
                    time.sleep(0.04)
                    geo = get_window_geometry(w_id)
                    if geo:
                        break
                if geo:
                    self.known_windows[w_id] = geo
                    self.bridge.open_signal.emit(w_id, geo[0], geo[1], geo[2], geo[3])
                else:
                    clean_window_opacity(w_id)
                    self.known_windows.pop(w_id, None)
                    
            threading.Thread(target=handle_new_win, args=(wid,), daemon=True).start()

        # 2. Closed Windows
        closed_windows = known_set - current_set
        for wid in closed_windows:
            last_geo = self.known_windows.pop(wid, None)
            if last_geo and last_geo[2] > 80:
                self.bridge.close_signal.emit(last_geo[0], last_geo[1], last_geo[2], last_geo[3])

        # 3. Update active window geometries
        for wid in current_set.intersection(set(self.known_windows.keys())):
            if is_normal_app_window(wid):
                geo = get_window_geometry(wid)
                if geo:
                    self.known_windows[wid] = geo

def cleanup_and_exit(signum, frame):
    clean_all_window_opacities()
    sys.exit(0)

def main():
    global MY_PID
    MY_PID = os.getpid()

    signal.signal(signal.SIGTERM, cleanup_and_exit)
    signal.signal(signal.SIGINT, cleanup_and_exit)

    pid_file = "/tmp/dragon-animator.pid"
    if os.path.exists(pid_file):
        try:
            with open(pid_file, "r") as f:
                old_pid = int(f.read().strip())
            if old_pid != MY_PID:
                os.kill(old_pid, signal.SIGTERM)
                time.sleep(0.15)
        except Exception:
            pass
    with open(pid_file, "w") as f:
        f.write(str(MY_PID))

    clean_all_window_opacities()

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    bridge = AnimationBridge()
    overlay = DragonOverlay(bridge)
    manager = EventDrivenWindowManager(bridge)

    clean_all_window_opacities()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
