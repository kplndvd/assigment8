import re
import random
import emojis


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
    name_responses = [f"Hi! {name_mentioned} fancy meeting you here" + emojis.encode(" :smile:"),
                      f"Welcome {name_mentioned}  " + emojis.encode(" :smile:"),
                      f"Howdy {name_mentioned} :)" + emojis.encode(" :smile:"),
                      f"{name_mentioned} ... I like that name" + emojis.encode(" :smile:"),
                      f"{name_mentioned}  What a beautiful name!" + emojis.encode(" :smile:")]
    return {"animation": "excited", "msg": random.choice(name_responses)}

