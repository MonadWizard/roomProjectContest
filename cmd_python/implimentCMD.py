import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        txt_l = text.lower()
        
    except:
        print("Sorry could not recognize what you said")




import subprocess

cmd_dic = {'file explorer':'explorer .', 'calculator':'calc .', 'notepad':'notepad .', 'character map':'charmap .', 'paint':'mspaint .',
 'command Prompt': 'cmd .', 'windows media player':'wmplayer .', 'task manager':'taskmgr .', 'chrome':'start chrome.exe'}

subprocess.call(cmd_dic[txt_l],shell=True)

# str_data = input("Enter Command : ")
# subprocess.call(cmd_dic[str_data],shell=True)

# subprocess.call('calc .',shell=True)
# subprocess.call('start chrome.exe',shell=True)




