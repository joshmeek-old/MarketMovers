import ystockquote
import csv

smallestValue = 0;

def smallest( symbol, value ):
    global smallestValue
    if value < smallestValue:
        smallestValue = value
        print symbol + " " + str(value)

while True:
    with open('symbols.csv', 'rU') as file:
        reader = csv.reader(file)
        for row in reader:
            if ystockquote.get_change(row[0]) != 'N/A':
                smallest(row[0], float(ystockquote.get_change(row[0]).strip('+')))
