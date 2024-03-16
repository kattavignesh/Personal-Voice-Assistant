####################################################
__author__ = "VIGNESH"                              
__copyright__ = "Copyright (C) 2024 Author Vignesh" 
__license__ = "Public"                              
__version__ = "1.0"                                 
####################################################

################################
import sys
import pyttsx3
import wikipedia
import speech_recognition as sr
################################

voice = pyttsx3.init()
r = sr.Recognizer()
# Record the user's speech
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
    print("Recognizing...")
# Recognize the user's speech
try:
    In = r.recognize_google(audio)
except:
        print("Could not understand audio")
        sys.exit()
result = wikipedia.summary(In, sentences=4) 
print(result)
voice.say(result)
voice.runAndWait()
