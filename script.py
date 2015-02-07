import ystockquote
import csv

with open('symbols.csv', 'rb') as file:
    reader = csv.reader(file)
    for row in reader:
        print row
