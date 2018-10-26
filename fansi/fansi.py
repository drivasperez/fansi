# Fansi.py
"""
A library for easily adding colour, emphasis
and emojis to your terminal printouts.

By Daniel Rivas, 2018.
"""

import re
from colorama import init, deinit
from .data import AnsiCodes, EmojiCodes


def parse_emphasis(str, resetcode=AnsiCodes.reset()):
    """
    Italics with _tags_ or *tags*.
    Bold with __tags__ or **tags**.
    Bold and italic with ___tags___ or ***tags***
    """

    strong_emphasis = re.compile(
        r"(?<!\w)(_{3}|\*{3})(?!_)(.+?)(?<!_)\1(?!\w)")
    str = strong_emphasis.sub(
        AnsiCodes.form_code("bold italics") + r"\2" + AnsiCodes.reset() +
        resetcode, str)

    strong = re.compile(r"(?<!\w)(_{2}|\*{2})(?!_)(.+?)(?<!_)\1(?!\w)")
    str = strong.sub(
        AnsiCodes.form_code("bold") + r"\2" + AnsiCodes.reset() + resetcode,
        str)

    emphasis = re.compile(r"(?<!\w)(_{1}|\*{1})(?!_)(.+?)(?<!_)\1(?!\w)")

    str = emphasis.sub(
        AnsiCodes.form_code("italics") + r"\2" + AnsiCodes.reset() + resetcode,
        str)

    return str


def parse_inline_styles(str, resetcode=AnsiCodes.reset()):
    """
    ::red bg-blue bold::This text is affected::reset::This code is not.
    """

    tag_re = re.compile(r" (?<!\w)(:{2})(?!:)(.+?)(?<!:)\1(?!\w)")
    str = tag_re.sub(lambda match: check_for_end(match.group(2), resetcode),
                     str)

    return str


def check_for_end(str, resetcode):
    if str == "end":
        return AnsiCodes.reset() + resetcode
    else:
        return AnsiCodes.form_code(str)


def parse_emojis(str):
    """
    TODO: Parse emojis in the text.
    TODO: Syntax :emoji:
    """
    emoji_re = re.compile(r"(?<!\w)(:{1})(?!:)(.+?)(?<!:)\1(?!\w)")
    str = emoji_re.sub(lambda match: EmojiCodes.get_emoji(match.group(2)), str)
    return str


def format(str, codes=None):
    if codes is not None:
        reset = AnsiCodes.form_code(codes)
        str = parse_emphasis(str, reset)
        str = parse_inline_styles(str, reset)
        str = parse_emojis(str)
        str = AnsiCodes.form_code(codes) + str + AnsiCodes.reset()

    str = parse_emphasis(str)
    str = parse_inline_styles(str)
    str = parse_emojis(str)
    str = AnsiCodes.reset() + str + AnsiCodes.reset()

    return str


def say(str, codes=None):
    init()
    str = format(str, codes)
    print(str)
    deinit()


# --- Premade formats ---


def danger(str, emoji=True):
    """
    For urgent messages, e.g. error printouts.
    """
    say(str, "bold red")
