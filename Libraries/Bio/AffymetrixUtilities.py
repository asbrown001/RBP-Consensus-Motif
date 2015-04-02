import Bio.Affy.CelFile
import os
import subprocess
import shlex


class AffymetrixUtilities:
    absolute_apt_dir = ""

    def __init__(self, dir_rbp):
        app_dir = "Dependencies/AFP/Binaries/OSX/apt-1.16.1-x86_64-apple-lion/bin"
        self.absolute_apt_dir = os.path.join(dir_rbp, app_dir)

    def createCELFileForConversionMapping(self, rbp_dir):
        cel_dir = os.path.join(rbp_dir, "SampleData/Temp/Temp")
        output_dir = os.path.join(cel_dir, "Mapping")

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        output_file = os.path.join(output_dir, 'cel_mapping.txt')
        writer = open(output_file, 'w')
        writer.write('cel_files\n')

        for f in os.listdir(cel_dir):
            if os.path.splitext(f)[1][1:].upper() == 'CEL':
                write_path = os.path.join(cel_dir, f)
                writer.write(str(write_path) + '\n')

        writer.close()
        return str(output_file)

    def convertCELUsingAFP(self, cel_map_path, output_path):
        executable_path = os.path.join(self.absolute_apt_dir, "apt-cel-convert")
        executable_path = str(executable_path).replace(' ', '\ ')
        command = executable_path + ' --format text --out-dir "' + str(output_path) + '" --cel-files "' + str(cel_map_path) +'"'
        args = shlex.split(command)
        p = subprocess.Popen(args)
        p.wait()

    def readCELWithBioPython(self, affyFilePath):
        with open(affyFilePath) as handle:
            cel = Bio.Affy.CelFile.read(handle)
            return cel
