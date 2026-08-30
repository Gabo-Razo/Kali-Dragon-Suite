#!/usr/bin/env python3
"""
🐉 KALI DRAGON SUITE - ULTRA-RESILIENT WINDOW ANIMATION DAEMON
Vibrant 60 FPS Dragon Flight & Impact Plasma Shockwave on Window Open/Close.
100% Non-intrusive: Never touches window opacity or properties.
"""

import sys, os, time, math, random, json, signal, subprocess, threading, re
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, QObject, pyqtSignal
from PyQt6.QtGui import QPainter, QColor, QRadialGradient, QBrush, QPen, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget

def get_color_config():
    cfg_path = os.path.expanduser("~/.local/share/dragon-anim/color_config.json")
    if os.path.exists(cfg_path):
        try:
            with open(cfg_path, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"primary": "#ffab00", "glow": "rgba(255, 171, 0, 0.45)", "hex": "#ffd700", "rgb": [255, 215, 0]}

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
        out = subprocess.check_output(["xprop", "-id", str(wid), "_NET_WM_WINDOW_TYPE", "WM_CLASS", "_NET_WM_STATE"], stderr=subprocess.DEVNULL, timeout=0.2).decode()
        out_lower = out.lower()
        if any(skip in out_lower for skip in ["_dock", "_desktop", "_notification", "_tooltip", "_menu", "_splash", "_hidden"]):
            return False
        if any(skip in out_lower for skip in ["xfce4-panel", "plank", "conky", "desktop", "wrapper"]):
            return False
        return True
    except Exception:
        return False

class AnimationTarget:
    def __init__(self, mode, x, y, w, h):
        self.mode = mode
        self.x = x
        self.y = y
        self.w = max(250, w)
        self.h = max(180, h)
        self.progress = 0.0
        self.trail = []
        self.particles = []
        
        cx = x + w / 2.0
        cy = y + h / 2.0
        if mode == "CLOSE":
            for _ in range(35):
                angle = random.uniform(0, 2 * math.pi)
                dist = random.uniform(min(w, h) * 0.3, max(w, h) * 0.6)
                self.particles.append({
                    "x": cx + math.cos(angle) * dist,
                    "y": cy + math.sin(angle) * dist,
                    "target_x": cx,
                    "target_y": cy,
                    "size": random.uniform(3.0, 7.0),
                    "speed": random.uniform(0.10, 0.25),
                    "alpha": random.uniform(0.7, 1.0)
                })

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
        self.active_animations = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animations)

    def reload_assets(self):
        self.color_cfg = get_color_config()
        self.rgb = tuple(self.color_cfg.get("rgb", [255, 215, 0]))
        self.primary_hex = self.color_cfg.get("primary", "#ffab00")
        self.core_hex = self.color_cfg.get("hex", "#ffd700")
        
        sprite_path = os.path.expanduser("~/.local/share/dragon-anim/dragon_sprite.png")
        if not os.path.exists(sprite_path):
            sprite_path = "/home/gr/Escritorio/Kali-Red-Dragon-Suite/variants/gold/desktop/animator/dragon_sprite.png"
        self.dragon_pixmap = QPixmap(sprite_path)

    def add_animation(self, mode, x, y, w, h):
        self.reload_assets()
        target = AnimationTarget(mode, x, y, w, h)
        self.active_animations.append(target)

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        if not self.isVisible():
            self.show()
        if not self.timer.isActive():
            self.timer.start(16)
        self.update()

    def update_animations(self):
        if not self.active_animations:
            self.timer.stop()
            self.hide()
            return

        surviving = []
        for anim in self.active_animations:
            anim.progress += 0.035 # ~500ms smooth animation
            if anim.progress < 1.0:
                surviving.append(anim)

        self.active_animations = surviving
        self.update()

    def paintEvent(self, event):
        if not self.active_animations:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)

        r, g, b = self.rgb

        for anim in self.active_animations:
            t = anim.progress
            cx = anim.x + anim.w / 2.0
            cy = anim.y + anim.h / 2.0

            if anim.mode == "OPEN":
                # 1. Orbital Dragon Flight (0.0 to 0.70)
                if t <= 0.70:
                    flight_t = t / 0.70
                    angle = (1.0 - flight_t) * 1.8 * math.pi - (math.pi / 4.0)
                    rad_x = (anim.w / 2.0) + 70.0 * (1.0 - flight_t)
                    rad_y = (anim.h / 2.0) + 50.0 * (1.0 - flight_t)
                    
                    px = cx + math.cos(angle) * rad_x
                    py = cy + math.sin(angle) * rad_y

                    anim.trail.append((px, py))
                    if len(anim.trail) > 20:
                        anim.trail.pop(0)

                    # Plasma trail ribbon
                    if len(anim.trail) > 2:
                        for i in range(len(anim.trail) - 1):
                            p1 = anim.trail[i]
                            p2 = anim.trail[i + 1]
                            ratio = i / float(len(anim.trail))
                            alpha = int(ratio * (1.0 - flight_t * 0.4) * 240)
                            width = max(2.0, ratio * 6.5)
                            pen = QPen(QColor(r, g, b, max(0, min(255, alpha))), width)
                            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
                            painter.setPen(pen)
                            painter.drawLine(QPointF(p1[0], p1[1]), QPointF(p2[0], p2[1]))

                    # Flying Dragon Sprite
                    dw = min(160.0, anim.w * 0.40)
                    dh = dw
                    painter.save()
                    painter.translate(px, py)
                    painter.rotate(math.degrees(angle) + 90)
                    painter.setOpacity(min(1.0, flight_t * 2.5) * (1.0 - max(0.0, flight_t - 0.7) * 3.3))
                    painter.drawPixmap(QRectF(-dw/2.0, -dh/2.0, dw, dh), self.dragon_pixmap, QRectF(self.dragon_pixmap.rect()))
                    painter.restore()

                # 2. Central Burst & Expanding Shockwave (0.35 to 1.0)
                if t >= 0.35:
                    burst_t = (t - 0.35) / 0.65
                    burst_alpha = int(max(0, math.sin(burst_t * math.pi) * 220))
                    
                    # Expanding Frame Glow
                    frame_scale = 0.88 + burst_t * 0.12
                    fw = anim.w * frame_scale
                    fh = anim.h * frame_scale
                    fx = cx - fw / 2.0
                    fy = cy - fh / 2.0
                    
                    pen = QPen(QColor(r, g, b, burst_alpha), 3.0)
                    painter.setPen(pen)
                    painter.setBrush(Qt.BrushStyle.NoBrush)
                    painter.drawRoundedRect(QRectF(fx, fy, fw, fh), 8.0, 8.0)

                    # Core Shockwave
                    rad = min(anim.w, anim.h) * 0.50 * (0.3 + burst_t * 0.7)
                    radial = QRadialGradient(QPointF(cx, cy), rad)
                    radial.setColorAt(0.0, QColor(255, 255, 255, int(burst_alpha * 0.85)))
                    radial.setColorAt(0.5, QColor(r, g, b, int(burst_alpha * 0.55)))
                    radial.setColorAt(1.0, QColor(0, 0, 0, 0))
                    painter.setBrush(QBrush(radial))
                    painter.setPen(Qt.PenStyle.NoPen)
                    painter.drawEllipse(QPointF(cx, cy), rad, rad)

            elif anim.mode == "CLOSE":
                # Inward Vortex Collapse
                collapse_t = t
                alpha = int(max(0, (1.0 - collapse_t) * 230))
                
                painter.setPen(Qt.PenStyle.NoPen)
                for p in anim.particles:
                    p["x"] += (p["target_x"] - p["x"]) * p["speed"] * 2.0
                    p["y"] += (p["target_y"] - p["y"]) * p["speed"] * 2.0
                    p_alpha = int(p["alpha"] * alpha)
                    painter.setBrush(QColor(r, g, b, max(0, min(255, p_alpha))))
                    painter.drawEllipse(QPointF(p["x"], p["y"]), p["size"], p["size"])

                rad = min(anim.w, anim.h) * 0.40 * (1.0 - collapse_t * 0.75)
                radial = QRadialGradient(QPointF(cx, cy), rad)
                radial.setColorAt(0.0, QColor(255, 255, 255, int(alpha * 0.75)))
                radial.setColorAt(0.6, QColor(r, g, b, int(alpha * 0.45)))
                radial.setColorAt(1.0, QColor(0, 0, 0, 0))
                painter.setBrush(QBrush(radial))
                painter.drawEllipse(QPointF(cx, cy), rad, rad)

