import os

app_directory = r"/Users/andrew/Google Drive/Nucleic Acid Research/SourceCode/RBP-Consensus-Motif_1.0.1/"
working_directory = os.path.join(app_directory, "SampleData/Temp/Temp")
output_directory = os.path.join(app_directory, "SampleData/Temp/Temp/MapFile")

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

output_file = os.path.join(output_directory, "mapfile.txt")
output = open(output_file, 'w')

output.write('cel_files\n')

for f in os.listdir(working_directory):
    if os.path.splitext(f)[1][1:].upper() == 'CEL':
        file_path = os.path.join(working_directory, f)
        output.write(str(file_path) + '\n')

output.close()