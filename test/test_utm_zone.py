import utm_zone as UTM
import unittest

data = [
    # Gothenburg, Sweden
    ((11.974560, 57.708870), 32632),
    # New York, USA
    ((-74.00597, 40.71435), 32618),
    # San Jose, Costa Rica
    ((-84.087502, 9.934739), 32616),
    # Capetown, South Africa (northen)
    ((18.42406, -33.92487), 32734),
    # Bali, Indonesia (northen)
    ((115.188919, -8.409518), 32750),
    # Edinburgh, Scotland
    ((-3.200833, 55.948612), 32630),
]


class TestUtmZoneFromCoordinates(unittest.TestCase):
    def test_to_epsg_from_latlon(self):
        for latlon, expected_result in data:
            result = UTM.epsg(latlon)
            self.assertEqual(result, expected_result)


class TestUtmZoneFromGeoJson(unittest.TestCase):
    def to_geojson(self, pos):
        return {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": pos},
                }
            ],
        }

    def test_to_epsg_from_geojson(self):
        for latlon, expected_result in data:
            result = UTM.epsg(self.to_geojson(latlon))
            self.assertEqual(result, expected_result)
