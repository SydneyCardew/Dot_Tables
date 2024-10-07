import argparse
from csv_functions import csv_read
from table_functions import simple_table
from table_functions import advanced_table
from config_class import Configuration


def main():

    config = Configuration('MAIN')

    # CLI argument parser
    parser = argparse.ArgumentParser(prog="Dot Tables")
    parser.add_argument("-a", "--advanced", action='store_true', help="output advanced style table")
    parser.add_argument("-hd", "--header", action='store_true', help="include header cells")
    parser.add_argument("-v", "--version", action='version', version=config.version)
    parser.add_argument("source", help="The filename of the source CSV file", nargs='?', type=str)
    args = parser.parse_args()

    advanced = True if args.advanced else False

    table_arr = csv_read(args.source)
    if advanced:
        table_str = advanced_table(table_arr, args.header)
    else:
        table_str = simple_table(table_arr, args.header)
    with open('output.txt', "w+") as write_file:
        write_file.write(table_str)


if __name__ == "__main__":
    main()
