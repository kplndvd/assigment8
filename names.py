import re


def names(msg_list):

    with open('name_list.txt', 'r') as name_list:
        name_list = name_list.read()
        name_list = re.sub("[^\w]", " ", name_list).split()
    name_list = [item.replace(item, item.lower()) for item in name_list]


    return any(word in name_list for word in msg_list)
