import urllib.request, urllib.error, urllib.parse
import re

def load_sync(path):
    if not re.match(r'^https?', path):
        path = 'http://%s' % path
    path = urllib.parse.unquote(path)
    return urllib.request.urlopen(path).read()
