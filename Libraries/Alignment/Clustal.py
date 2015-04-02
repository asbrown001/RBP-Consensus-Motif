from Bio.Align.Applications import ClustalOmegaCommandline, ClustalwCommandline

class ClustalAlignment:
    def clustalOmega(self, infile, outfile):
        cline = ClustalOmegaCommandline(infile = infile, outfile = outfile, verbose = True, auto = True)
        cline()
    def clustalW(self, infile, outfile):
        clustalEXE = "clustalw2"
        cline = ClustalwCommandline(clustalEXE, infile = infile)
        cline()