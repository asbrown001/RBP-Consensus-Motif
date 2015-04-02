import os, os.path, zipfile, gzip, tarfile


class Decompress:
    def unZip(self, fileName, destinationFilePath):
        with zipfile.ZipFile(fileName) as zf:
            for member in zf.infolist():
                directories = member.filename.split('/')
                path = destinationFilePath
                for directory in directories[:-1]:
                    drive, directory = os.path.splitdrive(directory)
                    head, directory = os.path.split(directory)

                    if directory in (os.curdir, os.pardir, ''): continue
                    path = os.path.join(path, directory)

                zf.extract(member, path)

    def gUnzip(self, fileName, destinationFilePath):
        print "Expanding archive to .data file "
        f = gzip.open(fileName, 'rb')
        content = f.read()
        print "File expanded "
        tempDecompress = open(destinationFilePath, 'w')
        print "Writing decompressed archive to Temp directory "
        tempDecompress.write(content)
        print "Writing complete, file saved in decompressed format in " + destinationFilePath
        tempDecompress.close()
        f.close()

    def unTar(self, fileName, destinationFilePath):
        tar = tarfile.open(fileName)
        print "Expanding archive to .data file "
        tar.extractall(destinationFilePath)
        print "File expanded and moved to new destination "
        tar.close()
        for f in os.listdir(destinationFilePath):
            if os.path.splitext(f)[1][1:].upper() == 'GZ':
                archive_path = os.path.join(destinationFilePath, f)
                unarchive_path = os.path.join(destinationFilePath, "Temp")

                if not os.path.exists(unarchive_path):
                    os.mkdir(unarchive_path)
                unarchive_zip_path = os.path.join(unarchive_path, str(f).split('.')[0] + ".CEL")
                self.gUnzip(archive_path, unarchive_zip_path)