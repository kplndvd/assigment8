import re
import random


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

