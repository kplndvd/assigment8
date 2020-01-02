import re


def financial(msg_list):
    with open('financial_words.txt', 'r') as financial_words:
        financial_words = financial_words.read()
        financial_words = re.sub("[^\w]", " ", financial_words).split()
    financial_words = [item.replace(item, item.lower()) for item in financial_words]
    return any(word in financial_words for word in msg_list)