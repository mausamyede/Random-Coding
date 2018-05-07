import csv
import numpy
from RideScenario import RideScenario
from Utilities import parseToFloat


class AccidentPredictor:
    def csvReader(self, csvFile):
        return csv.DictReader(csvFile)

    def distanceBetween(self, dataRideScenario, currentRideScenario):
        x = numpy.array(dataRideScenario.getDataPoint())
        y = numpy.array(currentRideScenario.getDataPoint())
        return numpy.linalg.norm(x - y)

    def predictFor(self, currentRideScenario):
        all_distances = []
        with open("dftRoadSafety_Accidents_2016.csv", "rb") as fileObj:
            for row in self.csvReader(fileObj):
                dataRideScenario = self.getRideScenario(row)
                distance = self.distanceBetween(dataRideScenario, currentRideScenario)
                all_distances.append(distance)
        mindist = min(all_distances)
        print mindist
        if mindist <= 400:
            print 'High'
        elif mindist <= 700:
            print 'Medium'
        else:
            print 'Low'

    def getRideScenario(self, row):
        return RideScenario(parseToFloat(row["Longitude"]), parseToFloat(row["Latitude"]),
                            parseToFloat(row["Day_of_Week"]), parseToFloat(row["Time"].replace(':', '')),
                            parseToFloat(row["Road_Type"]), parseToFloat(row["Speed_limit"]),
                            parseToFloat(row["Light_Conditions"]),
                            parseToFloat(row["Weather_Conditions"]),
                            parseToFloat(row["Road_Surface_Conditions"]))
