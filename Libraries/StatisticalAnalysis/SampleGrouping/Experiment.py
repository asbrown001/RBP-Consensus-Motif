

class Experiment:
    def __init__(self, experimentName):
        self.SampleGroups = []
        self.TotalSampleGroups = 0
        self.ExperimentName = experimentName
        self.DataTablePath = ''

    def addSampleGroupToExperiment(self, sampleGroup):
        self.TotalSampleGroups += 1
        self.SampleGroups.append(sampleGroup)

    def returnExperimentName(self):
        return self.ExperimentName

    def returnTotalNumberOfSampleGroups(self):
        return self.TotalSampleGroups

    def returnSampleGroups(self):
        return self.SampleGroups

    def setDataTablePath(self, file_path):
        self.DataTablePath = file_path

    def getDataTablePath(self):
        return self.DataTablePath