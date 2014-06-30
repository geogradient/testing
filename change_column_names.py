# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 11:28:30 2014

@author: jobel
"""
from jobel.files import walkdir

destDir = '/home/jobel/testing/collocate_cvs/test/'
srcDir = dict({"MEGS":"/home/jobel/testing/collocate_cvs/MEGS/",
               "FUB":"/home/jobel/testing/collocate_cvs/FUB/"})
               
#srcDir  = '/media/jobel/SeagateDrive/eodata2014/level2/MEGS/'
#

srcList = walkdir.list_files_by_type(srcDir["MEGS"])


'''
for ifile in srcList:
    
df =  pd.read_csv(srcList[1], sep="\t")

columnList = list(df.columns.values)

newName = list()
jobel.beam.split_columnName(icolumn)

for icolumn in columnList:
    newName.append(
    
jobel.files.walkdir()

''' 



       
    
    

