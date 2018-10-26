import fansi.fansi

fansi.say(
    "Fansi is a **Python library** that makes it __easy__ to mark-up your *terminal printouts*.",
    "noen")

fansi.say("You can add ::yellow:: colours ::end:: and ___emphasis___ inline.")

fansi.say("And you can also set global text settings.", "cyan italics")

fansi.say(":poop::beer::man::abcd: __bold text__ _italicised text_ ___bold and italicised text___")

# fansi.say("Here _is_some_demo_text_ and **this** should also ___work___")

# fansi.say("___This should also work, I think___ and be red", "red")

# fansi.say("_Hello?_ Does this __work__?", "blue")

# fansi.say("This is :heart_eyes: only formatted by the codes", "blue bold italics")

# fansi.say("Testing _testing_ **testing** ___testing___",
#           codes="bg-yellow magenta")

# fansi.danger("Oh no *oh boy* oh no no nononono")

# fansi.say("Just checking", "yellow")

# fansi.say("Is it ::bold:: detecting ::red:: this? ::end:: Looks like it!", "yellow italics")
