import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def print_ascii_art():
    ascii = """
              _
          _n_|_|_,_
         |===.-.===|
         |  ((_))  |
         '==='-'==='
    +-------------------+
    |    EXIF-VIEWER    |
    +-------------------+
    | Made By Antarctic |
    +-------------------+
    """

def get_exif_data(image_path, output_tags=None):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if exif_data is not None:
            if output_tags:
                filtered_data = {TAGS.get(tag, tag): value for tag, value in exif_data.items() if TAGS.get(tag, tag) in output_tags}
            else:
                filtered_data = exif_data
                
            return filtered_data
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_to_txt(data, output_file):
    with open(output_file, 'w') as txt_file:
        txt_file.write(f"[{data['Path']}]\n")
        txt_file.write("+------+-------------+\n")
        for key, value in data.items():
            if key != 'Path':
                txt_file.write(f"| {key:<5} | {value:<15} |\n")
        txt_file.write("+------+-------------+\n")

def main():
    parser = argparse.ArgumentParser(description="Extract EXIF data from an image")
    parser.add_argument("-r", "--image_path", type=str, required=True, help="Path to the image")
    parser.add_argument("-o", "--output_tags", nargs='+', type=str, help="List of tags to be included in the output")
    
    args = parser.parse_args()
    exif_data = get_exif_data(args.image_path, args.output_tags)
    
    if exif_data:
        exif_data['Path'] = args.image_path
        output_file = f"{args.image_path.split('.')[0]}.txt"
        save_to_txt(exif_data, output_file)
        print(f"EXIF data saved to {output_file}")
    else:
        print("No EXIF data found in the image.")

if __name__ == "__main__":
    print_ascii_art()
    main()
