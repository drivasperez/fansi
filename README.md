# Fansi
Fansi is a Python library that makes formatting, colouring and adding emojis to terminal printouts easy.

# Installation

`pip install fansi`

To uninstall: `pip uninstall fansi`

# Usage

First: `from fansi import fansi`

Then, instead of `print()` statements, use `fansi.say()`

`fansi.say("This string can have fansi formatting!")`

To add italics, use `_tags_` or `*tags*`. To add bolding, use `__tags__` or `**tags**`. To add bolding and italics, use `___tags___` or .

For example: `fansi.say("This _text will be italicised. __This text will be **bolded**. ___This text will be both___")`

You can add any Ansi formatting tags inline, using `::tags::` To reset the formatting, use the `::end::` tag.

For example: `fansi.say("This text will be normal. ::green bold italics:: This text will be green, bold and italicised. ::end:: This text will be back to normal.")`

Ansi tags can also be added to the entire string.

For example: `fansi.say("This text will be magenta on a green background.", "magenta bg-green")`

You can also emojis using `:tags:`. Long and shortnames work.

For example: `fansi.say("Here are some :poop: emojis! :panda_face::tiger:cat:")`'

That's it!
