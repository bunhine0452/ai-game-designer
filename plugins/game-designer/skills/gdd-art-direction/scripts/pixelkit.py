"""Shared helpers for the pixel-art scripts (pixel_audit.py, palette_ramp.py).

- PNG read/write with the standard library only. When Pillow is installed it is used for reading
  (faster, and it adds JPEG, WebP and GIF); otherwise a pure-Python decoder reads 1/2/4/8/16-bit
  PNGs of every colour type (no interlacing).
- Images are (w, h, px) where px is an array('I') of packed RGBA values (see pack/unpack).
- OKLab colour math (Ottosson 2020): perceptual lightness steps and colour distances.
- Palette parsing: "#hex,#hex", .hex/.txt files (one colour per line), GIMP .gpl, or a PNG swatch.
"""
import math
import os
import struct
import sys
import zlib
from array import array

PNG_SIG = b"\x89PNG\r\n\x1a\n"


# ---------- packed RGBA ----------
def pack(r, g, b, a=255):
    return r | (g << 8) | (b << 16) | (a << 24)


def unpack(v):
    return v & 255, (v >> 8) & 255, (v >> 16) & 255, (v >> 24) & 255


def alpha(v):
    return (v >> 24) & 255


def hexcol(v):
    r, g, b, _ = unpack(v)
    return f"#{r:02x}{g:02x}{b:02x}"


def parse_hex(s):
    s = s.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(c * 2 for c in s)
    if len(s) != 6:
        raise ValueError(f"not a hex colour: {s!r}")
    return pack(int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))


def _from_rgba_bytes(w, h, data):
    px = array("I")
    px.frombytes(bytes(data))
    if sys.byteorder == "big":
        px.byteswap()
    assert len(px) == w * h
    return w, h, px


# ---------- PNG ----------
def read_image(path, pure=False):
    """Return (w, h, px). Uses Pillow when available unless pure=True."""
    if not pure:
        try:
            from PIL import Image
        except ImportError:
            Image = None
        if Image is not None:
            with Image.open(path) as im:
                im = im.convert("RGBA")
                return _from_rgba_bytes(im.size[0], im.size[1], im.tobytes())
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != PNG_SIG:
        kind = "JPEG" if data[:3] == b"\xff\xd8\xff" else "this format"
        raise ValueError(f"{path}: not a PNG. Reading {kind} needs Pillow (pip install pillow), "
                         "and pixel art should be saved as PNG anyway: JPEG compression smears the pixels.")
    return _decode_png(data)


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else (b if pb <= pc else c)


def _decode_png(data):
    pos, idat, plte, trns = 8, [], None, None
    w = h = bd = ct = il = 0
    while pos < len(data):
        ln, typ = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + ln]
        pos += 12 + ln
        if typ == b"IHDR":
            w, h, bd, ct, _, _, il = struct.unpack(">IIBBBBB", body)
        elif typ == b"PLTE":
            plte = body
        elif typ == b"tRNS":
            trns = body
        elif typ == b"IDAT":
            idat.append(body)
        elif typ == b"IEND":
            break
    if il:
        raise ValueError("interlaced PNG: re-save it without interlacing, or install Pillow")
    ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ct]
    bits = ch * bd
    stride, bpp = (w * bits + 7) // 8, max(1, bits // 8)
    raw = zlib.decompress(b"".join(idat))
    rows, prev, i = [], bytearray(stride), 0
    for _ in range(h):
        f, line = raw[i], bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        if f == 1:
            for x in range(bpp, stride):
                line[x] = (line[x] + line[x - bpp]) & 255
        elif f == 2:
            line = bytearray((a + b) & 255 for a, b in zip(line, prev))
        elif f == 3:
            for x in range(stride):
                line[x] = (line[x] + (((line[x - bpp] if x >= bpp else 0) + prev[x]) >> 1)) & 255
        elif f == 4:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0
                c = prev[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + _paeth(a, prev[x], c)) & 255
        rows.append(line)
        prev = line
    out = bytearray()
    key = None
    if trns and ct in (0, 2):   # colour-key transparency
        vals = struct.unpack(">" + "H" * (len(trns) // 2), trns)
        key = vals if ct == 2 else (vals[0],) * 3
    for line in rows:
        if bd == 16:
            line = line[0::2]   # keep the high bytes
        if ct == 3 or bd < 8:
            per = 8 // bd if bd < 8 else 1
            idx = []
            for byte in line:
                if bd == 8:
                    idx.append(byte)
                else:
                    idx.extend((byte >> (8 - bd * (k + 1))) & ((1 << bd) - 1) for k in range(per))
            idx = idx[:w]
            if ct == 3:
                for n in idx:
                    out += bytes(plte[n * 3:n * 3 + 3]) + bytes([trns[n] if trns and n < len(trns) else 255])
            else:   # low-bit greyscale
                scale = 255 // ((1 << bd) - 1)
                for n in idx:
                    v = n * scale
                    out += bytes([v, v, v, 0 if key and n == key[0] else 255])
            continue
        for x in range(w):
            if ct == 6:
                out += line[x * 4:x * 4 + 4]
            elif ct == 2:
                r, g, b = line[x * 3:x * 3 + 3]
                out += bytes([r, g, b, 0 if key and (r, g, b) == tuple(k >> 8 if bd == 16 else k for k in key) else 255])
            elif ct == 4:
                v, a = line[x * 2], line[x * 2 + 1]
                out += bytes([v, v, v, a])
            else:
                v = line[x]
                out += bytes([v, v, v, 0 if key and v == (key[0] >> 8 if bd == 16 else key[0]) else 255])
    return _from_rgba_bytes(w, h, out)


def write_png(path, w, h, px, scale=1):
    """Write packed RGBA pixels as an 8-bit RGBA PNG, optionally upscaled by an integer (nearest)."""
    if scale > 1:
        w, h, px = upscale(w, h, px, scale)
    a = array("I", px)
    if sys.byteorder == "big":
        a.byteswap()
    b = a.tobytes()
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        raw += b[y * w * 4:(y + 1) * w * 4]

    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)

    with open(path, "wb") as f:
        f.write(PNG_SIG + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))


