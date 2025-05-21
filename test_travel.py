#unit tests
import unittest
from api_utils import get_route_google, get_weather, get_places_google, geocode_location
from runner import run_evaluation

class TestTravelAgent(unittest.TestCase):
    def test_route_api(self):
        ok, data = get_route_google("San Francisco,CA", "Los Angeles,CA")
        self.assertTrue(ok)
        self.assertIn("routes", data)

    def test_weather_api(self):
        geo_ok, (lat, lon) = geocode_location("Los Angeles,CA")
        ok
