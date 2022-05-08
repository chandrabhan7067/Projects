# from math import trunc
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')    

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak('Good mornig sir')

    elif hour>=12 and hour<16:
        Speak('Good afternoon')

    else:
        Speak('Good evening')
    Speak('I am google assistance can i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening........')
        r.pause_threshold = 1
        # r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said:{query}\n')

    except Exception as e:
        # print(e)
        print('say that again')
        return 'None'
    return query

if __name__ == '__main__':
    wish()
    # while True:
    if 1:
        query =  takeCommand().lower()

        if "wikipedia" in query:
            Speak('Searching wikipedia......')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            Speak('Accodind to wikipedia.')
            Speak(result)

        elif "open you tube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"The time is {strtime}")
            
        elif "open code" in query:
            webbrowser.open("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")