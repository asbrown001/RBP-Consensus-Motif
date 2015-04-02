class SampleGroup:
    def __init__(self, sampleGroupName):
        self.TotalSampleGroups = 0
        self.SampleGroupName = sampleGroupName
        self.Samples = []
        self.combinedFilePath = ''
        self.averageIntensityPath = ''
        self.descCombinedPath = ''
        self.qualityIntensityPath = ''
        self.sampleAttributes = []

    def addSampleToSampleGroup(self, sample):
        self.TotalSampleGroups += 1
        self.Samples.append(sample)

    def returnTotalSampleGroups(self):
        return self.TotalSampleGroups

    def returnSampleGroupName(self):
        return self.SampleGroupName

    def returnAllSamples(self):
        return self.Samples

    def setCombinedFilePath(self, filePath):
        self.combinedFilePath = filePath

    def returnCombinedFileReader(self):
        reader = open(self.combinedFilePath, 'r')
        return reader

    def setAverageIntensityPath(self, filePath):
        self.averageIntensityPath = filePath

    def returnAverageIntensityPath(self):
        return self.averageIntensityPath

    def setDescCombinedPath(self, filePath):
        self.combinedFilePath = filePath

    def getDescCombinedPath(self):
        return self.descCombinedPath

    def setQualityIntensityPath(self, filePath):
        self.qualityIntensityPath = filePath

    def getQualityIntensityPath(self):
        return self.qualityIntensityPath

    def addSampleAttributeToThis(self, attribute):
        self.sampleAttributes.append(attribute)

    def returnSampleAttributes(self):
        return self.sampleAttributes