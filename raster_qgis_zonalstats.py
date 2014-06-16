# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:07:17 2014
Source:
http://gis.stackexchange.com/questions/45284/how-to-use-qgis-zonal-stats-plugin-from-python-console
@author: jobel
"""

from qgis.analysis import QgsZonalStatistics

#specify polygon shapefile vector
polygonLayer = QgsVectorLayer('F:/temp/zonalstat/zonePoly.shp', 'zonepolygons', "ogr") 

# specify raster filename
rasterFilePath = 'F:/temp/zonalstat/raster1.tif'

# usage - QgsZonalStatistics (QgsVectorLayer *polygonLayer, const QString &rasterFile, const QString &attributePrefix="", int rasterBand=1)
zoneStat = QgsZonalStatistics (polygonLayer, rasterFilePath, 'pre-', 1)
zoneStat.calculateStatistics(None)