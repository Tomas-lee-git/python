"""
    1. libraries
        1). cowsay;
        2). pyttsx3:
            i. action: python text-to-speech;
            ii. install: pip install py3-tts;
            iii. use:
                import pyttsx3
                engine = pyttsx3.init()
                engine.say("I will speak this text")
                engine.runAndWait()
"""

import cowsay
import pyttsx3

engine = pyttsx3.init("dummy") # initialize the library for text to speech

this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
