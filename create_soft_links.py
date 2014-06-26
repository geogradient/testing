# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 09:38:52 2014
Mantainer: José Beltrán [email](<beltran.data@gmail.com>)
Last update: 2014-06-17 Version: 1.0

"""
import os
#from os.path import exists

destDir = '/home/jobel/testing/softlinks/'
srcDir  = '/media/jobel/SeagateDrive/eodata2014/level2/MEGS/' 

xmlrequest = '/media/jobel/SeagateDrive/eodata2014/level2/test/gpt_graph.xml'
#
srcList = list()
# Adding recursive walk for directories
for dirpath, dirnames, files in os.walk(srcDir):
    for file in files: # files is a list of files in the current directory
        if file.lower().endswith(".nc"): #".nc"
            #fullpath = #os.path.join(root, file)
            currentFilepath = dirpath
            srcList.append(os.path.join(currentFilepath, file))
        #else:
         #   print("File format not recognized")
srcList.sort()
print("file list to process ready")

#
filterList = list()

for merisFile in srcList:
    merisFileName = os.path.basename(merisFile) # MERIS filename extraction
    merisYear = merisFileName[14:18]
    if (merisYear in ["2008","2010","2011"]):
        filterList.append(merisFile)
        print("Keep in this one")
     
for merisFile in filterList:
    
    merisFileName = os.path.basename(merisFile) # MERIS filename extraction
    inputFileName = merisFile # Keep the full path and current MERIS filename
    outputFile = destDir + merisFileName # New filename
    
    print("Processing: Processing file " + merisFile + " ...")
    
    ExCommand = "ln -s " +  inputFileName + " " + outputFile
    print(ExCommand+'\n')   
 
    os.system(ExCommand)

print('done')

