import os
import argparse
from PIL import Image, ImageFilter

def upscale_image(input_path, output_path, max_dimension=1500):
    try:
        with Image.open(input_path) as img:
            # Calculate new size
            width, height = img.size
            if max(width, height) >= max_dimension:
                print(f"Skipping {input_path}: already larger or equal to {max_dimension}px")
                return

            ratio = max_dimension / max(width, height)
            new_width = int(width * ratio)
            new_height = int(height * ratio)

            # High-quality resampling
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

            # Apply Unsharp Mask to enhance details
            # Radius 1.5, Percent 100, Threshold 3 are good starting points for upscaling
            sharpened_img = resized_img.filter(ImageFilter.UnsharpMask(radius=1.5, percent=100, threshold=3))

            # Save
            sharpened_img.save(output_path, quality=95, subsampling=0)
            print(f"Upscaled {os.path.basename(input_path)} to {new_width}x{new_height}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Upscale images in a directory.")
    parser.add_argument("--input_dir", default="inbox/photos", help="Input directory")
    parser.add_argument("--output_dir", default="inbox/photos/upscaled", help="Output directory")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of images to process (0 for all)")
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    processed_count = 0
    files = sorted([f for f in os.listdir(args.input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
    
    for filename in files:
        if args.limit > 0 and processed_count >= args.limit:
            break
            
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename)
        
        upscale_image(input_path, output_path)
        processed_count += 1

if __name__ == "__main__":
    main()
