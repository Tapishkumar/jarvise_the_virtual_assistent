import speech_recognition
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import jokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import clint

from toolz.curried import take
from clint.textui import progress
from twilio.rest import Client
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as winc
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    houre = int(datetime.datetime.now().hour)
    if houre >= 0:
        if houre < 12:
            speak("Good morning sir !")

        elif houre >= 12 and houre < 12:
            speak("Good afternoon sir")

        else:
            speak("Good Evening sir !")
    elif houre >= 12 and houre < 12:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir !")

    assName = ("Ahri 1 point o")
    speak("I am your Assistant sir !")
    speak(assName)


def username():
    speak("What should I Call you sir !")
    uname = takeCommand()
    speak("Welcome mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#################".center(columns))
    print("Welcom Mr.", uname.center(columns))
    print("################".center(columns))

    speak("How can i Help you Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening.... ")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognize....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Unable to Recognized your voice')
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low sequrity in gmail

    server.login('your email id', 'your email password')
    server.sendmail('your email id ', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
    # this function will clean the unwanted things
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia ' in query:
            speak("Speaching wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Here you go to Youtube\n')
            webbrowser.open("youtube.com")
        elif 'open google ' in query:
            speak("here you go to Google\n")
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            speak("Here you go sir\n")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            speak("Here is your music sir")
            music_dir = "C:/Users/Tapish/Music/Video Projects"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' or ' what is time ' or 'time ' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif 'the date ' or ' what is today date ' in query :
            strdate = datetime.date.today().strdate("%Month:%Year")

        elif 'open chrom' in query:
            codepath = r"C:\\ProgramFiles\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)
        elif 'email to mom' in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak('email has been sent !:')
            except Exception as e:
                print(e)
                speak("I am not able to send this email ")
        elif 'how are you ' in query:
            speak("I am fine sir ")
            assName = query
        elif "change the name" in query:
            speak("What should You call me sir")
            assName = takeCommand()
            speak("thanks for naming me ")
        elif "what's your name" in query:
            speak("my friends calls me  ")
            speak(assName)
            print("my frinds call me ",assName)

        elif "what is your name" in query:
            speak(assName)
            print(f"my name is {assName}")
