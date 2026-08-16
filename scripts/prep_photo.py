"""
Prepare a portrait photo for clean ASCII conversion:
  1. remove/mask the background (rembg if available, or threshold/alpha channel)
  2. boost local contrast so face features gain highlights and shadows
  3. composite onto pure white so background reads as blank

Output: source-prepped.png (grayscale), consumed by make_ascii_svg.py.
Run once whenever the source photo changes; the ascii SVG itself is static.

    python scripts/prep_photo.py [input.jpg] [output.png]
"""
import os
import sys
import numpy as np
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

img = Image.open(INP)

# Try rembg if available, otherwise process directly
try:
    from rembg import remove
    cut = remove(img.convert("RGBA"))
    rgb = np.array(cut.convert("RGB"))
    alpha = np.array(cut.split()[-1])
except Exception:
    img_rgba = img.convert("RGBA")
    rgb = np.array(img_rgba.convert("RGB"))
    alpha = np.array(img_rgba.split()[-1])

# Convert RGB to Grayscale
try:
    import cv2
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.6, tileGridSize=(8, 8))
    gray = clahe.apply(gray)
    gray = cv2.convertScaleAbs(gray, alpha=1.05, beta=18)
    mask = (alpha.astype(np.float32) / 255.0)
    mask = cv2.GaussianBlur(mask, (0, 0), 1.0)
    out = gray.astype(np.float32) * mask + 255.0 * (1.0 - mask)
    out = np.clip(out, 0, 255).astype(np.uint8)
except Exception:
    # Pure PIL/NumPy fallback
    pil_gray = Image.fromarray(rgb).convert("L")
    pil_gray = ImageEnhance.Contrast(pil_gray).enhance(1.4)
    pil_gray = ImageEnhance.Brightness(pil_gray).enhance(1.1)
    pil_gray = ImageOps.autocontrast(pil_gray, cutoff=2)
    gray_arr = np.array(pil_gray)
    mask = (alpha.astype(np.float32) / 255.0)
    out = gray_arr.astype(np.float32) * mask + 255.0 * (1.0 - mask)
    out = np.clip(out, 0, 255).astype(np.uint8)

Image.fromarray(out, mode="L").save(OUT)
print("wrote", OUT, out.shape)

