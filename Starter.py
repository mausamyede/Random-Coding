from AccidentPredictor import AccidentPredictor
from RideScenario import RideScenario

predictor = AccidentPredictor()
currentRideScenario = RideScenario(12, 234, 4, 1230, 4, 56, 4, 6, 7)
predictor.predictFor(currentRideScenario)