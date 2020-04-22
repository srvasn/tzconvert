import re

import lxml.html
import requests

DATE_TIME_FORMAT = "%d:%m:%y %H:%M:%S %Z%z"


def get_tz(city_name, debug=False):
    """
    :param city_name: city name as string
    :return: Dict containing timezone code and offset, or None on failure
    """
    regex = r"\((\w+)([+|-])(\d+):?(\d+)?\)$"

    search_string = "{} time zone".format(city_name)

    # need to pass a User-Agent header, else response does not include summary info that we want to grab
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get("https://www.google.com/search", {'q': search_string}, headers=headers)

    doc = lxml.html.document_fromstring(str(response.content))
    el = doc.xpath("//div[contains(@class, 'card-section')]")

    # grabbing dom node values
    tz_verbose_name = str(el[0][0].text_content()).strip()  #cosmetic
    tz_parsable = str(el[0][1].text_content()).strip()

    if debug:
        print("Response code : %d" % response.status_code)
        print("Verbose timezone name : %s " % tz_verbose_name)
        print("Parsable timezone string : %s" % tz_parsable)

    # run regular expression against string
    match = re.search(regex, tz_parsable)

    if not match:
        if debug: print("No match")

        return None

    # match found
    tz_string = match.group(1)
    tz_sign = match.group(2)
    tz_hrs = int(match.group(3))

    if match.group(4):  # minutes are not always returned
        tz_mins = int(match.group(4))
    else:
        tz_mins = 0

    if debug:
        print("Timezone string : %s" % tz_string)
        print("Timezone sign : %s" % tz_sign)
        print("Hours : %s" % tz_hrs)
        print("Mins : %s" % tz_mins)

    # calculate total offset in seconds
    offset_sec = tz_hrs * 3600 + tz_mins * 60;

    # adjusting offset according to captured sign
    if tz_sign == "-":
        offset_sec *= -1

    return {
        "tz_string": tz_string,
        "offset_sec": offset_sec
    }
