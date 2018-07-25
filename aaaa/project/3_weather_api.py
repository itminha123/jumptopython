import urllib.request
import datetime
import json
import time

access_key = "UREVmQGGPyZcH9gz8eKshT%2Ffyo6paHADoJ4G2P1LuuJMY%2FqoBjGdMJ2icmwgclLU1cVM8YLzAz4qrpeKmfEKEg%3D%3D"


def get_request_url(url):
    req = urllib.request.Request(url)