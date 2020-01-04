import emojis

three_monkeys = emojis.encode(" :hear_no_evil: :speak_no_evil: :see_no_evil:")
smile = emojis.encode(":smile:")
fish = emojis.encode(":tropical_fish:")
clock = emojis.encode(":clock1:")
bot = emojis.encode(":space_invader:")
thumbsup = emojis.encode(":thumbsup:")
sunglasses = emojis.encode(":sunglasses:")
dancer = emojis.encode(":dancer:")
astonished = emojis.encode(":astonished:")
underage = emojis.encode(":underage:")
unamused = emojis.encode(":unamused:")
no_good = emojis.encode(":no_good:")
interrobang = emojis.encode(":interrobang:")
moneybag = emojis.encode(":moneybag:")
money_with_wings = emojis.encode(":money_with_wings:")
dollar = emojis.encode(":dollar:")
musical_score = emojis.encode(":musical_score:")
heavy_exclamation_mark = emojis.encode(":heavy_exclamation_mark:")
ok_hand = emojis.encode(":ok_hand:")
ok_woman = emojis.encode(":ok_woman:")
clap = emojis.encode(":clap:")
checkered_flag = emojis.encode(":checkered_flag:")
gift = emojis.encode(":gift:")
sob = emojis.encode(":sob:")
joy = emojis.encode(":joy:")
muscle = emojis.encode(":muscle:")
roller_coaster = emojis.encode("roller_coaster")
warning = emojis.encode(":warning:")
surfer = emojis.encode(":surfer:")
laughing = emojis.encode(":laughing:")
baby = emojis.encode(":baby:")
sparkling_heart = emojis.encode(":sparkling_heart:")
two_hearts = emojis.encode(":two_hearts:")
heart = emojis.encode(":heart:")
dog = emojis.encode(":dog:")
animals = emojis.encode(":dog: :cat: :fish: :mouse: :hamster: :rabbit: :wolf: :frog: :tiger: :koala:"
                        ":bear: :cow: :boar: :monkey: :horse: :racehorse: :camel: :sheep: :elephant: :panda_face:")


bank = {  # responses list:
    "default_responses": ["Perhaps we can discuss another topic", " I like that " + thumbsup,
                          "Pretty cool " + sunglasses, " Dance for me ! " + dancer,
                          " Although I'm pretty smart I'm really just a chatbot" + bot, "I'm here to help" + smile],

    "swear_responses": ["You should wash your mouth with some soap! " + astonished,
                        "Please use clean language" + underage,
                        "I don't speak Klingon , try typing in English" + three_monkeys,
                        " Looks like you have a typo" + three_monkeys,
                        "I'm not programmed for dirty language " + unamused,
                        "Your mother wouldn't be happy with this " + no_good,
                        "oopsi you slipped a dirty, lets re-phrase" + three_monkeys,
                        "I think you want to re-phrase " + interrobang],

    "financial_responses": ["Show me the money! " + moneybag,
                            "Get a lotto ticket I've got a good feeling about this " + money_with_wings,
                            "It's all about the money " + dollar,
                            "If I were a rich man..la la la " + musical_score],

    'no_responses': ["Let's try to be positive about this " + dancer,
                     " No ? How about YES"+heavy_exclamation_mark, "Think happy thoughts"],

    "takeoff_responses": ["Ask my partner Google, he will be real useful for that one! " + ok_hand,
                          "I'm not sure " + ok_woman,
                          " figures..", "Why not?", " Pretty much", "You may want to ask some people as well",
                          "Can you try to rephrase?", "I had the same question my self",
                          "I suggest we change the subject", "mm, well what do you think?",
                          "That's a great question, you should ask google"],

    "dancing_responses": ["I think that's great! " + clap, "Wonderful", "I have to agree on that",
                          "Yep!", "For sure!",
                          "Go Go Go! " + checkered_flag],

    "crying_responses": ["Would a tissue help? " + gift,
                         "Crying is a good way to let it out " + sob,
                         "These tears should turn into tears of joy " + sob + joy],

    "bored_responses": [" That reminds me of a famous quote ", "What do you think about this quote?",
                        " Famous quote: "],

    "afraid_responses": ['I\'m just a bot ' + bot, "Have no Fear " + surfer,
                         "The entire world is a very narrow bridge " + roller_coaster +
                         " and the important this is not to be afraid " + muscle,
                         "Please do not feed the fears! " + warning],

    "funny_responses": ["Ha, listen to this joke " + laughing, "Funny " + laughing,
                        "I'm feeling ticklish, " + baby + " reminds me of a joke: ",
                        "You've got a great sense of humor! " + smile + ", so do I: "],

    "waiting_responses": ["Patience is a virtue" + clock, "I've been waiting all my life" + clock],

    "inlove_responses": ["Love Love me Do " + sparkling_heart,
                         "Love is in the air " + two_hearts, heart],

    "heartbroke_responses": ["There are many fish in the sea" + fish, "Don't worry be happy" + smile,
                             "broken_heart", "Something good will happen soon, you'll see" + smile],

    "dog_responses": [" I love pets! I have a dog in my self as you can see", " I'm a dog type " + dog,
                      dog, " I like many animals " + animals],

    # trigger list:
    'time_list': ["time", "date", "zone", "hour", "minute", "hours", "minutes", "seconds", "hr", "min", "sec"],

    'no_words': ["no", "not", "negative", "nobody", "unhappy", "none"],

    'crying_words': ["cry", "crying", "weep", "weeping", "sob", "tear", "sobbing", "tears"],

    'bored_words': ["bored", "boredom", "disinterested", "fatigued", "tired", "dull",
                    "inattentive", "sick", "tired", "spiritless"],

    'afraid_words': ['boo', 'scare', 'scared', 'fright', 'frighten', 'afraid', 'terrified', 'fear', 'roar', 'scream'],

    'funny_words': ["laugh", "laughing", "hilarious", "joke", "jokes", "funny", "chuckle", "giggle", "howl", "snicker",
                    "burst", "bursting", "crackup", "cracking", "humor"],

    'waiting_words': ["await", "delay", "expect", "hanging", "hang", "linger",
                      "remain", "standby", "stay", "stick", "stall", "hold back"],

    'inlove_words': ["love", "kiss", "kissing", "hugs", "hug", "hugging", "in love", "loving", "him", "her", "family",
                     "son", "daughter"],
    'heartbroke_words': ["heart", "heart broken", "broke my heart"],
    'dog_words': ["pets", "pet", "dog", "animals", "cat", "cats", "parrot", "parrots", "hamster"],
}

