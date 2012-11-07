#! /usr/bin/env python
"""
Create Models Skeleton from XLS

Usage:
  skel <filename> <cols>
  skel -h | --help
  skel --version

Options:
  -h --help       Show this screen.
  --version       Show version.
  <cols>          Eg. A2:AK2

"""
from openpyxl import load_workbook
from docopt import docopt
from openpyxl.cell import get_column_letter


def print_cols(filename, cols):
    """
    Parse spreadsheet file and extract column headers
    """
    wb = load_workbook(filename)
    sheet = wb.get_sheet_by_name(wb.get_sheet_names()[0])
    dimensions = sheet.calculate_dimension()
    data = sheet.range(cols)

    high_row = sheet.get_highest_row()
    for cell in data[0]:
        max_len = 0
        for row in sheet.range(cell.address + ":" + cell.address[:-1] +
                str(high_row)):
            try:
                if row[0].value and len(row[0].value) > max_len:
                    max_len = len(row[0].value)
            except TypeError:
                pass

        new_name = cell.value.replace(' ', '_').replace('/', '_').replace('?',
                '').replace('.', '').replace('&', '').lower()

        print "    %s = models.CharField(max_length=%d, blank=True)" % (new_name, max_len)


if __name__ == '__main__':
    arguments = docopt(__doc__, version="Models Skeleton 0.1")

    if '<filename>' in arguments:
        print_cols(arguments['<filename>'], arguments['<cols>'])

