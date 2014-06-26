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

destDir = '/home/jobel/testing/FUB_ELINA/dimap/'
srcDir  = '/home/jobel/testing/FUB_ELINA/' # gpt_configuration.srcDirs['CCL1P_out']

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
    MEGS b[35] = suspended_particle_matter
         b[37] = chlorophyll_2
         33 = yellow_substance
         60 = nnboa_chl2
         61 = nnboa_spm
         
         16 = reflectance_01
         28 = reflectance_14
         231 = c2r_chi_sum_wat
         241 = c2r_RLw_01
         249 = c2r_RLw_09
         250 = c2r_RLw_a_01
         258 = c2r_RLw_a_09
         
    '''    
    ExCommand = beam.pconvertProcessor + " -f dim " + merisFile + " -o " + destDir 
    print(ExCommand+'\\')    
 
    os.system(ExCommand)

print('done')
