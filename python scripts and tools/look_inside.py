import os

"""
This is a script that looks for inside
any directory or subdirectory that you
write in the variable path and find the
word that you store in the BAN variable.
"""

path = r'D:\Reportes\AR'
BAN = 'CHUTC'


for root, subdir, files in os.walk(path):
    print "Inside the first root --> " + str(root)
    print "Found " + str(len(files)) + " files!!!"
    print "Found " + str(len(subdir)) + " subdirectories!!!"
    if len(subdir) == 0:  #Means there are only files inside
        for eachFile in files:
            file_name = root + os.sep + eachFile
            fp = open(file_name, 'r')
            print "Parsing file: " + str(file_name)
            for eachLine in fp.readlines():            
                if BAN in eachLine:
                    print "Found " + BAN + " in " + eachFile
                    print "This is the line: "
                    print eachLine
            fp.close()
    else:  #Means there are subdirectories inside
        for eachSubDirectory in subdir:        
            eachSubDirectory = root + os.sep + eachSubDirectory
            print "#######", eachSubDirectory
            for eachSubDirRoot, eachSubDir, filesSubDir in os.walk(eachSubDirectory):
                print "!!!", eachSubDirRoot
                print "@@@", eachSubDir
                print "$$$", filesSubDir
                for eachFile in filesSubDir:
                    file_name = eachSubDirRoot + os.sep + eachFile
                    fp = open(file_name, 'r')
                    print "Parsing file: " + str(file_name)
                    for eachLine in fp.readlines():            
                        if BAN in eachLine:
                            print "Found " + BAN + " in " + eachFile
                            print "This is the line: "
                            print eachLine
                    fp.close()

print "Finished looking inside this directory"
