import csv
"""FileIO module is to read/write data from/to a CSV or other flat files.

The methods are
"""


def controlled_execution(self):

    try:
        print(f'controlled execution')
        pass
    finally:
        print(f'finally')


def read_file(filename):
    print(filename)


"""Extract data from CSV file and print to terminal.

Here i learn to use -
1) "with" python (for a good read - http://effbot.org/zone/python-with-statement.htm)
2) use the csv module
"""
with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines')
