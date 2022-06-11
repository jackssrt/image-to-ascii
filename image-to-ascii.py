# Image to ASCII Art
# Created on 7 Jul 2015
# Forked on 11 Jun 2022
# Author: jsimb
# Forked by: jackssrt
#
# Writes a .txt file containing ascii art corresponding to an arbitrary image.
# Tested with python3.

import os
import sys
from pathlib import Path
from typing import List

from PIL import Image


def select_palette() -> List[str]:
    while True:
        palettes = [
            " -.':rLIVRQ",
            " -.':rLIVXRMWQ@",
            " .,~:;irsXA253hMHGS#9B&@",
            " ░▒▓█",
        ]
        for i, p in enumerate(palettes):
            print(i, p)
        i = int(input(f"Which palette do you want? "))
        if i < 0 or i >= len(palettes):
            print(f"Please enter a number between 0 and {len(palettes)-1}")
        else:
            return list(palettes[i])


def image_to_ascii(
    image_file: str, max_height: int, char_ratio: float, palette: List[str]
) -> str:
    if os.path.exists(f"in/{image_file}"):
        img = Image.open(f"in/{image_file}")
    else:
        img = Image.open(image_file)
    img = img.convert("L")  # convert to grayscale

    (x, y) = img.size
    newsize = (
        int(x / y * max_height * char_ratio),
        max_height,
    )  # width is r*height, image aspect-ratio is kept
    img = img.resize(newsize, Image.Resampling.LANCZOS)  # type:ignore

    result = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            lum = 255 - img.getpixel((x, y))
            result += palette[(lum // (255 // (len(palette) - 1)))]
        result += "\n"
    return result


def main():
    if len(sys.argv) != 4:
        print(
            "Usage: ./image-to-ascii.py <image_file> <max_height> <character_width_to_height_ratio>"
        )
        sys.exit()
    f = sys.argv[1]
    h = int(sys.argv[2])
    r = float(sys.argv[3])
    palette = select_palette()
    ascii = image_to_ascii(f, h, r, palette)
    outfile = f"out/{Path(f).stem}.txt"
    with open(outfile, "w", encoding="utf-8") as f2:
        f2.write(ascii)
    print(f"Done! Wrote to {outfile}")


if __name__ == "__main__":
    main()
