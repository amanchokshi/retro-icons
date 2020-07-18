import argparse
import subprocess
from pathlib import Path

parser = argparse.ArgumentParser(
    description="""
    Convert svg vectors to pngs using inkscape.
    """
)

parser.add_argument(
    "--svg_dir", metavar="\b", help="Dir with svgs to be converted",
)

parser.add_argument(
    "--out_dir",
    metavar="\b",
    default="./icns",
    help="Dir where mac icons will be saved. Default=./icns",
)

args = parser.parse_args()
png_dir = Path(args.svg_dir)
out_dir = Path(args.out_dir)

svgs = [f for f in png_dir.glob("*.svg")]
out_dir.mkdir(parents=True, exist_ok=True)

for svg in svgs:

    fname = svg.stem

    # convert iconset to icns file
    subprocess.call(
        [
            "inkscape",
            "-h",
            "1024",
            f"{svg}",
            "--export-filename",
            f"{out_dir}/{fname}.png",
        ]
    )
