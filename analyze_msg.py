

import random
import datetime
from swear import swear
from financial import financial
from bank import bank
from names import names, get_name_list_after_update
from get_quote import get_quote
from get_joke import get_joke
import emojis


def analyze_msg(msg):
    msg_list = msg.split()
    msg_list = [word.replace(word, word.lower()) for word in msg_list]

    if any(word in bank['inlove_words'] for word in msg_list):
        return {"animation": "inlove", "msg": random.choice(bank["inlove_responses"])}

    elif any(word in bank['heartbroke_words'] for word in msg_list):
        return {"animation": "heartbroke", "msg": random.choice(bank['heartbroke_responses'])}

    elif any(word in bank['funny_words'] for word in msg_list):
        return {"animation": "giggling", "msg": random.choice(bank["funny_responses"]) + get_joke()}

    elif any(word in bank['dog_words'] for word in msg_list):
        return {"animation": "dog", "msg": random.choice(bank['dog_responses'])}

    elif any(word in bank['crying_words'] for word in msg_list):
        return {"animation": "crying", "msg": random.choice(bank['crying_responses'])}

    elif any(word in bank['bored_words'] for word in msg_list) or "quote".lower() in msg:
        return {"animation": "bored", "msg": random.choice(bank['bored_responses']) + get_quote()}

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
        now = str(datetime.datetime.now()) + emojis.encode(" :watch:")
        return {"animation": "ok", "msg": now}

    elif swear(msg_list):
        return {"animation": "confused", "msg": random.choice(bank["swear_responses"])}

    elif names(msg_list):
        return get_name_list_after_update()

    else:
        return {"animation": "inlove", "msg": random.choice(bank['default_responses'])}










