import numpy as np
from scipy import stats


class ANOVA:
    def oneWayANOVA_Experiment(self, experiment):
        data_arrays = []
        gene_id_array = []
        passed_anova_container = []

        for samplegroup in experiment.returnSampleGroups():
            sample_group_array = []

            for sample in samplegroup.returnAllSamples():
                path = sample.getSampleFilePath()
                reader = open(path, 'r')
                lines = reader.readlines()

                if len(gene_id_array) == 0:
                    for x in range(1, lines.__len__()):
                        gene_id_array.append(lines[x].split('\t')[0])

                sample_group_array.append(lines)

            sample_group_num_array = []

            for x in range(1, sample_group_array[0].__len__()):
                exprArray = []
                for sample_group in sample_group_array:
                    exprArray.append(float(sample_group[x].split('\t')[1]))
                sample_group_num_array.append(exprArray)
            data_arrays.append(sample_group_num_array)

        for gene_index in range(0, len(data_arrays[1])):
            npArray = []

            for array in data_arrays:
                npArray.append(array[gene_index])

            F, p = stats.f_oneway(*[d for d in npArray])

            if float(p) < 0.05:
                container_associate_array = [ gene_id_array[gene_index], npArray, F, p ]
                passed_anova_container.append(container_associate_array)

        return passed_anova_container


class DynamicRecArray(object):
    def __init__(self, dataType):
        self.dataType = np.dtype(dataType)
        self.length = 0
        self.size = 10
        self._data = np.empty(self.size, dtype=self.dataType)

    def __len__(self):
        return self.length

    def append(self, record):
        if self.length == self.size:
            self.size = int(1.5 * self.size)
            self._data = np.resize(self._data, self.size)
        self._data[self.length] = record
        self.length += 1

    def extend(self, records):
        for record in records:
            self.append(record)

    @property
    def data(self):
        return self._data[:self.length]