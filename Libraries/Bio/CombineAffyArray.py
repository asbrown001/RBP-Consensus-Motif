import os
from StandardDeviation import StandardDeviation
from SampleAttribute import SampleAttribute


class CombineAffyArray:

    def __init__(self, rbp_consensus_root):
        self.outputPath = os.path.join(rbp_consensus_root, "Defaults/CombinedCEL")

    def createPhenotypTableForR(self, attributeArray, output_path, append, sampleName):
        dataLine = ''

        if not append:
            file_mode = 'a'
        else:
            dataLine = 'ColumnID\t'
            for attribute in attributeArray:
                dataLine += attribute.getAttributeName().replace(' ', '_') + '\t'

            dataLine = dataLine.rpartition("\t")[0]
            dataLine += "\n"
            file_mode = 'w'

        writer = open(output_path, file_mode)

        if len(dataLine) > 0:
            writer.write(dataLine)

        dataLine = sampleName.replace(' ', '_') + '\t'

        for attribute in attributeArray:
            dataLine += attribute.getAttributeValue().replace(' ', '_') + '\t'

        dataLine = dataLine.rpartition('\t')[0]
        writer.write(dataLine + '\n')
        writer.close()

    def createDataTableForExperiment(self, sampleGroupPaths, outputPath):
        desc_path = outputPath + '.verbose'
        descWriter = open(desc_path, 'w')
        sample_group_arrays = []

        for sampleGroup in sampleGroupPaths:
            reader = open(sampleGroup, 'r')
            lines = reader.readlines()
            sample_group_arrays.append(lines)

        arrayLength = self.calculateArrayLength(sample_group_arrays[0])

        for x in range(0, arrayLength):
            y = 0
            descLine = ''

            for sampleArray in sample_group_arrays:
                aLine = sampleArray[x]
                aLine = aLine.replace('\n', '')

                if len(str(aLine).replace(' ', '')) > 0:
                    if '\t' in aLine:
                        columns = aLine.split('\t')

                        if x == 0:
                            if y == (len(sample_group_arrays) - 1):
                                descLine += str(columns[1]) + '\n'
                            else:
                                descLine += str(columns[1]) + '\t'
                        else:
                            if y == 0:
                                descLine += str(columns[0]) + '\t'
                                descLine += str(columns[1]) + '~'
                                descLine += str(columns[2]) + '~'
                                descLine += str(columns[3]) + '\t'

                            elif y == (len(sample_group_arrays) - 1):
                                descLine += str(columns[1]) + '~'
                                descLine += str(columns[2]) + '~'
                                descLine += str(columns[3]) + '\n'

                            else:
                                descLine += str(columns[1]) + '~'
                                descLine += str(columns[2]) + '~'
                                descLine += str(columns[3]) + '\t'

                    y += 1

            descWriter.write(descLine)

        descWriter.close()

        return desc_path


    def removePoorQuality(self, combine_path):
        f = open(combine_path, 'r')
        lines = f.readlines()

        arrayLength = self.calculateArrayLength(lines)
        file_name = os.path.splitext(combine_path)[0].split('/')[-1]
        file_name += '.quality'
        q = os.path.splitext(combine_path)[0].split('/')
        del q[-1]
        dir_path = '/'.join(str(y) for y in q)
        file_path = os.path.join(dir_path, file_name)

        writer = open(file_path, 'w')
        headerLine = 'GeneId\t'

        for segment in lines[0].split('\t'):
            if len(str(segment)) > 0:
                headerLine += segment.split('|')[1] + '\t'

        headerLine = headerLine.rpartition('\t')[0]
        writer.write(headerLine)

        for x in range(1, arrayLength):
            line = str(lines[x].replace('\n', ''))
            columns = line.split('\t')
            pass_qual = True
            dataLine = ''
            y = 0

            for column in columns:
                if y == 0:
                    dataLine += column + '\t'
                elif y == (len(columns) - 1):
                    mean_expression = float(column.split('~')[0])
                    std_dev = float(column.split('~')[2])
                    dataLine += str(column).split('~')[0]
                    percent_dev = (std_dev / mean_expression)

                    if percent_dev > 0.12:
                        pass_qual = False
                else:
                    mean_expression = float(column.split('~')[0])
                    std_dev = float(column.split('~')[2])
                    dataLine += str(column).split('~')[0] + '\t'
                    percent_dev = (std_dev / mean_expression)

                    if percent_dev > 0.12:
                        pass_qual = False

                y += 1

            if pass_qual:
                writer.write(dataLine + '\n')

        f.close()
        return file_path

    def averageDuplicates(self, combine_path, sampleGroupName):
        f = open(combine_path, 'r')
        lines = f.readlines()

        arrayLength = self.calculateArrayLength(lines)
        file_name = os.path.splitext(combine_path)[0].split('/')[-1]
        file_name += '.avg'
        q = os.path.splitext(combine_path)[0].split('/')
        del q[-1]
        dir_path = '/'.join(str(y) for y in q)
        file_path = os.path.join(dir_path, file_name)

        writer = open(file_path, 'w')
        header_line = "GeneID\tMeanExpression|" + sampleGroupName.replace(' ', '_') + "\tVariance\tStandardDeviation\n"
        writer.write(header_line)

        for x in range(1, arrayLength):
            line = str(lines[x].replace('\n', ''))
            columns = line.split('\t')
            gene_id = columns[0]
            del columns[0]
            numColumns = self.calculateArrayLength(columns)
            sd = StandardDeviation()

            for y in range(0, numColumns):
                value = float(columns[y])
                sd.addValueToAnalysisArray(value)

            sd.calculateAverage()
            sd.calculateVariance()
            sd.calculateStdDev()

            dataLine = sd.returnDataLine()
            write_line = gene_id + '\t' + dataLine
            writer.write(write_line)

        writer.close()
        f.close()
        return file_path\

    def combineSampleGroupFiles(self, fileArray, sampleGroupName):
        readerArray = []

        for f in fileArray:
            reader = open(f, 'r')
            lines = reader.readlines()
            readerArray.append(lines)

        arrayLength = self.calculateArrayLength(readerArray[0])
        sampleGroup_path = os.path.join(self.outputPath, sampleGroupName)

        if not os.path.exists(sampleGroup_path):
            os.mkdir(sampleGroup_path)

        newFile_path = os.path.join(sampleGroup_path, sampleGroupName + '.norm')
        writer = open(newFile_path, 'w')

        for x in range(0, arrayLength):
            y = 0
            dataLine = ''
            numFiles = len(fileArray)

            for r in readerArray:
                line = str(r[x]).replace('\n', '')

                if '\t' in line:
                    if x == 0:
                        line = str(line).replace('\t', '')
                    if y == 0 and x != 0:
                        pass
                    if x > 0 and y > 0:
                        line = line.split('\t')[1]
                        line = line.replace('\t', '')

                    if numFiles == (y + 1):
                        dataLine += line
                    else:
                        dataLine += line + '\t'

                y += 1

            if len(dataLine) > 0:
                writer.write(dataLine + '\n')

        writer.close()
        return newFile_path

    def calculateArrayLength(self, reader):
        length = reader.__len__()
        return length