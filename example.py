import argparse
import image_printer

DEFAULT_SCALE_FACTOR = 0.05
DEFAULT_RATIO_FACTOR = 2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example script demonstrating image_printer')
    parser.add_argument("--path")
    parser.add_argument("--scale")
    parser.add_argument("--ratio")

    args = parser.parse_args()

    path = args.path

    scale = DEFAULT_SCALE_FACTOR
    try:
        scale = float(args.scale)
    except TypeError:
        pass

    ratio = DEFAULT_RATIO_FACTOR
    try:
        ratio = float(args.ratio)
    except TypeError:
        pass

    image_printer.print_image(path, x_scale=scale, y_x_ratio=ratio)
