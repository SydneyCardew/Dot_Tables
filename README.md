# Dot Table
### Version 0.2

---

A simple command-line python utility for building 
tables in the wikidot markup syntax from csv files.

Dot Table accepts the following arguments:

```dot_table.py [target] [--advanced] [--header] [--noheader] [--clip] [--help] [--version]```

* `target` is the filename of the target csv, pathed from the Dot Table root directory.
* `--advanced` or `-a` outputs a table in wikidot's 'advanced' format.
* `--header` or `-hd` over-rides the configured header setting, making sure 
the table is generated *with* header cells.
* `--noheader` or `-nd` over-rides the configured header setting, making sure the table 
is generated *without* header cells.
* `--clip` or `-c` dumps the output directly to the clipboard.
* `--help` or `-h` displays the command line help.
* `--version` or `-v` displays the version.

## Simple Operation

To use Dot Table, direct it to a target csv file:

`\> py dot_table.py test.csv`

Dot Tables will then generate a txt file in the `Output` folder, the contents of
which can be copy-pasted straight into wikidot. For more convenient usage, the `-c`
flag will cause the output to be copied directly to the clipboard.



