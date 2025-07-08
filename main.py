import os
import argparse
from fontTools.ttLib import TTFont

def convert_font_to_woff2(input_path, output_path):
    try:
        font = TTFont(input_path)
        font.flavor = 'woff2'
        font.save(output_path)
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Convert various font formats to WOFF2.")
    parser.add_argument("input_files", nargs="+", help="One or more input font files (TTF, OTF).")
    parser.add_argument("-o", "--output_dir", default="./", help="Output directory for WOFF2 files. Defaults to current directory.")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    for input_file in args.input_files:
        if not os.path.exists(input_file):
            print(f"Error: Input file not found: {input_file}")
            continue

        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join(args.output_dir, f"{base_name}.woff2")
        convert_font_to_woff2(input_file, output_file)

if __name__ == "__main__":
    main()


