__author__ = 'Suman'

import re
import Tkinter
import tkFileDialog
import csv

class CarEvaluation:
    """Class that represents the data from the cars.data.csv file"""

    def __init__(self, row):
        dictGeneralOrdering = {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4}
        dictDoors = {'2': 2, '3': 3, '4': 4, '5more': 5}
        dictSeats = {'2': 2, '4': 4, 'more': 5}
        dictCargo = {'small': 1, 'med': 2, 'big': 3}

        if len(row) < 6:
            pass

        self.origRow = row
        self.price = row[0]
        self.maintenance =row[1]
        self.doors = row[2]
        self.seats = row[3]
        self.cargo = row[4]
        self.safety = row[5]

        if len(row) > 6:
            self.condition = row[6]

        try:
            self.priceRank = dictGeneralOrdering[self.price]
            self.maintenanceRank = dictGeneralOrdering[self.maintenance]
            self.doorsCnt = dictDoors[self.doors]
            self.seatsCnt = dictSeats[self.seats]
            self.cargoRank = dictCargo[self.cargo]
            self.safetyRank = dictGeneralOrdering[self.safety]
        except:
            print 'The line %s, %s, %s, %s, %s, %s, %s contains errors ' \
                  'setting the ranks to none.' % (self.price, self.maintenance, self.doors, self.seats, self.cargo, self.safety, self.condition)
            self.priceRank = None
            self.maintenanceRank = None
            self.doorsCnt = None
            self.seatsCnt = None
            self.cargoRank = None
            self.safetyRank = None
            pass

    def toString(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(
                            self.price, self.maintenance,
                            self.doors, self.seats,
                            self.cargo, self.safety,
                            self.condition)

    def __repr__(self):
        return repr(self.toString())


def printRows(header, items):
    print("===============================================")
    print(header)
    print("===============================================")
    for item in items:
        print(item)

def selectCars(carEvals, regexp, sortLambda, sortReverse, title):
    result = list()
    for car in carEvals:
        matchedRec = re.search(regexp, car.toString())
        if matchedRec != None:
            result.append(car)

    result.sort(key=sortLambda, reverse=sortReverse)
    printRows(title, result)

    # start of the main of the program.
if __name__ == "__main__":

        root=Tkinter.Tk()
        root.withdraw()
        dataFile = tkFileDialog.askopenfilename(parent=root)

        # Open a file stream
        strmCarData = open(dataFile)

        # Wrap in a CSV data reader
        csvReader = csv.reader(strmCarData)

        # Loop to read in the data rows
        carEvals = list()
        for row in csvReader:
            try:
                carEvals.append(CarEvaluation(row))
            except Exception, ex:
                print ("Exception on line {0}: {1} Skipped the row !".format(csvReader.line_num, ex))


        # Close the file stream
        strmCarData.close()

        # 2a. Print to the console the top 10 rows of the data sorted by 'safety' in descending order
        carEvals.sort(key=lambda CarEvaluation : CarEvaluation.safetyRank, reverse=True )
        printRows("Top 10 Safety Rating", carEvals[0:10])

        # 2b Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order
        carEvals.sort(key=lambda CarEvaluation : CarEvaluation.maintenanceRank, reverse=False )
        printRows("Top 15 Lowest Maintenance", carEvals[0:15])

        # 2c Print to the console all rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order
        selectCars(carEvals, "^(vhigh|high)?,(vhigh|high)?,[\d]?,[\d]?,([a-z]+)?,(vhigh|high)?,([a-z]*)$",
                    lambda CarEvaluation : CarEvaluation.doorsCnt, False,
                    "Cars w/ High or Very High for price, Maintenance and Safety, sorted by Doors Asc")

        # 2d Save to a file all rows that have price = vhigh, Maint = med, Doors = 4, Seats >= 4.
        root=Tkinter.Tk()
        root.withdraw()
        outputFile = tkFileDialog.asksaveasfilename(parent=root)

        # Open a stream to the output file
        opstream = open(outputFile, "wb+")
        csvwrtier = csv.writer(opstream)

        # Loop to write relevant rows to the file.
        for car in carEvals:
            # Only if the criteria matches
            if car.price == "vhigh" and car.maintenance == "med" and car.doorsCnt == 4 and car.seatsCnt >= 4:
                # Save the row to the output file.
                csvwrtier.writerow(car.origRow)

        # Close the file stream
        opstream.close()