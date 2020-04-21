from datetime import datetime

from dateutil import tz

import tzhelpers


def adjust_datetime(naive_date, city_name, debug=False):
    """
    :param naive_date: Non tz aware datetime object
    :param city_name: City name as string
    :return: Tz aware datetime adjusted to city, None on failure
    """
    city_name = str(city_name).title()

    # setting timezone of naive date passed to utc
    local_aware_datetime = naive_date.replace(tzinfo=tz.tzutc())

    # fetching timezone values for city_name from helper
    adjusted_tz_vals = tzhelpers.get_tz(city_name, debug)

    # could not fetch values, probably due to incorrect web response
    if not adjusted_tz_vals:
        return None

    # creating tz offset object
    adjusted_tz_info = tz.tzoffset(adjusted_tz_vals["tz_string"], adjusted_tz_vals["offset_sec"])

    # converting timezone
    adjusted_datetime = local_aware_datetime.astimezone(adjusted_tz_info)

    return adjusted_datetime


if __name__ == "__main__":
    # demo

    cities = ["London", "San Francisco", "Shanghai", "Manila", "Sydney", "Cape town", "Rome", "Oslo", "Moscow"]

    # create naive date without timezone information
    current_datetime = datetime.utcnow()

    for city in cities:
        print("\nCity name : %s" % city)

        naive_datetime = current_datetime
        adjusted_datetime = adjust_datetime(naive_datetime, city)

        if not adjusted_datetime:
            print("Could not fetch adjusted date time")
            continue

        print("Naive date : %s" % current_datetime.strftime(tzhelpers.DATE_TIME_FORMAT))
        print("Adjusted date : %s\n" % adjusted_datetime.strftime(tzhelpers.DATE_TIME_FORMAT))
