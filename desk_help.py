from ntpath import join
import random
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import json


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  

    speak("I am andy Sir. Please tell me how may I help you")  
    print("I am andy Sir. Please tell me how may I help you")     

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        
        print(f"{query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query
f=open("C://Users//rishabh//Documents//pass.txt","r")
x=f.readline()

   
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('therishabhgarg222@gmail.com',x)
    server.sendmail('therishabhgarg222@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print("According to Wikipedia")
            print(results)
            speak(results)
        elif 'good' in query:
            speak('thank you, my pleasure')
            print('thank you, my pleasure')
        elif 'open youtube' in query:
            speak('what to watch')
            print('what to watch')
            query = takeCommand().lower()
            webbrowser.open('https://youtube.com/results?search_query='+''+join(query))

        elif 'open google' in query:
            speak('what to search')
            print('what to search')
            query = takeCommand().lower()
            webbrowser.open('https://google.com/search?q='+''+join(query))

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C://Users//rishabh//Music'
            songs = os.listdir(music_dir) 
            z=(0,2,3,4,5,6)
            x=random.choice(z)
            os.startfile(os.path.join(music_dir, songs[x]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            print(strTime) 
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C://Users//rishabh//Desktop//Desktop assistant//Microsoft VS Code/_/Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rishabhgarg045@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")    
        elif 'game' in query:
            speak("lets play rock paper scissors ,what's your choice ")
            print("lets play rock paper scissors ,what's your choice ")
            ab = takeCommand().lower()
            game=('rock','paper','scissors')
            ac=random.choice(game)
            speak("i will go with : "+ac)
            print("i will go with : "+ac)
            if ac==ab:
                speak("it's a tie")
                print("it's a tie")
            elif ac=="rock" and ab=="paper":
                speak("you won sir,well played")
                print("you won sir,well played")
            elif  ac=="rock" and ab=="scissors":
                speak('I won sir,well played')
                print('I won sir,well played')
            elif  ac=="paper" and ab=="rock":
                speak('I won sir,well played')
                print('I won sir,well played')
            elif  ac=="scissors" and ab=="paper":
                speak('I won sir,well played')
                print('I won sir,well played')
            elif ac=="paper" and ab=="scissors":
                speak("you won sir,well played")
                print("you won sir,well played")
            elif ac=="scissors" and ab=="rock":
                speak("you won sir,well played")
                print("you won sir,well played")
        elif 'open resume' in query:
            speak('opening resume on calyxpod')
            print('opening resume on calyxpod')
            webbrowser.open('https://mitwpu.calyxpod.com/t6ZqCC/profile')
        elif 'read news' in query:
            print("Which Country's news headline should I read ?")
            speak("Which Country's news headline should I read ?")
            query1 = takeCommand().lower()
            if 'india' in query1:
                a="India"
                r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0b28eb3be49747eca2d97129e5b1cb2c')
            if 'america' in query1:
                a="America"
                r=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=0b28eb3be49747eca2d97129e5b1cb2c')
            if 'britain' in query1:
                a="Great Britain"
                r=requests.get('https://newsapi.org/v2/top-headlines?country=gb&apiKey=0b28eb3be49747eca2d97129e5b1cb2c')
            data=json.loads(r.content)
            speak("How many Headlines should I read ?")
            print("How many Headlines should I read ?")
            query1 = takeCommand().lower()
            query = int(query1)

            for i in range(query):
                if i==0:
                    print("TOP "+str(query)+" NEWS HEADLINES FROM "+a+" ARE : ")
                    speak("TOP "+str(query)+" NEWS HEADLINES FROM "+a+" ARE : ")

                news=data['articles'][i]['title']
                print("News ",i+1,":",news)
                speak(i+1)
                speak(news)

            speak("which news should I read in detail")
            print("which news should I read in detail")
            while True:
                    query1 = takeCommand().lower()
                    
            
                    if  "that's it" in query1:
                        print("it was fun reading news for you sir, Thank you!")
                        speak("it was fun reading news for you sir, Thank you!")
                        break
                    query = int(query1)
                    news1=data['articles'][query-1]['title']
                    news2=data['articles'][query-1]['description']
                    news=("%s - %s"%(news1,news2))
                    print("News in detail is :",news)
                    speak(news)
                                       
                    speak("which news next ?")
                    print("which news next ?")
        elif "stop" in query:
            speak("okay sir , have a good day")
            print("okay sir , have a good day")
            break
