
# python audio create #

from gtts import gTTS

txt_to_speech = gTTS(text="Lover Boy Tuhin", lang='en')
txt_to_speech.save('sample.mp3')






# python speech to text
import pyttsx3

my_message=''' please speak what you want: ''' 
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
engine.say('{}'.format(my_message))
engine.runAndWait()
#rate = engine.getProperty('rate')








