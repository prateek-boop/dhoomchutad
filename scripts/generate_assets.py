"""
EduEagle Asset Generator: Pure Python Standard Library
Generates:
- favicon-16x16.png
- favicon-32x32.png
- apple-touch-icon.png (180x180)
- favicon.ico (multi-resolution 16x16 and 32x32)
- og-image.png (1200x630)
- og-image.svg
"""

import os
import zlib
import struct
import math

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(CURR_DIR) if os.path.basename(CURR_DIR) in ("scripts", "scratch") else CURR_DIR
STATIC_DIR = os.path.join(REPO_ROOT, "static")

def write_png(filepath, width, height, rgba_buffer):
    raw = bytearray()
    stride = width * 4
    for y in range(height):
        raw.append(0) # Filter None
        offset = y * stride
        raw.extend(rgba_buffer[offset:offset+stride])

    def chunk(tag, data):
        crc = zlib.crc32(tag + data) & 0xffffffff
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)

    png_bytes = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(bytes(raw), level=9))
        + chunk(b"IEND", b"")
    )
    with open(filepath, "wb") as f:
        f.write(png_bytes)
    return png_bytes

def write_ico(filepath, png_list):
    header = struct.pack("<HHH", 0, 1, len(png_list))
    entries = bytearray()
    offset = 6 + 16 * len(png_list)
    image_data = bytearray()

    for w, h, data in png_list:
        w_b = 0 if w >= 256 else w
        h_b = 0 if h >= 256 else h
        size = len(data)
        entries.extend(struct.pack("<BBBBHHII", w_b, h_b, 0, 0, 1, 32, size, offset + len(image_data)))
        image_data.extend(data)

    with open(filepath, "wb") as f:
        f.write(header + entries + image_data)

