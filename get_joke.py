import http.client
import json


def get_joke():
    conn = http.client.HTTPSConnection("joke3.p.rapidapi.com")
    payload = ''
    headers = {
        'x-rapidapi-key': '436a2c8ec8mshc0cd71fcc152ca4p137da1jsnf6d60cbcb459'
    }
    conn.request("GET", "/v1/joke", payload, headers)
    res = conn.getresponse()
    data = res.read()
    j = data.decode("utf-8")
    n = json.loads(j)
    joke = n["content"]
    return joke
