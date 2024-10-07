import argparse
from csv_functions import csv_read
from table_functions import simple_table
from table_functions import advanced_table
from config_class import Configuration
from write_functions import write_txt
from write_functions import write_clipboard


def main():

    config = Configuration()

    # CLI argument parser
    parser = argparse.ArgumentParser(prog="Dot Tables")
    parser.add_argument("-a", "--advanced", action='store_true', help="output advanced style table")
    parser.add_argument("-hd", "--header", action='store_true', help="over-ride settings to include header")
    parser.add_argument("-nd", "--noheader", action='store_true', help="over-ride settings to not include header")
    parser.add_argument("-c", "--clip", action='store_true', help="dump output text directly to clipboard")
    parser.add_argument("-v", "--version", action='version', version=config.version)
    parser.add_argument("source", help="The filename of the source CSV file", nargs='?', type=str)
    args = parser.parse_args()

    config.header_override(args)
    config.store_target(args)

    advanced = True if args.advanced else False

    table_arr = csv_read(args.source)
    if advanced:
        table_str = advanced_table(table_arr, config)
    else:
        table_str = simple_table(table_arr, config)
    write_txt(table_str, config)
    if args.clip:
        write_clipboard(table_str)
        print("output copied to clipboard")


if __name__ == "__main__":
    main()
