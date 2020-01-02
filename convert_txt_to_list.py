

# def convert_txt_to_list(some_txt_file, list_prefix)
#     with open(some_txt_file, 'r') as f{list_prefix}+"_words":
#
#         # financial_words = financial_words.read()
#         # financial_words = re.sub("[^\w]", " ", financial_words).split()
#         #
#         #
#         # dict={}
#         #


import urllib.request
import json

r = urllib.request.urlopen("http://quotes.stormconsultancy.co.uk/random.json").read()
r = r.decode('utf-8')
print(r)
author = r.author
q = r.quote
