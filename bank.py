import emojis

three_monkeys = emojis.encode(" :hear_no_evil: :speak_no_evil: :see_no_evil:")
smile = emojis.encode(":smile:")
fish = emojis.encode(":tropical_fish:")
clock = emojis.encode(":clock1:")
bot = emojis.encode(":space_invader:")

bank = {  # responses list:
    "default_responses": ["Perhaps we can discuss another topic", emojis.encode(" I like that :thumbsup:"),
                          emojis.encode("Pretty cool :sunglasses:"), emojis.encode(" Dance for me ! :dancer:"),
                          " Although I'm pretty smart I'm really just a chatbot" + bot, "I'm here to help" + smile],

    "swear_responses": [emojis.encode("You should wash your mouth with some soap! :astonished:"),
                        emojis.encode("Please use clean language :underage:"),
                        "I don't speak Klingon , try typing in English" + three_monkeys,
                        " Looks like you have a typo" + three_monkeys,
                        emojis.encode("I'm not programmed for dirty language :unamused: "),
                        emojis.encode("Your mother wouldn't be happy with this :no_good:"),
                        "oopsi you slipped a dirty, lets re-phrase" + three_monkeys,
                        emojis.encode("I think you want to re-phrase :interrobang: ") ],

    "financial_responses": [emojis.encode("Show me the money! :moneybag:"), emojis.encode("Get a lotto ticket I've got a good feeling about this :money_with_wings:"),
                            emojis.encode("It's all about the money :dollar:"),
                            emojis.encode("If I were a rich man..la la la :musical_score:")],

    'no_responses': [emojis.encode("Let's try to be positive about this :dancer:"),
                     emojis.encode(" No ? How about YES:heavy_exclamation_mark:"), "Think happy thoughts"],

    "takeoff_responses": [emojis.encode("Ask my partner Google, he will be real useful for that one! :ok_hand:"),
                          emojis.encode("I'm not sure :ok_woman:"),
                          " figures..", "Why not?", " Pretty much", "You may want to ask some people as well",
                          "Can you try to rephrase?", "I had the same question my self",
                          "I suggest we change the subject", "mm, well what do you think?"],

    "dancing_responses": [emojis.encode("I think that's great! :clap:"), "Wonderful", "I have to agree on that",
                          "Yep!", "For sure!",
                          emojis.encode("Go Go Go! :checkered_flag:")],

    "crying_responses": [emojis.encode("Would a tissue help? :gift:"),
                         emojis.encode("Crying is a good way to let it out :sob:"),
                         emojis.encode("These tears should turn into tears of joy :sob: :joy:")],

    "bored_responses": [" That reminds me of a famous quote ", "What do you think about this quote?", " Famous quote: "],

    "afraid_responses": ['I\'m just a bot ' + bot, emojis.encode('Have no Fear :surfer:'),
                         emojis.encode('The entire world is a very narrow bridge :roller_coaster: and the important this is not to be afraid :muscle:'),
                         emojis.encode('Please do not feed the fears! :warning:')],

    "funny_responses": [emojis.encode("Ha, listen to this joke :laughing:: "), emojis.encode("Funny :laughing:"),
                        emojis.encode("I'm feeling ticklish, :baby: reminds me of a joke: "),
                        emojis.encode("You've got a great sense of humor! :smile:, so do I: ")],

    "waiting_responses": ["Patience is a virtue" + clock, "I've been waiting all my life" + clock],

    "inlove_responses": [emojis.encode("Love Love me Do :sparkling_heart:"),
                         emojis.encode("Love is in the air :two_hearts:"), emojis.encode(":heart:")],

    "heartbroke_responses": ["There are many fish in the sea" + fish, "Don't worry be happy" + smile,
                             emojis.encode(":broken_heart:"),
                             "Something good will happen soon, you'll see" + smile],

    "dog_responses": [" I love pets! I have a dog in my self as you can see", emojis.encode(" I'm a dog type :dog:"),
                      emojis.encode(":dog:"), emojis.encode(
            " I like many animals :dog: :cat: :fish: :mouse: :hamster: :rabbit: :wolf: :frog: :tiger: :koala:"
            ":bear: :cow: :boar: :monkey: :horse: :racehorse: :camel: :sheep: :elephant: :panda_face: ")],

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
