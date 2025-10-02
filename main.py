#!/usr/bin/env python3
"""
Aesthetic Filter Generator
Creates 10 different aesthetic variations from a single image
All images are saved in high quality to 'image_folder'
"""

from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import sys

def create_aesthetic_variations(input_image_path, output_folder='image_folder'):
    """
    Creates 10 different aesthetic variations from a single image
    and saves them in high quality to the specified folder.

    Parameters:
    - input_image_path: Path to the input image
    - output_folder: Folder to save the filtered images (default: 'image_folder')
    """

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"✓ Created folder: {output_folder}")

    # Load the original image
    try:
        img = Image.open(input_image_path)
        print(f"✓ Loaded image: {input_image_path}")
        print(f"  Image size: {img.size}")
        print(f"  Image mode: {img.mode}")
    except Exception as e:
        print(f"✗ Error loading image: {e}")
        return None

    # Convert to RGB if necessary (for consistency)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Get the base filename without extension
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]

    # Dictionary to store all variations
    variations = {}

    # 1. VIBRANT (Clarendon-style): Enhanced saturation and contrast
    print("\n[1/10] Creating Vibrant filter...")
    vibrant = img.copy()
    vibrant = ImageEnhance.Color(vibrant).enhance(1.4)
    vibrant = ImageEnhance.Contrast(vibrant).enhance(1.2)
    vibrant = ImageEnhance.Brightness(vibrant).enhance(1.05)
    variations['01_vibrant'] = vibrant

    # 2. VINTAGE (Warm sepia tone with reduced saturation)
    print("[2/10] Creating Vintage filter...")
    vintage = img.copy()
    vintage = ImageEnhance.Color(vintage).enhance(0.6)
    vintage = ImageEnhance.Contrast(vintage).enhance(0.9)
    sepia_matrix = (
        0.393, 0.769, 0.189, 0,
        0.349, 0.686, 0.168, 0,
        0.272, 0.534, 0.131, 0
    )
    vintage = vintage.convert('RGB', sepia_matrix)
    variations['02_vintage'] = vintage

    # 3. BLACK & WHITE (High contrast monochrome)
    print("[3/10] Creating Black & White filter...")
    bw = img.copy()
    bw = ImageOps.grayscale(bw).convert('RGB')
    bw = ImageEnhance.Contrast(bw).enhance(1.3)
    variations['03_black_white'] = bw

    # 4. WARM GLOW (Enhanced warm tones - Valencia style)
    print("[4/10] Creating Warm Glow filter...")
    warm = img.copy()
    width, height = warm.size
    warm_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = warm.getpixel((x, y))
            r = min(255, int(r * 1.1 + 10))
            g = min(255, int(g * 1.05 + 5))
            b = min(255, int(b * 0.9))
            warm_data.append((r, g, b))
    warm.putdata(warm_data)
    warm = ImageEnhance.Brightness(warm).enhance(1.05)
    variations['04_warm_glow'] = warm

    # 5. COOL BLUE (Blue tint - Walden style)
    print("[5/10] Creating Cool Blue filter...")
    cool = img.copy()
    width, height = cool.size
    cool_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = cool.getpixel((x, y))
            r = min(255, int(r * 0.9))
            g = min(255, int(g * 0.95))
            b = min(255, int(b * 1.15 + 10))
            cool_data.append((r, g, b))
    cool.putdata(cool_data)
    variations['05_cool_blue'] = cool

    # 6. DRAMATIC (Lo-Fi style: High contrast, deep shadows)
    print("[6/10] Creating Dramatic filter...")
    dramatic = img.copy()
    dramatic = ImageEnhance.Contrast(dramatic).enhance(1.5)
    dramatic = ImageEnhance.Color(dramatic).enhance(1.3)
    dramatic = ImageEnhance.Brightness(dramatic).enhance(0.95)
    variations['06_dramatic'] = dramatic

    # 7. SOFT PASTEL (Desaturated, bright, dreamy)
    print("[7/10] Creating Soft Pastel filter...")
    soft = img.copy()
    soft = ImageEnhance.Color(soft).enhance(0.7)
    soft = ImageEnhance.Contrast(soft).enhance(0.85)
    soft = ImageEnhance.Brightness(soft).enhance(1.1)
    variations['07_soft_pastel'] = soft

    # 8. SHARP & CRISP (HDR-like effect)
    print("[8/10] Creating Sharp & Crisp filter...")
    sharp = img.copy()
    sharp = sharp.filter(ImageFilter.SHARPEN)
    sharp = ImageEnhance.Sharpness(sharp).enhance(2.0)
    sharp = ImageEnhance.Contrast(sharp).enhance(1.15)
    variations['08_sharp_crisp'] = sharp

    # 9. MUTED AESTHETIC (Modern Instagram aesthetic)
    print("[9/10] Creating Muted Aesthetic filter...")
    muted = img.copy()
    muted = ImageEnhance.Color(muted).enhance(0.75)
    muted = ImageEnhance.Contrast(muted).enhance(0.95)
    width, height = muted.size
    muted_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = muted.getpixel((x, y))
            r = min(255, int(r * 0.95 + 15))
            g = min(255, int(g * 0.95 + 15))
            b = min(255, int(b * 0.95 + 15))
            muted_data.append((r, g, b))
    muted.putdata(muted_data)
    variations['09_muted_aesthetic'] = muted

    # 10. SUNSET VIBES (Golden hour effect)
    print("[10/10] Creating Sunset Vibes filter...")
    sunset = img.copy()
    width, height = sunset.size
    sunset_data = []
    for y in range(height):
        for x in range(width):
            r, g, b = sunset.getpixel((x, y))
            r = min(255, int(r * 1.15 + 15))
            g = min(255, int(g * 1.05 + 8))
            b = min(255, int(b * 0.85))
            sunset_data.append((r, g, b))
    sunset.putdata(sunset_data)
    sunset = ImageEnhance.Brightness(sunset).enhance(1.05)
    variations['10_sunset_vibes'] = sunset

    # Save all variations in high quality
    print("\n" + "="*50)
    print("SAVING IMAGES IN HIGH QUALITY...")
    print("="*50)

    saved_count = 0
    for filter_name, filtered_img in variations.items():
        output_path = os.path.join(output_folder, f"{base_name}_{filter_name}.jpg")
        try:
            filtered_img.save(output_path, 'JPEG', quality=95, optimize=True)
            print(f"✓ Saved: {output_path}")
            saved_count += 1
        except Exception as e:
            print(f"✗ Error saving {filter_name}: {e}")

    print("\n" + "="*50)
    print(f"COMPLETE! {saved_count}/10 variations saved successfully!")
    print(f"Location: {os.path.abspath(output_folder)}/")
    print("="*50)

    return variations

