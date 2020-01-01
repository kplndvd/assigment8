import re
import random


def analyze_msg(msg):
    msg_list = msg.split()
    msg_list = [word.replace(word, word.lower()) for word in msg_list]

    with open('swear_words.txt', 'r') as swear_words:
        swear_words = swear_words.read()
        swear_words = re.sub("[^\w]", " ", swear_words).split()
        for item in swear_words:
            item = item.lower()
    swear_words = [item.replace(item, item.lower()) for item in swear_words]

    swear_responses = ["You should wash your mouth with some soap!", "Please use clean language",
                       "I don't speak Klingon , try typing in English", " Looks like you have a typo",
                       "I'm not programmed for dirty language", ""]

    financial_words = []
    with open('financial_words.txt', 'r') as financial_words:
        financial_words = financial_words.read()
        financial_words = re.sub("[^\w]", " ", financial_words).split()

    financial_words = [item.replace(item, item.lower()) for item in financial_words]
    financial_responses = ["Show me the money!", "Get a lotto ticket I've got a good feeling about this :)"]

    if any(msg_list) == 'david'.lower():
        return {"animation": "inlove", "msg": " hello " + msg + " welcome to the chat!"}
    elif any(word in swear_words for word in msg_list):

        print("yes")
        return {"animation": "confused", "msg": random.choice(swear_responses)}

    # elif msg ....:
    #     return {"animation": "heartbroke", "msg": random.choice(swear_responses)}
    # elif msg in swear_words:
    #     return {"animation": "giggling", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "excited", "msg": random.choice(swear_responses)}
    # elif msg in swear_words:
    #     return {"animation": "dog", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "dancing", "msg": random.choice(swear_responses)}
    # elif msg in swear_words:
    #     return {"animation": "crying", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "bored", "msg": random.choice(swear_responses)}
    # elif msg in swear_words:
    #     return {"animation": "afraid", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "waiting", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "takeoff", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "ok", "msg": random.choice(swear_responses)}
    # elif msg ....:
    #     return {"animation": "no", "msg": random.choice(swear_responses)}
    elif any(msg_list) in financial_words:
        return {"animation": "money", "msg": random.choice(financial_responses)}
    else:
        return {"animation": "inlove", "msg": msg}








