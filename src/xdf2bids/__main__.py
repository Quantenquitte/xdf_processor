"""Command-line interface for xdf2bids."""
import argparse

from xdf2bids.xdf_processor import process_xdf_file, __version__

INPUT_FILE = None
OUTPUT_DIR = None

def main():
    """Main function to handle command-line arguments and process XDF files."""

    parser = argparse.ArgumentParser(description="Convert XDF files to BIDS format.")
    parser.add_argument("input_file", type=str, help="Path to the input XDF file.")
    parser.add_argument("output_dir", type=str, help="Directory to save the BIDS formatted output.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    process_xdf_file(args.input_file, args.output_dir)

if __name__ == "__main__":
    main()