def upscale(w, h, px, k):
    out = array("I")
    for y in range(h):
        row = array("I")
        for v in px[y * w:(y + 1) * w]:
            row.extend([v] * k)
        for _ in range(k):
            out.extend(row)
    return w * k, h * k, out


# ---------- colour ----------
def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c):
    c = 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
    return c * 255.0


def _cbrt(x):
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))


_LAB_CACHE = {}


def oklab(v):
    """Packed colour (alpha ignored) -> OKLab (L, a, b). L runs 0 (black) to 1 (white)."""
    key = v & 0xFFFFFF
    hit = _LAB_CACHE.get(key)
    if hit:
        return hit
    r, g, b, _ = unpack(v)
    r, g, b = _lin(r), _lin(g), _lin(b)
    l_ = _cbrt(0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b)
    m_ = _cbrt(0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b)
    s_ = _cbrt(0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b)
    lab = (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
           1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
           0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)
    if len(_LAB_CACHE) < 200000:
        _LAB_CACHE[key] = lab
    return lab


def from_oklab(L, a, b):
    """OKLab -> (packed colour, in_gamut). Out-of-gamut channels are clipped."""
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    rgb = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
           -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
           -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    ok = all(-1e-4 <= c <= 1 + 1e-4 for c in rgb)
    r, g, b = (int(round(min(255.0, max(0.0, _gam(min(1.0, max(0.0, c))))))) for c in rgb)
    return pack(r, g, b), ok


def oklch(v):
    L, a, b = oklab(v)
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def from_oklch(L, C, h):
    """OKLCh -> packed colour, reducing chroma until the colour fits sRGB."""
    for _ in range(40):
        col, ok = from_oklab(L, C * math.cos(math.radians(h)), C * math.sin(math.radians(h)))
        if ok:
            return col
        C *= 0.95
    return from_oklab(L, 0, 0)[0]


def dist(u, v):
    """Perceptual distance in OKLab (about 0.02 is a just-noticeable difference)."""
    a, b = oklab(u), oklab(v)
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


def luminance(v):
    """WCAG relative luminance."""
    r, g, b, _ = unpack(v)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(u, v):
    a, b = sorted((luminance(u), luminance(v)))
    return (b + 0.05) / (a + 0.05)


def hsv(v):
    r, g, b, _ = unpack(v)
    mx, mn = max(r, g, b), min(r, g, b)
    return (0.0 if mx == 0 else (mx - mn) / mx), mx / 255.0


def hue_delta(h1, h2):
    """Signed shortest hue difference h2 - h1 in degrees (-180..180]."""
    d = (h2 - h1) % 360
    return d - 360 if d > 180 else d


# ---------- palettes ----------
def load_palette(spec):
    """'#aabbcc,#112233', a .hex/.txt/.gpl file, or a PNG swatch -> list of packed colours (unique, in order)."""
    if os.path.exists(spec):
        if spec.lower().endswith(".png"):
            _, _, px = read_image(spec)
            cols = [v | 0xFF000000 for v in px if alpha(v) > 0]
        else:
            cols = []
            with open(spec, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith(("#", "GIMP", "Name", "Columns")) and not _is_hex(line):
                        continue
                    parts = line.split()
                    if spec.lower().endswith(".gpl") and len(parts) >= 3 and all(p.isdigit() for p in parts[:3]):
                        cols.append(pack(*(int(p) for p in parts[:3])))
                    elif _is_hex(parts[0]):
                        cols.append(parse_hex(parts[0]))
    else:
        cols = [parse_hex(s) for s in spec.replace(";", ",").replace(" ", ",").split(",") if s.strip()]
    seen, out = set(), []
    for c in cols:
        if c not in seen:
            seen.add(c)
            out.append(c)
    if not out:
        raise ValueError(f"no colours found in {spec!r}")
    return out


def _is_hex(s):
    s = s.lstrip("#")
    return len(s) in (3, 6) and all(c in "0123456789abcdefABCDEF" for c in s)


def nearest(v, palette):
    return min(palette, key=lambda p: dist(v, p))
