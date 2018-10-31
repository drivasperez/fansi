# Fansi.py
"""
A library for easily adding colour, emphasis
and emojis to your terminal printouts.

By Daniel Rivas, 2018.
"""

import re
from colorama import init, deinit
from .data import AnsiCodes, EmojiCodes


def parse_emphasis(body, resetcode=AnsiCodes.reset()):
    """
    Italics with _tags_ or *tags*.
    Bold with __tags__ or **tags**.
    Bold and italic with ___tags___ or ***tags***
    """

    strong_emphasis = re.compile(r"(?<!\w)(_{3}|\*{3})(?!_)(.+?)(?<!_)\1(?!\w)")
    body = strong_emphasis.sub(
        AnsiCodes.form_code("bold italics") + r"\2" + AnsiCodes.reset() + resetcode,
        body,
    )

    strong = re.compile(r"(?<!\w)(_{2}|\*{2})(?!_)(.+?)(?<!_)\1(?!\w)")
    body = strong.sub(
        AnsiCodes.form_code("bold") + r"\2" + AnsiCodes.reset() + resetcode, body
    )

    emphasis = re.compile(r"(?<!\w)(_{1}|\*{1})(?!_)(.+?)(?<!_)\1(?!\w)")

    body = emphasis.sub(
        AnsiCodes.form_code("italics") + r"\2" + AnsiCodes.reset() + resetcode, body
    )

    return body


def parse_inline_styles(body, resetcode=AnsiCodes.reset()):
    """
    ::red bg-blue bold:: This text is affected ::end:: This code is not.
    """

    tag_re = re.compile(r"(^| )(?<!\w)(:{2})(?!:)(.+?)(?<!:)\2(?!\w)")
    body = tag_re.sub(lambda match: check_for_end(match.group(3), resetcode), body)

    return body


def check_for_end(body, resetcode):
    if body == "end":
        return AnsiCodes.reset() + resetcode
    else:
        return AnsiCodes.form_code(body)


def parse_emojis(body):
    """
    Parse emojis in the text.
    Syntax :poo: :lion: :multiple::emojis::together:
    """
    emoji_re = re.compile(r"(?<!\w)(:{1})(?!:)(.+?)(?<!:)\1(?!\w)")
    body = emoji_re.sub(lambda match: EmojiCodes.get_emoji(match.group(2)), body)
    return body


def format(body, codes=None):
    if codes is not None:
        reset = AnsiCodes.form_code(codes)
        body = parse_emphasis(body, reset)
        body = parse_inline_styles(body, reset)
        body = parse_emojis(body)
        body = AnsiCodes.form_code(codes) + body + AnsiCodes.reset()

    else:
        body = parse_emphasis(body)
        body = parse_inline_styles(body)
        body = parse_emojis(body)
        body = AnsiCodes.reset() + body + AnsiCodes.reset()

    return body


def say(body, codes=None):
    init()
    body = format(body, codes)
    print(body)
    deinit()


# --- Premade formats ---


def danger(body, emoji=True):
    """
    For urgent messages, e.g. error printouts.
    """
    say(body, "bold red")
