# inspired by
# https://github.com/retifrav/python-scripts/blob/master/generate-iconset/generate-iconset.py

import os
import shutil
import subprocess
from pathlib import Path


class IconParameters:
    width = 0
    scale = 1

    def __init__(self, width, scale):
        self.width = width
        self.scale = scale

    def getIconName(self):
        if self.scale != 1:
            return f"icon_{self.width}x{self.width}.png"
        else:
            return f"icon_{self.width//2}x{self.width//2}@2x.png"


# https://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/app-icon#app-icon-sizes
ListOfIconParameters = [
    IconParameters(16, 1),
    IconParameters(16, 2),
    IconParameters(32, 1),
    IconParameters(32, 2),
    IconParameters(64, 1),
    IconParameters(64, 2),
    IconParameters(128, 1),
    IconParameters(128, 2),
    IconParameters(256, 1),
    IconParameters(256, 2),
    IconParameters(512, 1),
    IconParameters(512, 2),
    IconParameters(1024, 1),
    IconParameters(1024, 2),
]


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="""
        Convert pngs to macos icns iconsets
        """
    )

    parser.add_argument(
        "--png_dir", metavar="\b", help="Dir with pngs to be converted",
    )

    parser.add_argument(
        "--out_dir",
        metavar="\b",
        default="./icns",
        help="Dir where mac icons will be saved. Default=./icns",
    )

    args = parser.parse_args()
    png_dir = Path(args.png_dir)
    out_dir = Path(args.out_dir)

    pngs = [f for f in png_dir.glob("*.png")]

    for png in pngs:

        fname = png.stem
        iconset_dir = Path(f"{out_dir}/{fname}.iconset")
        iconset_dir.mkdir(parents=True, exist_ok=True)

        # generate iconset
        for ip in ListOfIconParameters:
            subprocess.call(
                [
                    "sips",
                    "-z",
                    str(ip.width),
                    str(ip.width),
                    png,
                    "--out",
                    os.path.join(iconset_dir, ip.getIconName()),
                ]
            )

        # convert iconset to icns file
        subprocess.call(
            [
                "iconutil",
                "-c",
                "icns",
                iconset_dir,
                "-o",
                os.path.join(out_dir, f"{fname}.icns"),
            ]
        )

        shutil.rmtree(iconset_dir)
