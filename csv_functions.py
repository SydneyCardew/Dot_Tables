import csv


def csv_read(source):
    table_arr = []
    source_path = "./" + source
    try:
        with open(source_path, newline='') as csvfile:
            csvobject = csv.reader(csvfile)
            for row in csvobject:
                table_arr.append([' ' if x == '' else x for x in row])
    except FileExistsError:
        print('Fatal Error: Source file does not exist.')
    return table_arr


