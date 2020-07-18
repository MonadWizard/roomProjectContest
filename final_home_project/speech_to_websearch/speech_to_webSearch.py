#python 3.6 need


####### start text to speech#############
import pyttsx3    # text to speech

my_message=''' please speak what you want: ''' 
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
engine.say('{}'.format(my_message))
engine.runAndWait()

####### end text to speech#############


####### start speech to text#############
import speech_recognition as sr   #speech to text
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

####### start speech to text#############





#################### web search ######################

import requests, sys, webbrowser, bs4


class web_search:
    
    def searchG(inpt):
        # res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))  #create request
        res = requests.get('https://google.com/search?q='+''.join(inpt))  #create request
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        linkElements = soup.select('.r a')
        linkToOpen = min(2, len(linkElements))  # HOW MENY LINKS YOU WANT TO OPEN
        for i in range(linkToOpen):
            webbrowser.open('https://google.com'+linkElements[i].get('href'))
        
        return (inpt)

web_search.searchG(textW)


