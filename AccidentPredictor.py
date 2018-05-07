import csv
import numpy
from RideScenario import RideScenario


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
        if mindist <= 179:
            print 'High'
        elif mindist <= 180:
            print 'Medium'
        else:
            print 'Low'

    def parseToFloat(self, str):
        try:
            return float(str)
        except ValueError:
            return 0

    def getRideScenario(self, row):
        return RideScenario(self.parseToFloat(row["Longitude"]), self.parseToFloat(row["Latitude"]),
                            self.parseToFloat(row["Day_of_Week"]),
                            self.parseToFloat(row["Road_Type"]), self.parseToFloat(row["Speed_limit"]),
                            self.parseToFloat(row["Light_Conditions"]),
                            self.parseToFloat(row["Weather_Conditions"]),
                            self.parseToFloat(row["Road_Surface_Conditions"]))
