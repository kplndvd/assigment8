import json
import urllib.request
import ast


def get_quote():
    q = urllib.request.urlopen("http://quotes.stormconsultancy.co.uk/random.json").read()
    r = q.decode('utf-8')
    r = ast.literal_eval(r)
    author = r["author"]
    quote = r["quote"]
    quote_author ='"'+ quote+'"' + ' by: ' + author
    return quote_author



