import unittest
from datetime import datetime
import tzconvert, tzhelpers

NAIVE_DATE_TIME_FORMAT = "%d:%m:%y %H:%M:%S"


class TestTZConverter(unittest.TestCase):
    def setUp(self):
        self.cities = [
            "Mumbai",
            "London",
            "San Francisco",
            "Shanghai",
            "Manila",
            "Sydney",
            "Cape town",
            "Rome",
            "Oslo",
            "Moscow"
        ]

        self.city_fixed_times = [
            "21:04:20 22:53:24 GMT+0100",
            "21:04:20 14:53:24 GMT-0700",
            "22:04:20 05:53:24 GMT+0800",
            "22:04:20 05:53:24 GMT+0800",
            "22:04:20 07:53:24 GMT+1000",
            "21:04:20 23:53:24 GMT+0200",
            "21:04:20 23:53:24 GMT+0200",
            "21:04:20 23:53:24 GMT+0200",
            "22:04:20 00:53:24 GMT+0300"
        ]

        self.naive_date_str_fixed = "21:04:20 21:53:24"

    def tearDown(self):
        self.cities = []
        self.naive_date = None

    def test_tz_helper(self):
        pass

    def test_tz_converter(self):
        naive_date_obj = datetime.strptime(self.naive_date_str_fixed, NAIVE_DATE_TIME_FORMAT)

        for i, city in enumerate(self.cities):
            adjusted_date = tzconvert.adjust_datetime(naive_date_obj, city)
            adjusted_date_str = adjusted_date.strftime(tzhelpers.DATE_TIME_FORMAT)

            assert adjusted_date_str == self.city_fixed_times[i]


if __name__== "main":
    unittest.main()
