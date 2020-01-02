import re


def swear(msg_list):

    with open('swear_words.txt', 'r') as swear_words:
        swear_words = swear_words.read()
        swear_words = re.sub("[^\w]", " ", swear_words).split()
    for item in swear_words:
        item = item.lower()
    swear_words = [item.replace(item, item.lower()) for item in swear_words]
    return any(word in swear_words for word in msg_list)
