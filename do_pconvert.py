#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

"""
Created on 02.05.2012
@author: Jose Beltran based on Uwe's script do_smile_correction.py
"""
from os import system, listdir
from sys import exit
import gpt_configuration

#########  #########################
#dataReprocessingVersion = gpt_configuration.dataReprocessingVersion
#srcDir  = gpt_configuration.wewWaterSrcDir
srcDir  = gpt_configuration.srcDirs['toProcess']
destDir = gpt_configuration.srcDirs['test']

###########################################################
def exit_on_empty_list(list):
    _size = len(list)
    if _size == 0:
        print "Nothing to do here. Now quitting."
        exit(1)
    else:
        return _size

# Get the input list
srcList = listdir(srcDir)
listSize = exit_on_empty_list(srcList)

# MER_FSG_2PNUPA20100524_092812_000000252089_00394_43033_2920.N1
# 0         1         2         3         4         5         6
# 01234567890123456789012345678901234567890123456789012345678901
# pin_20080709_Asko2008.placemark 


# List clean up the files that are no products or not MERIS FSG Level1B or not N1 products
for a in range(listSize):
    for item in srcList:
        if not item.endswith('.nc'):
            print "Removing " + item + " from list."
            srcList.remove(item)
exit_on_empty_list(srcList)
srcList.sort()


for merisFile in srcList:
    inputFileName = srcDir + merisFile
       
    print "pconvert Processing file " + merisFile + " ..."
    
    #ExCommand = gpt_configuration.pconvertProcessor + " -f dim " + inputFileName + " -o " + destDir
    " writing a png file of a band 1 [FUB = algal_2]"
    " for MEGS chlorophyll_2  is  band 37 by using the nc product not N1"
    ExCommand = gpt_configuration.pconvertProcessor + " -f png -b 37 " + inputFileName + " -o " + destDir
    print ExCommand
    #print "FUB-WeW 1.2.8 processing: Processing file " + merisFile + " ..."
    system(ExCommand)

print 'done'
