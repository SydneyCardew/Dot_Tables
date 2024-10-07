def simple_table(table_arr, header):
    table_str = ""
    for index, row in enumerate(table_arr):
        if index == 0 and header:
            table_str += (f"||~ {'||~ '.join(map(str, row))}||\n")
        else:
            table_str += (f"||{'||'.join(map(str, row))}||\n")
    return table_str


def advanced_table(table_arr, header):
    table_str = '[[table  style="border-collapse:collapse;"]]\n'
    for index, row in enumerate(table_arr):
        row_str = "[[row]]\n"
        for cell in row:
            row_str += f'[[{"hcell" if header and index == 0 else "cell"} style="border: 1px solid silver;"]]\n' \
                       f'{cell}\n' \
                       f'[[/{"hcell" if header and index == 0 else "cell"}]]\n'
        row_str += "[[/row]]\n"
        table_str += row_str
    table_str += "[[/table]]"
    return table_str

