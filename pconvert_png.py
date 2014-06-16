# -*- coding: utf-8 -*-
"""
Created on Mon Jun  16 06:50:30 2014
Mantainer: José Beltrán [email](<beltran.data@gmail.com>)
Last update: 2014-06-16 Version: 1.0


**Subset and reproject from WGS84 to UTM33WGS84**
MEGS8.1 (ODESA1.2.4) MERIS FR datasets.
"""

"""The module gpt_config has the configuration paths for using the 
BEAM gpt processor (v5.0) localy."""


import os
#from os.path import exists

import gpt_config as beam

destDir = '/home/jobel/reprojected'
srcDir  = '/home/jobel/Dropbox/data/testing/' # gpt_configuration.srcDirs['CCL1P_out']

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
for merisFile in srcList:
    
    print ("pconvert Processing file " + merisFile + " ...")
    
    #ExCommand = gpt_configuration.pconvertProcessor + " -f dim " + inputFileName + " -o " + destDir
    #" writing a png file of a band 1 [FUB = algal_2]"
    #" for MEGS chlorophyll_2  is  band 37 by using the nc product not N1"
    
    #merisFileName = os.path.basename(merisFile) # MERIS filename extraction
    inputFileName = merisFile # Keep the full path and current MERIS filename
    #outputFile = 'FUB_algal_2_' 
    '''
    FUB b[1] = algal_2
        b[2] = yellow_subs
        b[3] = total_susp
         ...
    '''    
    ExCommand = beam.pconvertProcessor + " -m equalize -n 0,0,0,255 -f png -b 1 " + merisFile + " -o " + destDir 
    print(ExCommand+'\\')    
 
    os.system(ExCommand)

print('done')