def main():
    """Main function for command-line usage"""
    print("="*50)
    print("AESTHETIC FILTER GENERATOR")
    print("Creates 10 different variations from one image")
    print("="*50)

    if len(sys.argv) < 2:
        print("\nUSAGE:")
        print("  python aesthetic_filters.py <image_path> [output_folder]")
        print("\nEXAMPLES:")
        print("  python aesthetic_filters.py photo.jpg")
        print("  python aesthetic_filters.py vacation.png my_filters")
        print("\nFILTERS INCLUDED:")
        filters = [
            "1. Vibrant - Enhanced colors and contrast",
            "2. Vintage - Warm sepia with retro feel",
            "3. Black & White - High contrast monochrome",
            "4. Warm Glow - Golden warm tones",
            "5. Cool Blue - Blue tinted atmosphere",
            "6. Dramatic - Deep contrast and saturation",
            "7. Soft Pastel - Dreamy desaturated look",
            "8. Sharp & Crisp - HDR-style clarity",
            "9. Muted Aesthetic - Modern Instagram style",
            "10. Sunset Vibes - Golden hour effect"
        ]
        for f in filters:
            print(f"  {f}")
        return

    image_path = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else 'image_folder'

    if not os.path.exists(image_path):
        print(f"\n✗ Error: Image file '{image_path}' not found!")
        return

    create_aesthetic_variations(image_path, output_folder)

if __name__ == "__main__":
    main()