class Canvas:
    def __init__(self, width, height, bg=(10, 15, 29, 255)):
        self.w = width
        self.h = height
        self.buf = bytearray(bg * (width * height))

    def set_pixel(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            idx = (y * self.w + x) * 4
            if len(color) == 3:
                r, g, b = color
                a = 255
            else:
                r, g, b, a = color
            if a == 255:
                self.buf[idx:idx+4] = bytes([r, g, b, a])
            elif a > 0:
                # Alpha blend
                sa = a / 255.0
                da = 1.0 - sa
                self.buf[idx] = int(r * sa + self.buf[idx] * da)
                self.buf[idx+1] = int(g * sa + self.buf[idx+1] * da)
                self.buf[idx+2] = int(b * sa + self.buf[idx+2] * da)
                self.buf[idx+3] = 255

    def fill_rect(self, x, y, w, h, color):
        for cy in range(max(0, y), min(self.h, y + h)):
            for cx in range(max(0, x), min(self.w, x + w)):
                self.set_pixel(cx, cy, color)

    def draw_rect(self, x, y, w, h, color, thickness=1):
        self.fill_rect(x, y, w, thickness, color)
        self.fill_rect(x, y + h - thickness, w, thickness, color)
        self.fill_rect(x, y, thickness, h, color)
        self.fill_rect(x + w - thickness, y, thickness, h, color)

    def draw_shield(self, cx, cy, radius, fill_color, border_color, border_w=2):
        for py in range(int(cy - radius), int(cy + radius * 1.2)):
            for px in range(int(cx - radius), int(cx + radius + 1)):
                dx = abs(px - cx) / radius
                dy = (py - cy) / radius
                if -0.8 <= dy <= 0.2:
                    inside = dx <= 0.85
                elif 0.2 < dy <= 1.15:
                    t = (dy - 0.2) / 0.95
                    max_dx = 0.85 * (1.0 - t ** 1.3)
                    inside = dx <= max_dx
                else:
                    inside = False

                if inside:
                    if dx > 0.75 or dy > 0.95:
                        self.set_pixel(px, py, border_color)
                    else:
                        self.set_pixel(px, py, fill_color)

    def draw_char(self, char, x, y, color, scale=1):
        glyph = FONT_5X7.get(char.upper(), FONT_5X7.get('?'))
        for row_idx, row in enumerate(glyph):
            for col_idx, bit in enumerate(row):
                if bit == '1':
                    self.fill_rect(x + col_idx * scale, y + row_idx * scale, scale, scale, color)

    def draw_text(self, text, x, y, color, scale=1, spacing=1):
        cx = x
        for ch in text:
            if ch == ' ':
                cx += 4 * scale
            else:
                self.draw_char(ch, cx, y, color, scale)
                cx += (5 + spacing) * scale

FONT_5X7 = {
    'A': ['01110','10001','10001','11111','10001','10001','10001'],
    'B': ['11110','10001','10001','11110','10001','10001','11110'],
    'C': ['01111','10000','10000','10000','10000','10000','01111'],
    'D': ['11110','10001','10001','10001','10001','10001','11110'],
    'E': ['11111','10000','10000','11110','10000','10000','11111'],
    'F': ['11111','10000','10000','11110','10000','10000','10000'],
    'G': ['01111','10000','10000','10111','10001','10001','01110'],
    'H': ['10001','10001','10001','11111','10001','10001','10001'],
    'I': ['11111','00100','00100','00100','00100','00100','11111'],
    'J': ['00111','00010','00010','00010','00010','10010','01100'],
    'K': ['10001','10010','10100','11000','10100','10010','10001'],
    'L': ['10000','10000','10000','10000','10000','10000','11111'],
    'M': ['10001','11011','10101','10101','10001','10001','10001'],
    'N': ['10001','11001','10101','10011','10001','10001','10001'],
    'O': ['01110','10001','10001','10001','10001','10001','01110'],
    'P': ['11110','10001','10001','11110','10000','10000','10000'],
    'Q': ['01110','10001','10001','10001','10101','10011','01101'],
    'R': ['11110','10001','10001','11110','10100','10010','10001'],
    'S': ['01111','10000','10000','01110','00001','00001','11110'],
    'T': ['11111','00100','00100','00100','00100','00100','00100'],
    'U': ['10001','10001','10001','10001','10001','10001','01110'],
    'V': ['10001','10001','10001','10001','10001','01010','00100'],
    'W': ['10001','10001','10001','10101','10101','11011','10001'],
    'X': ['10001','10001','01010','00100','01010','10001','10001'],
    'Y': ['10001','10001','01010','00100','00100','00100','00100'],
    'Z': ['11111','00001','00010','00100','01000','10000','11111'],
    '0': ['01110','10011','10101','10101','11001','10001','01110'],
    '1': ['00100','01100','00100','00100','00100','00100','01110'],
    '2': ['01110','10001','00001','00110','01000','10000','11111'],
    '3': ['01110','10001','00001','00110','00001','10001','01110'],
    '4': ['00010','00110','01010','10010','11111','00010','00010'],
    '5': ['11111','10000','11110','00001','00001','10001','01110'],
    '6': ['01110','10000','11110','10001','10001','10001','01110'],
    '7': ['11111','00001','00010','00100','01000','01000','01000'],
    '8': ['01110','10001','10001','01110','10001','10001','01110'],
    '9': ['01110','10001','10001','01111','00001','00001','01110'],
    '-': ['00000','00000','00000','11111','00000','00000','00000'],
    '|': ['00100','00100','00100','00100','00100','00100','00100'],
    '.': ['00000','00000','00000','00000','00000','01100','01100'],
    ':': ['00000','01100','01100','00000','01100','01100','00000'],
    '&': ['01100','10010','10100','01000','10101','10010','01101'],
    '?': ['01110','10001','00010','00100','00100','00000','00100'],
}

def generate_icon(size):
    c = Canvas(size, size, bg=(15, 23, 42, 255))
    cx = size // 2
    cy = size // 2
    radius = size * 0.38
    c.draw_shield(cx, cy, radius, fill_color=(30, 41, 59), border_color=(37, 99, 235))
    cap_r = int(radius * 0.45)
    for dy in range(-cap_r, cap_r + 1):
        for dx in range(-cap_r * 2, cap_r * 2 + 1):
            if abs(dx) + abs(dy) * 2 <= cap_r * 2:
                c.set_pixel(cx + dx, cy - int(radius * 0.1) + dy, (56, 189, 248))
    return c

def generate_og_image():
    w, h = 1200, 630
    c = Canvas(w, h, bg=(10, 15, 29, 255))
    
    c.draw_rect(24, 24, w - 48, h - 48, color=(36, 52, 77), thickness=2)
    c.fill_rect(24, 24, w - 48, 6, color=(37, 99, 235))
    
    c.fill_rect(60, 60, w - 120, h - 120, color=(15, 23, 42))
    c.draw_rect(60, 60, w - 120, h - 120, color=(30, 41, 59), thickness=1)

    shield_cx, shield_cy = 160, 200
    shield_radius = 65
    c.draw_shield(shield_cx, shield_cy, shield_radius, fill_color=(30, 41, 59), border_color=(37, 99, 235))
    for dy in range(-25, 26):
        for dx in range(-50, 51):
            if abs(dx) + abs(dy) * 2 <= 50:
                c.set_pixel(shield_cx + dx, shield_cy - 10 + dy, (56, 189, 248))

    c.draw_text("EDUEAGLE", 260, 150, color=(241, 245, 249), scale=8, spacing=2)
    c.draw_text("STUDENT SUCCESS & INTERVENTION ENGINE", 265, 230, color=(56, 189, 248), scale=3, spacing=1)
    
    c.fill_rect(100, 280, w - 200, 2, color=(36, 52, 77))

    card_w = 310
    card_h = 160
    card_y = 315

    c.fill_rect(100, card_y, card_w, card_h, color=(21, 31, 50))
    c.draw_rect(100, card_y, card_w, card_h, color=(36, 52, 77), thickness=1)
    c.fill_rect(100, card_y, card_w, 4, color=(56, 189, 248))
    c.draw_text("STUDENT 360", 120, card_y + 25, color=(241, 245, 249), scale=3)
    c.draw_text("UNIFIED ACADEMIC DOSSIER", 120, card_y + 60, color=(148, 163, 184), scale=2)
    c.draw_text("ATTENDANCE & GRADES", 120, card_y + 85, color=(100, 116, 139), scale=2)
    c.draw_text("CONTINUOUS EVALUATION", 120, card_y + 110, color=(100, 116, 139), scale=2)

    c.fill_rect(445, card_y, card_w, card_h, color=(21, 31, 50))
    c.draw_rect(445, card_y, card_w, card_h, color=(36, 52, 77), thickness=1)
    c.fill_rect(445, card_y, card_w, 4, color=(37, 99, 235))
    c.draw_text("RISK DRIVERS", 465, card_y + 25, color=(241, 245, 249), scale=3)
    c.draw_text("EXPLAINABLE ATTRIBUTION", 465, card_y + 60, color=(148, 163, 184), scale=2)
    c.draw_text("FACTOR IMPACT METRICS", 465, card_y + 85, color=(100, 116, 139), scale=2)
    c.draw_text("TRANSPARENT SCORING", 465, card_y + 110, color=(100, 116, 139), scale=2)

    c.fill_rect(790, card_y, card_w, card_h, color=(21, 31, 50))
    c.draw_rect(790, card_y, card_w, card_h, color=(36, 52, 77), thickness=1)
    c.fill_rect(790, card_y, card_w, 4, color=(22, 163, 74))
    c.draw_text("GOVERNANCE", 810, card_y + 25, color=(241, 245, 249), scale=3)
    c.draw_text("FERPA RECORD PROTECTION", 810, card_y + 60, color=(148, 163, 184), scale=2)
    c.draw_text("NON-PUNITIVE POLICY", 810, card_y + 85, color=(100, 116, 139), scale=2)
    c.draw_text("MANDATORY HUMAN OVERRIDE", 810, card_y + 110, color=(100, 116, 139), scale=2)

    c.draw_text("INSTITUTIONAL GRADE ACADEMIC ADVISORY PLATFORM | HTTPS://EDUEAGLE.EDU", 100, 520, color=(100, 116, 139), scale=2)

    return c

def main():
    print(f"Generating assets into {STATIC_DIR}...")
    os.makedirs(STATIC_DIR, exist_ok=True)
    os.makedirs(os.path.join(STATIC_DIR, "images"), exist_ok=True)

    print("Building favicon assets...")
    c16 = generate_icon(16)
    p16 = write_png(os.path.join(STATIC_DIR, "favicon-16x16.png"), 16, 16, c16.buf)

    c32 = generate_icon(32)
    p32 = write_png(os.path.join(STATIC_DIR, "favicon-32x32.png"), 32, 32, c32.buf)

    c180 = generate_icon(180)
    p180 = write_png(os.path.join(STATIC_DIR, "apple-touch-icon.png"), 180, 180, c180.buf)

    write_ico(os.path.join(STATIC_DIR, "favicon.ico"), [(16, 16, p16), (32, 32, p32)])
    print("Favicons and ICO generated.")

    print("Building Open Graph preview image (1200x630)...")
    c_og = generate_og_image()
    write_png(os.path.join(STATIC_DIR, "images", "og-image.png"), 1200, 630, c_og.buf)
    write_png(os.path.join(STATIC_DIR, "og-image.png"), 1200, 630, c_og.buf)
    print("OG images generated successfully.")

if __name__ == "__main__":
    main()
