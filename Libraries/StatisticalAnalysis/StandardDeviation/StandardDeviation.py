import math


class StandardDeviation:

    def __init__(self):
        self.variance = 0
        self.stdDev = 0
        self.mean = 0
        self.valueArray = []

    def addValueToAnalysisArray(self, value):
        self.valueArray.append(value)

    def calculateAverage(self):
        accumulator = 0

        for val in self.valueArray:
            accumulator += val

        mean = accumulator / len(self.valueArray)
        self.mean = mean

        return mean

    def calculateVariance(self):
        accumulator = 0

        for val in self.valueArray:
            subMean = val - self.mean
            accumulator += (subMean * subMean)

        variance = accumulator / len(self.valueArray)
        self.variance = variance

        return variance

    def calculateStdDev(self):
        stdDev = math.sqrt(self.variance)
        self.stdDev = stdDev

        return stdDev

    def returnDataLine(self):
        return str(self.mean) + '\t' + str(self.variance) + '\t' + str(self.stdDev) + '\n'