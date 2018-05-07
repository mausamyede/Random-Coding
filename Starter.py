import csv

from AccidentPredictor import AccidentPredictor
from RideScenario import RideScenario
from Utilities import parseToFloat

predictor = AccidentPredictor()

with open("test_data.csv", "rb") as testObj:
    reader = csv.DictReader(testObj)
    for row in reader:
        currentRideScenario = RideScenario(parseToFloat(row["Longitude"]), parseToFloat(row["Latitude"]),
                                           parseToFloat(row["Day_of_Week"]), parseToFloat(row["Time"].replace(':', '')),
                                           parseToFloat(row["Road_Type"]), parseToFloat(row["Speed_limit"]),
                                           parseToFloat(row["Light_Conditions"]),
                                           parseToFloat(row["Weather_Conditions"]),
                                           parseToFloat(row["Road_Surface_Conditions"]))
        predictor.predictFor(currentRideScenario)
