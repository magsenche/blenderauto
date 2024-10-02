import argparse
import pathlib


def convert(folder, prefix="", prefix_filter="bw"):
    import cv2

    for file in folder.rglob("*"):
        if file.name.endswith(".png") and not file.name.startswith(prefix_filter):
            img = cv2.imread(str(file))
            _, bnw_img = cv2.threshold(255 - img, 127, 255, cv2.THRESH_BINARY)
            cv2.imwrite(str(file.parent / f"{prefix}{file.name}"), bnw_img)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str)
    parser.add_argument("-p", "--prefix", type=str, default="")
    parser.add_argument("-s", "--prefix_filter", type=str, default="bw")
    args = parser.parse_args()
    convert(pathlib.Path(args.folder), args.prefix, args.prefix_filter)
