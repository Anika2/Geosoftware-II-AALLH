# Author Aysel Tandik
# 17.01.2019

import unittest
import getPolygon

def test_Polygon():
    # polygon[[[6.9046222111,46.2504449229],[5.4863870954,46.8001811678],[5.8659149771,47.7689879162],[8.3927701106,47.969983885],[8.7223599544,46.8411872734],[6.9046222111,46.2504449229]]]
    # bounding box[[[5.4863870954,46.2504449229],[8.7223599544,46.2504449229],[8.7223599544,47.969983885],[5.4863870954,47.969983885],[5.4863870954,46.2504449229]]] # 
    result = getPolygon.getPolygon("BB.geojson", "C:\\Users\\celeb\\Desktop\\Testdaten")
    assert result == ([6.9046222111,46.2504449229],[5.4863870954,46.8001811678],[5.8659149771,47.7689879162],[8.3927701106,47.969983885],[8.7223599544,46.8411872734],[6.9046222111,46.2504449229], None)

def test_PolygonLine():
    result = getPolygon.getPolygon("lineString.geojson", "C:\\Users\\celeb\\Desktop\\Testdaten\\GeoJSON")
    assert result == ([(6.564331, 51.119041), (7.099915, 51.108696), (6.995544, 51.280817)], None)


