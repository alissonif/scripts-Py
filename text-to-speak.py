# from gtts import gTTS
# import os

# text = input("Enter the text to be read: ")
# tts = gTTS(text=text, lang='en')
# tts.save("read_text.mp3")
# os.system("start read_text.mp3")

import pyttsx3

engine = pyttsx3.init()
text = input("Enter the text to be read: ")
engine.say(text)
engine.runAndWait()
 