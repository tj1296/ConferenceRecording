import speech_recognition as sr

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:

    print('speak now')
    audio = r1.listen(source)

    print(r2.recognize_google(audio))