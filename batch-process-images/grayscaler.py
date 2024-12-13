from pathlib import Path
import argparse
import os

from PIL import Image, UnidentifiedImageError

def convert_images(input_dir, output_dir):
    for image_name in os.listdir(input_dir):
        image_path = os.path.join(input_dir, image_name)
        image_output_path = os.path.join(output_dir, image_name)
        
        try:
            image = Image.open(image_path)
            grayscale_image = image.convert("L")
            grayscale_image.save(image_output_path)
            print(f"{image_output_path} was successfuly converted to grayscale.")
        except UnidentifiedImageError as e:
            print(f"{image_name} is not an image.")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="grayscaler",
        description="A small utility to batch process images.",
        epilog="Thanks for using %(prog)s! :)",
    )

    parser.add_argument(
        "input_directory",
        type=Path,
        help="The directory containing the input images.",
    )
    parser.add_argument(
        "output_directory",
        type=Path,
        nargs="?",  # Makes it optional
        help="The directory to save the processed images.",
        default=Path('output')
    )

    # Parse the arguments
    args = parser.parse_args()

    # Access the input and output directories
    input_dir = args.input_directory
    output_dir = args.output_directory

    # Checks
    if not input_dir.is_dir():
        exit("Input directory is invalid.")
        
    if not output_dir.exists():
        os.makedirs(output_dir)
        print("Output directory was created.")
    
    convert_images(input_dir, output_dir)
