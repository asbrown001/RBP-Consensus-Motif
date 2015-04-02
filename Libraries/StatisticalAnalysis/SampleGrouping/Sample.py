class Sample:
    def __init__(self, sampleName, path):
        self.SampleName = sampleName
        self.SampleFilePath = path

    def getSampleGroupName(self):
        return self.SampleName

    def getSampleFilePath(self):
        return self.SampleFilePath
