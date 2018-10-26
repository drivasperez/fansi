# data.py
import json
from os import path

class AnsiCodes:
    """
    Every Ansi Code for formatting text.
    """

    codes = {
        "reset": 0,
        "bold": 1,
        "italics": 3,
        "underline": 4,
        "blink": 5,
        "reverse": 7,
        "invisible": 8,
        # --- Foreground Colors ---
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
        # --- Background Colors ---
        "bg-black": 40,
        "bg-red": 41,
        "bg-green": 42,
        "bg-yellow": 43,
        "bg-blue": 44,
        "bg-magenta": 45,
        "bg-cyan": 46,
        "bg-white": 47,
    }

    @classmethod
    def form_code(cls, options):
        options = set(options.strip().split(" "))
        ansis = []
        for option in options:
            try:
                ansis.append(str(cls.codes[option]))
            except KeyError:
                continue
        if not ansis:
            ansis = ["0"]
        ansi_string = "\033[" + ";".join(ansis) + "m"
        return ansi_string

    @classmethod
    def reset(cls, options=""):
        return cls.form_code("reset" + options)


class EmojiCodes:
    """
    Every Unicode emoji code.
    """
    emojipath = path.join(path.dirname(__file__), 'emojis.json')
    with open(emojipath, "r") as data:
        emojis = json.load(data)

    @classmethod
    def get_emoji(cls, code):

        for emoji in cls.emojis['emojis']:
            # shortcode is ':shortcode:', our code is 'code', so take off
            # first and last chars.
            if emoji["shortname"][1:-1] == code:
                return emoji["emoji"]

        for emoji in cls.emojis['emojis']:
            if emoji["name"] == code:
                return emoji["emoji"]

        return("")


