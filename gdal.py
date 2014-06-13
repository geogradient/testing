#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reproject 
"""

from osgeo import gdal, osr
# Source
src_filename = 'MENHMAgome01_8301/mllw.gtx'
src = gdal.Open(src_filename, gdalconst.GA_ReadOnly)
src_proj = src.GetProjection()
src_geotrans = src.GetGeoTransform()

# We want a section of source that matches this:
match_filename = 'F00574_MB_2m_MLLW_2of3.bag'
match_ds = gdal.Open(match_filename, gdalconst.GA_ReadOnly)
match_proj = match_ds.GetProjection()
match_geotrans = match_ds.GetGeoTransform()
wide = match_ds.RasterXSize
high = match_ds.RasterYSize

# Output / destination
dst_filename = 'F00574_MB_2m_MLLW_2of3_mllw_offset.tif'
dst = gdal.GetDriverByName('GTiff').Create(dst_filename, wide, high, 1, gdalconst.GDT_Float32)
dst.SetGeoTransform( match_geotrans )
dst.SetProjection( match_proj)

# Do the work
gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)

del dst # Flusht


#---
def reproject_dataset ( dataset, \
            pixel_spacing=5000., epsg_from=4326, epsg_to=27700 ):
    """
    A sample function to reproject and resample a GDAL dataset from within 
    Python. The idea here is to reproject from one system to another, as well
    as to change the pixel size. The procedure is slightly long-winded, but
    goes like this:
    
    1. Set up the two Spatial Reference systems.
    2. Open the original dataset, and get the geotransform
    3. Calculate bounds of new geotransform by projecting the UL corners 
    4. Calculate the number of pixels with the new projection & spacing
    5. Create an in-memory raster dataset
    6. Perform the projection
    """
    # Define the UK OSNG, see <http://spatialreference.org/ref/epsg/27700/>
    osng = osr.SpatialReference ()
    osng.ImportFromEPSG ( epsg_to )
    wgs84 = osr.SpatialReference ()
    wgs84.ImportFromEPSG ( epsg_from )
    tx = osr.CoordinateTransformation ( wgs84, osng )
    # Up to here, all  the projection have been defined, as well as a 
    # transformation from the from to the  to :)
    # We now open the dataset
    g = gdal.Open ( dataset )
    # Get the Geotransform vector
    geo_t = g.GetGeoTransform ()
    x_size = g.RasterXSize # Raster xsize
    y_size = g.RasterYSize # Raster ysize
    # Work out the boundaries of the new dataset in the target projection
    (ulx, uly, ulz ) = tx.TransformPoint( geo_t[0], geo_t[3])
    (lrx, lry, lrz ) = tx.TransformPoint( geo_t[0] + geo_t[1]*x_size, \
                                          geo_t[3] + geo_t[5]*y_size )
    # See how using 27700 and WGS84 introduces a z-value!
    # Now, we create an in-memory raster
    mem_drv = gdal.GetDriverByName( 'MEM' )
    # The size of the raster is given the new projection and pixel spacing
    # Using the values we calculated above. Also, setting it to store one band
    # and to use Float32 data type.
    dest = mem_drv.Create('', int((lrx - ulx)/pixel_spacing), \
            int((uly - lry)/pixel_spacing), 1, gdal.GDT_Float32)
    # Calculate the new geotransform
    new_geo = ( ulx, pixel_spacing, geo_t[2], \
                uly, geo_t[4], -pixel_spacing )
    # Set the geotransform
    dest.SetGeoTransform( new_geo )
    dest.SetProjection ( osng.ExportToWkt() )
    # Perform the projection/resampling 
    res = gdal.ReprojectImage( g, dest, \
                wgs84.ExportToWkt(), osng.ExportToWkt(), \
                gdal.GRA_Bilinear )
    return dest