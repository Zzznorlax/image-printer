import argparse
from typing import Optional, Union
import image_printer

DEFAULT_SCALE_FACTOR = 0.05
DEFAULT_RATIO_FACTOR = 2


def _str_to_bool(raw: Union[str, bool], default: Optional[bool] = None) -> bool:

    if isinstance(raw, bool):
        return raw

    if raw.lower() in ('yes', 'true', 't', 'y', '1'):
        return True

    elif raw.lower() in ('no', 'false', 'f', 'n', '0'):
        return False

    if isinstance(default, bool):
        return default

    raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example script demonstrating image_printer')
    parser.add_argument("--path")
    parser.add_argument("--scale")
    parser.add_argument("--ratio")
    parser.add_argument("--reverse")

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

    reverse = _str_to_bool(args.reverse, default=True)

    image_printer.print_image(path, x_scale=scale, y_x_ratio=ratio, reverse_symbol=reverse)
