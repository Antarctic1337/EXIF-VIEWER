# EXIF Viewer

## Features

- Extracts and displays EXIF data from images.
- Easy-to-use command-line interface.
- Option to search for specific EXIF tags and generate detailed reports.

## Getting Started

1. Clone this repository: `git clone https://github.com/Antarctic1337/EXIF-VIEWER.git`
2. Navigate to the project directory: `cd EXIF-VIEWER`
3. Install dependencies: `pip install pillow`

## Usage

To extract and view EXIF data from an image:


```bash
python main.py -r path_to_your_image.jpg
```
Or

```bash
python main.py -r path_to_your_image.jpg
```

1. The script will extract the EXIF data from the image and display it in a formatted table.
2. If you want to include only specific EXIF tags in the output, you can provide a list of tag names using the -o option:

```bash
python exif_viewer.py -r path_to_your_image.jpg -o {Tag1}
```

1.The script will save the extracted EXIF data to a text file named after the image, e.g., image_name.txt.


# Disclaimer

The creator of this script assumes no liability for any damages that may occur from using this script. The usage of the script is at your own risk. Please ensure that you use the script responsibly and in accordance with applicable laws.

