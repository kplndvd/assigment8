import re
import random
import datetime
# import urllib.request
# from joke import joke
from swear import swear
from financial import financial
from bank import bank

name_mentioned = ""


def names(msg_list):
    with open('name_list.txt', 'r') as name_list:
        name_list = name_list.read()
        name_list = re.sub("[^\w]", " ", name_list).split()
    name_list = [item.replace(item, item.lower()) for item in name_list]

    for word in name_list:
        if word in msg_list:
            global name_mentioned
            name_mentioned = word.title()
    result = any(word in name_list for word in msg_list)

    return result


def get_name_list_after_update():
    name_responses = [f"Hi! {name_mentioned} fancy meeting you here", f"Welcome {name_mentioned} :) ",
                      f"Howdy {name_mentioned} :)", f"{name_mentioned} ... I like that name",
                      f"{name_mentioned}  What a beautiful name!"]
    return {"animation": "excited", "msg": random.choice(name_responses)}


def analyze_msg(msg):
    msg_list = msg.split()
    msg_list = [word.replace(word, word.lower()) for word in msg_list]

    if any(word in bank['inlove_words'] for word in msg_list):
        return {"animation": "inlove", "msg": random.choice(bank["inlove_responses"])}

    elif any(word in bank['heartbroke_words'] for word in msg_list):
        return {"animation": "heartbroke", "msg": random.choice(bank['heartbroke_responses'])}

    elif any(word in bank['funny_words'] for word in msg_list):
        return {"animation": "giggling", "msg": random.choice(bank['funny_responses'])}

    elif any(word in bank['dog_words'] for word in msg_list):
        return {"animation": "dog", "msg": random.choice(bank['dog_responses'])}

    elif any(word in bank['crying_words'] for word in msg_list):
        return {"animation": "crying", "msg": random.choice(bank['crying_responses'])}

    elif any(word in bank['bored_words'] for word in msg_list):
        return {"animation": "bored", "msg": random.choice(bank['bored_responses'])}

    elif any(word in bank['afraid_words'] for word in msg_list):
        return {"animation": "afraid", "msg": random.choice(bank['afraid_responses'])}

    elif any(word in bank['waiting_words'] for word in msg_list):
        return {"animation": "waiting", "msg": random.choice(bank['waiting_responses'])}

    elif any(word in bank['no_words'] for word in msg_list):
        return {"animation": "no", "msg": random.choice(bank['no_responses'])}

    elif msg.endswith("!"):
        return {"animation": "dancing", "msg": random.choice(bank['dancing_responses'])}

    elif msg.endswith("?"):
        return {"animation": "takeoff", "msg": random.choice(bank['takeoff_responses'])}

    elif financial(msg_list) or "$" in msg_list:
        return {"animation": "money", "msg": random.choice(bank['financial_responses'])}

    elif any(word in bank['time_list'] for word in msg_list):
        now = str(datetime.datetime.now())
        return {"animation": "ok", "msg": now}

    elif swear(msg_list):
        return {"animation": "confused", "msg": random.choice(swear_responses)}

    elif names(msg_list):
        return get_name_list_after_update()

    else:
        return {"animation": "inlove", "msg": random.choice(bank['default_responses'])}










