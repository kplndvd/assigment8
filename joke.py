import urllib.request
import ast


def get_joke():
    q = urllib.request.urlopen("https://joke3.p.rapidapi.com/v1/joke436a2c8ec8mshc0cd71fcc152ca4p137da1jsnf6d60cbcb459").read()
    r = q.decode('utf-8')
    r = ast.literal_eval(r)
    joke = r["content"]
    print(joke)
    return joke
get_joke()