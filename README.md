# Aesthetic Filter Generator 📸

Creates 10 different aesthetic variations from a single image and saves them in high quality.

## Installation

Install required library:
```bash
pip install Pillow
```

## Quick Start

### Method 1: Command Line
```bash
python aesthetic_filters.py your_photo.jpg
```

### Method 2: Python Script
```python
from aesthetic_filters import create_aesthetic_variations

# Generate all 10 filters
create_aesthetic_variations('your_photo.jpg')

# Custom output folder
create_aesthetic_variations('photo.jpg', 'my_filters')
```

## Filter Types

The program creates these 10 aesthetic variations:

1. **Vibrant** - Enhanced colors and contrast (Instagram Clarendon style)
2. **Vintage** - Warm sepia tone with retro feel
3. **Black & White** - High contrast monochrome
4. **Warm Glow** - Golden warm tones (Valencia style)
5. **Cool Blue** - Blue tinted atmosphere (Walden style)
6. **Dramatic** - Deep contrast and saturation (Lo-Fi style)
7. **Soft Pastel** - Dreamy desaturated look
8. **Sharp & Crisp** - HDR-style clarity
9. **Muted Aesthetic** - Modern Instagram aesthetic
10. **Sunset Vibes** - Golden hour effect

## Features

✓ **High Quality Output** - 95% JPEG quality for social media  
✓ **Minimal Modifications** - Subtle aesthetic changes  
✓ **Automatic Organization** - Creates output folder automatically  
✓ **Multiple Formats** - Supports JPG, PNG, and other formats  
✓ **Fast Processing** - Generates all 10 filters in seconds  

## Output

All filtered images are saved with descriptive names:
```
image_folder/
├── your_photo_01_vibrant.jpg
├── your_photo_02_vintage.jpg
├── your_photo_03_black_white.jpg
├── your_photo_04_warm_glow.jpg
├── your_photo_05_cool_blue.jpg
├── your_photo_06_dramatic.jpg
├── your_photo_07_soft_pastel.jpg
├── your_photo_08_sharp_crisp.jpg
├── your_photo_09_muted_aesthetic.jpg
└── your_photo_10_sunset_vibes.jpg
```

## Examples

### Example 1: Process a single image
```python
create_aesthetic_variations('vacation_photo.jpg')
```

### Example 2: Custom output folder
```python
create_aesthetic_variations('selfie.jpg', 'instagram_posts')
```

### Example 3: Batch processing
```python
import os
from aesthetic_filters import create_aesthetic_variations

for image in os.listdir('photos'):
    if image.endswith(('.jpg', '.png')):
        create_aesthetic_variations(f'photos/{image}', 'filtered_photos')
```

## Tips for Best Results

- Use high-resolution images for best quality
- Works best with well-lit photos
- Different filters suit different photo types:
  - **Portraits**: Warm Glow, Soft Pastel, Vintage
  - **Landscapes**: Vibrant, Dramatic, Sunset Vibes
  - **Urban**: Black & White, Cool Blue, Sharp & Crisp
  - **Food**: Warm Glow, Vibrant, Muted Aesthetic

## Requirements

- Python 3.6+
- Pillow (PIL)

## Troubleshooting

**Error: "No module named 'PIL'"**
```bash
pip install Pillow
```

**Error: "Image file not found"**
- Check the file path is correct
- Use absolute path or ensure file is in same directory

## License

Free to use for personal and commercial projects.