class ClientEventBridge(QObject):
    clients_changed = pyqtSignal(list)

class EventDrivenWindowManager:
    def __init__(self, overlay):
        self.overlay = overlay
        self.bridge = ClientEventBridge()
        self.bridge.clients_changed.connect(self.on_clients_changed)
        self.known_windows = {}

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

        # 1. New Windows Opened
        new_windows = current_set - known_set
        for wid in new_windows:
            if not is_normal_app_window(wid):
                continue
            
            def handle_new_win(w_id):
                time.sleep(0.06) # Let window manager map and position window
                geo = get_window_geometry(w_id)
                if geo:
                    self.known_windows[w_id] = geo
                    self.overlay.add_animation("OPEN", geo[0], geo[1], geo[2], geo[3])
                    
            threading.Thread(target=handle_new_win, args=(wid,), daemon=True).start()

        # 2. Closed Windows
        closed_windows = known_set - current_set
        for wid in closed_windows:
            last_geo = self.known_windows.pop(wid, None)
            if last_geo:
                self.overlay.add_animation("CLOSE", last_geo[0], last_geo[1], last_geo[2], last_geo[3])

        # 3. Update active window geometries
        for wid in current_set.intersection(set(self.known_windows.keys())):
            if is_normal_app_window(wid):
                geo = get_window_geometry(wid)
                if geo:
                    self.known_windows[wid] = geo

def main():
    pid_file = "/tmp/dragon-animator.pid"
    if os.path.exists(pid_file):
        try:
            with open(pid_file, "r") as f:
                old_pid = int(f.read().strip())
            os.kill(old_pid, signal.SIGTERM)
            time.sleep(0.15)
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
