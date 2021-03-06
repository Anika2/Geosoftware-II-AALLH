'''
Created on 16.01.2019
@author: Aysel Tandik
'''

import os
import sys
import tempfile

# add local modules folder
file_path = os.path.join('..', 'Testdata')
sys.path.append(file_path)

import unittest
import getBoundingBox

# Dataformat Geojson testing Polygon, Line, Point
def test_getBBJsonPolygon():
    # Dijon (nähe Paris)
    result = getBoundingBox.getBoundingBox("polygon.geojson", file_path)
    assert result == ([3.5218322277,46.7697482029, 7.4549376965,48.574577168], None)

def test_getBBJsonLine():
    result = getBoundingBox.getBoundingBox("lineString.geojson", file_path)
    assert result == ([6.564331, 51.108696, 7.099915, 51.280817], None)

def test_getBBJsonPoint():
    result = getBoundingBox.getBoundingBox("kalterherbergPoint.geojson", file_path)
    assert result == ([6.220493316650391, 50.52150360276628, 6.220493316650391, 50.52150360276628], None)

# Dataformat Csv testing Polygon
def test_getBBCsvPolygon():
    result = getBoundingBox.getBoundingBox("Polygon.csv", file_path)
    assert result == ([8.195801,51.998410,10.447998,52.789476], None)

# Dataformat NetCdf testing
def test_getBBNetCdf():
    result = getBoundingBox.getBoundingBox("cami_0000-09-01_64x128_L26_c030918.nc", file_path)
    assert result == ([0.0, -87.86379883923348, 357.1875, 87.86379883923263], None)

# Dataformat Shape testing Line, Polgyon and one additional file
def test_getBBShapeLine():
    result = getBoundingBox.getBoundingBox("POLYLINE.shp", file_path)
    assert result == ([7.6016807556152335, 51.94881477206191, 7.647256851196289, 51.974624029877454], None)

def test_getBBShapePolygon():
    result = getBoundingBox.getBoundingBox("POLYGON.shp", file_path)
    assert result == ([7.594213485717774, 51.94246595679555, 7.61824607849121, 51.95727846118796], None)

# Testing the coordinate reference system from EPSG:3857 WGS 84 / Pseudo-Mercator
# to EPSG:4326 WGS 84 --> Result must be: lat: 8.591308, lon: 52.49616
def test_CRS():
    stringResult = getBoundingBox.CRSTransform(959984.29, 5843845.80, 3857)
    string = str(stringResult[0])
    assert 0 == string.find("52.49616") # Longitude

    string2 = str(stringResult[1])
    assert 0 == string2.find("8.591308") # Latitude

# Testing the situation, where the datatype is not supported
def test_ErrorFile():
    errorfile = getBoundingBox.getBoundingBox("error.file", file_path)
    assert errorfile == (None, 'type .file not yet supported')

# Testing where input is not valid
def test_FalseInputFile():
    falseInput = getBoundingBox.getBoundingBox("falsetime.geojson", file_path)
    assert falseInput == (None, 'File Error!')
