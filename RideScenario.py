class RideScenario:
    def __init__(self, longitude, latitude, dayOfWeek, roadType, speedLimit, lightConditions, weatherConditions,
                 roadConditions):
        self.latitude = latitude
        self.longitude = longitude
        self.dayOfWeek = dayOfWeek
        self.roadType = roadType
        self.speedLimit = speedLimit
        self.lightConditions = lightConditions
        self.weatherConditions = weatherConditions
        self.roadConditions = roadConditions

    def getDataPoint(self):
        return (
        self.longitude, self.latitude, self.dayOfWeek, self.roadType, self.speedLimit, self.lightConditions,
        self.weatherConditions, self.weatherConditions)
