import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
print("package installed")

engine = pyttsx3.init('sapi5')   #pip install pyttsx3==2.71
voices = engine.getProperty("voices")

#print(voices[1].id)    #1---girl voice, 0----male voice

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=1 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Saaki here, Please tell me how may I help you")


def takeCommand():
    #it takes microphone input from user and returns string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio) # language='en-in')
        print("user said:", query)

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f = open('dataFile.txt','r')
    pwd = f.readline()

    server.login("xyz@gmail.com",pwd)
    f.close()
    server.sendmail("xyz@gmail.com", to, content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query =takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/search?q=how+to+vote+%23India&oi=ddle&ct=india-elections-2019-6233477951782912-l&hl=en&source=doodle-ntp&ved=0ahUKEwiQna6I8-XhAhWT4nMBHRt9DwsQPQgB")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\music'           #path of music folder
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'thank you' in query:
            speak("you are welcome, ma'am")

        elif 'email to xyz' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "xyzv@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend xyz. I am not able to send this email ")


        elif 'tata' in query:
            speak("Thank you for your time, xyz. See you next time")
            quit()
