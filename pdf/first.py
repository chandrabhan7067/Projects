import pyautogui as pyt
import pyttsx3 
import time
import speech_recognition as sr

def speak():
    engine = pyttsx3.init()
    engine.say("Ok i am listening")
    engine.runAndWait()
    
def save_pdf():
    pyt.keyDown('ctrl')
    pyt.press('s')

def Outer():
    pyt.click(80, 750)
    time.sleep(1)
    pyt.write('wordpad')
    time.sleep(1)
    pyt.keyDown('enter')
    time.sleep(1)
    pyt.click(500,250)

def Take_word():
    Outer()
    speak()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 3
        audio = r.listen(source)

        query = r.recognize_google(audio,language='en-in')
        pyt.write(query)
   
Take_word()