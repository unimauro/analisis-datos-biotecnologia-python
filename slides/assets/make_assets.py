"""Genera fondos biotech (teal Escuela Global) para el deck. Sin dependencias externas salvo Pillow."""
import math
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080  # 16:9 alta resolución
TEAL_DARK = (8, 38, 46)
TEAL = (21, 129, 88)      # #158158 acento de marca
TEAL_MID = (12, 74, 80)
CYAN = (36, 203, 229)     # #24CBE5 del tema

def vgrad(top, bottom):
    img = Image.new("RGB", (W, H), top)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    return img

def diag_glow(img, cx, cy, r, color, alpha):
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))
    glow = glow.filter(ImageFilter.GaussianBlur(r // 2))
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
    return img

def molecular_net(img, n=46, seed=7, alpha=46):
    """Red de nodos/aristas estilo 'molecular network' como el sílabo."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    pts = []
    s = seed
    def rnd():
        nonlocal s
        s = (s * 1103515245 + 12345) & 0x7fffffff
        return s / 0x7fffffff
    for _ in range(n):
        pts.append((rnd() * W, rnd() * H))
    for i, (x1, y1) in enumerate(pts):
        for (x2, y2) in pts[i + 1:]:
            dist = math.hypot(x1 - x2, y1 - y2)
            if dist < 230:
                a = int(alpha * (1 - dist / 230))
                d.line([(x1, y1), (x2, y2)], fill=CYAN + (a,), width=1)
    for (x, y) in pts:
        rr = 3
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=CYAN + (alpha + 30,))
    return Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")

def dna_helix(img, cx, top, bottom, amp=70, alpha=120):
    """Doble hélice vertical sutil."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    step = 14
    prev1 = prev2 = None
    y = top
    k = 0
    while y < bottom:
        ph = y / 46.0
        x1 = cx + math.sin(ph) * amp
        x2 = cx + math.sin(ph + math.pi) * amp
        if prev1:
            d.line([prev1, (x1, y)], fill=CYAN + (alpha,), width=3)
            d.line([prev2, (x2, y)], fill=TEAL + (alpha,), width=3)
        if k % 2 == 0:
            d.line([(x1, y), (x2, y)], fill=(255, 255, 255, alpha // 2), width=2)
        prev1, prev2 = (x1, y), (x2, y)
        y += step
        k += 1
    return Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")

# ---- Fondo PORTADA: full teal con red molecular + hélice a la derecha ----
cover = vgrad(TEAL_DARK, TEAL_MID)
cover = diag_glow(cover, int(W * 0.78), int(H * 0.30), 520, TEAL, 70)
cover = molecular_net(cover, n=52, seed=11, alpha=40)
cover = dna_helix(cover, int(W * 0.85), 60, H - 60, amp=80, alpha=110)
cover.save("cover.png", quality=92)

# ---- Fondo CONTENIDO: banda lateral teal izquierda + cuerpo blanco ----
band_w = int(W * 0.30)
b2 = molecular_net(vgrad(TEAL_DARK, TEAL_MID), n=40, seed=5, alpha=42).crop((0, 0, band_w, H))
final = Image.new("RGB", (W, H), (255, 255, 255))
final.paste(b2, (0, 0))
final = dna_helix(final, int(band_w * 0.5), 40, H - 40, amp=55, alpha=90)
final.save("content.png", quality=92)

# ---- Fondo SECCIÓN: full teal limpio para divisores ----
sec = vgrad(TEAL_DARK, TEAL_MID)
sec = diag_glow(sec, int(W * 0.5), int(H * 0.5), 600, TEAL, 55)
sec = molecular_net(sec, n=44, seed=3, alpha=34)
sec.save("section.png", quality=92)

print("OK: cover.png, content.png, section.png")
