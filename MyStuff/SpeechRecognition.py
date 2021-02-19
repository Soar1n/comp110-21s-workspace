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

for i in range(3):
    speech()





    