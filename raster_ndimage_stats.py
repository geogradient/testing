# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:21:15 2014
source:
http://gis.stackexchange.com/questions/43748/running-a-python-script-to-extract-raster-data-in-qgis
Your procedure is to make a raster of your zones. Then import your original raster and the zones raster each into a NumPy array. Make a third numpy array of the unique values in your zones array to use as an index for the ndimage function. Finally use one of the ndimage statistics to extract your result, e.g.



@author: jobel
"""
import numpy

myIndex = numpy.unique(zonesArray)    
minResult = ndimage.minimum(myRasterArray, labels=zonesArray, index=indexArray)