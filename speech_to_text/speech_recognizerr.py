import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        textW ="You said : {}".format(text)
        print(textW)
    except:
        print("Sorry could not recognize what you said")