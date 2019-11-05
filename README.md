# utm-zone

Find the UTM zone for your GeoJSON. 

Provided a GeoJSON object (with coordinates using WGS84), calculate the Proj.4 definition or EPSG code for a suitable UTM zone for this geometry. This will only work if the geometry has limited geographic size, so that it can fit into a single UTM zone.

Note that this module does not do any reprojection of coordinates, you might want to look at [pyproj](https://pypi.org/project/pyproj/) for that.

For a rough overview of how the UTM zone is calculated, have a look at [https://gis.stackexchange.com/a/190209/467](https://gis.stackexchange.com/a/190209/467).

See also [https://github.com/perliedman/utm-zone](https://github.com/perliedman/utm-zone) for a JavaScript version of this module.

## API

### `epsg(geojson)`

Returns the EPSG code for the UTM zone of the provided GeoJSON object.

### `proj(geojson)`

Returns the Proj.4 string for the UTM zone of the provided GeoJSON object.
