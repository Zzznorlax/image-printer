import argparse
import image_printer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example script demonstrating image_printer')
    parser.add_argument("--path")

    args = parser.parse_args()

    image_printer.print_image(args.path)
