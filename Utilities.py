def parseToFloat(str):
    try:
        return float(str)
    except ValueError:
        return 0