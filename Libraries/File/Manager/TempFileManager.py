import os
import pdb


class TempFileManager:
    def removeDirectoryFiles(self, directoryPath):
        if os.path.isdir(directoryPath):
            for dir in os.listdir(directoryPath):
                p = os.path.join(directoryPath, dir)
                if os.path.isfile(p):
                    print "Removing decompressed file " + p + " from Temp directory "
                    os.remove(p)
                    print "Temporary file removed "
                if os.path.isdir(p):
                    self.removeDirectoryFiles(p)