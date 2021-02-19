# pip install pipwin
# pipwin install pyaudio
# pip install SpeechRecognition

# python -m speech_recognition to test it out

import speech_recognition as sr

def speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
#    sr.Microphone() can also be a audio file
        print("Speak Anything  :  ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except:
            print("Sorry I could not recognize your voice...")
# This will only repeat 3 times to ensure we don't waste memory but it can go forever if we wanted it to or possibly until the end of a zoom call. 
for i in range(3):
    speech()







    