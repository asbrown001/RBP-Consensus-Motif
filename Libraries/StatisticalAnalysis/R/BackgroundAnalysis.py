#import rpy2.interactive as r
from numpy import *
#import rpy2.robjects as ro
from rpy2 import *
import rpy2.robjects as ro
import rpy2.interactive as r
#from rpy2.robjects.packages import importr
#import rpy2.interactive.packages
import os

class BackgroundAnalysis:
    def analyzeCELFiles(self, rbp_working_dir):
        ro.packages.importr("oligo")
        ro.r('require(affy)')
        sample_groups = []
        cel_dir = os.path.join(rbp_working_dir, "Defaults/TextCel")
        output_dir = os.path.join(rbp_working_dir, "Defaults/NormalizedCEL")
        for f in os.listdir(cel_dir):
            if os.path.splitext(f)[1][1:].upper() == 'CEL':
                print "Found binary to text converted CEL file: " + str(f) + " "

                r_file_path = os.path.join(cel_dir, f)
                r_command = 'data <- ReadAffy("' + r_file_path + '")'
                ro.r(r_command)
                print "Reading " + str(f) + " into R w/ ReadAffy() "

                r_command = 'eset <- rma(data)'
                ro.r(r_command)
                print "Analyzing " + str(f) + " data, subtracting background, and normalizing "

                output_file_path = os.path.join(output_dir, str(f).split('.')[0] + '.txt')
                r_command = 'write.exprs(eset,file="' + output_file_path + '")'
                ro.r(r_command)
                print "File analyzed, normalized data can be found: " + str(output_file_path) + " "

                sample_groups.append(output_file_path)

        return sample_groups

