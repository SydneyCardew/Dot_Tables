import os
import argparse
from csv_functions import csv_read
from table_functions import simple_table
from table_functions import advanced_table


def main():

    # CLI argument parser
    parser = argparse.ArgumentParser(prog="Dot Tables")
    parser.add_argument("-a", "--advanced", action='store_true', help="output advanced style table")
    parser.add_argument("-hd", "--header", action='store_true', help="include header cells")
    parser.add_argument("source", help="The filename of the source CSV file", nargs='?', type=str)
    args = parser.parse_args()

    mode = 'advanced' if args.advanced else 'simple'

    table_arr = csv_read(args.source)
    table_str = advanced_table(table_arr, args.header)
    with open('output.txt', "w+") as write_file:
        write_file.write(table_str)


if __name__ == "__main__":
    main()
