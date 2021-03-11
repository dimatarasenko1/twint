import datetime

import logging as logme

from .tweet import utc_to_local


class Datelock:
    until = None
    since = None
    _since_def_user = None


def convertToDateTime(string):
    dateTimeList = string.split()
    ListLength = len(dateTimeList)
    if ListLength == 2:
        return string
    if ListLength == 1:
        return string + " 00:00:00"
    else:
        return ""


def Set(Until, Since):
    logme.debug(__name__+':Set')
    d = Datelock()
    d.until = Until
    d.since = Since
    if Until:
        d.until = datetime.datetime.strptime(Until, "%Y-%m-%d")
        d.until = utc_to_local(d.until)
    else:
        d.until = datetime.datetime.today()

    if Since:
        d.since = datetime.datetime.strptime(Since, "%Y-%m-%d")
        d.since = utc_to_local(d.since)
        d._since_def_user = True
    else:
        d.since = datetime.datetime.strptime("2006-03-21 00:00:00", "%Y-%m-%d %H:%M:%S")
        d.since = utc_to_local(d.since)
        d._since_def_user = False

    return d
