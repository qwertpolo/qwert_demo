import requests


def is_unicode(url, auth=""):
    response = requests.get(url, auth=auth)
    return response.encoding == "utf-8"
