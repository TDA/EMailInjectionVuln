#!/usr/bin/env python
import os
import sys
import csv

__author__ = 'saipc'

def xls2latex(filename):
    with open(filename, 'r') as file:
        contents = csv.reader(file)
        new_rows = []
        for row in contents:
            new_rows.append(' & '.join(row))
        latex_table = ' \\\\\n\hline\n'.join(new_rows)
        # add padding
        latex_table = '\\\\\n\hline\n' + latex_table + ' \\\\\n\hline\n'
        latex_table = latex_table.replace("%", "\%")
        print(latex_table)

if __name__ == '__main__':
    filename = None
    if (len(sys.argv) < 2):
        print("Usage: python xls2latex filename")
        print("Exiting")
        filename = r"~/Documents/schand31_thesis/Results/pipeline.csv"
    filename = filename or sys.argv[1]
    print(filename)
    xls2latex(filename)
