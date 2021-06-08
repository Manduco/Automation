import pyttsx3
engine = pyttsx3.init()  # object creation
""" RATE"""
engine.setProperty('rate', 180)  # setting up new voice rate
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  #printing current voice rate
"""VOLUME"""
volume = engine.getProperty(
    'volume')  #getting to know current volume level (min=0 and max=1)
print(volume)  #printing current volume level
engine.setProperty('volume', 1)  # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')  #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)

engine.say('Hello Armando, the time is 9 AM')
engine.runAndWait()
engine.stop()
"""Saving Voice to a file"""