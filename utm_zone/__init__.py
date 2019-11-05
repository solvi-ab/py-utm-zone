from numbers import Number
import math

def epsg(geojson):
  """
  Provided a GeoJSON object, returns the EPSG code (integer) for the UTM zone best
  matching the GeoJSON's geometry.
  """
  firstCoord = getFirstCoord(geojson)
  offset = int(round((183 + firstCoord[0]) / 6.0))
  return 32600 + offset if firstCoord[1] > 0 else 32700 + offset

def proj(geojson):
  """
  Provided a GeoJSON object, returns the Proj.4 definition for the UTM zone best
  matching the GeoJSON's geometry.
  """
  firstCoord = getFirstCoord(geojson)
  zone = int(math.floor((firstCoord[0] + 180) / 6.0) + 1)
  return '+proj=utm +zone=%d +%s +datum=WGS84 +units=m +no_defs' % \
    (zone, 'north' if firstCoord[1] >= 0 else 'south')

def getFirstCoord(geojson):
  def recurse(coordinates):
    if not isinstance(coordinates[0], Number):
      return recurse(coordinates[0])
    else:
      return coordinates

  firstCoord = \
    recurse(geojson['coordinates']) if 'coordinates' in geojson \
    else recurse(geojson['geometry']['coordinates']) if 'geometry' in geojson \
    else recurse(geojson['geometries'][0]['coordinates']) if 'geometries' in geojson \
    else recurse(geojson['features'][0]['geometry']['coordinates']) if 'features' in geojson \
    else None

  if not firstCoord:
    raise Exception('Could not find any coordinates in this GeoJSON')

  return firstCoord
