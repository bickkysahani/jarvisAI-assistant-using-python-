import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishMe():
    speak("Welcome Back Sir!")
    
    time()
    
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("JARVIS at your service. Please tell me how can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1   #it will wait for 1 seconds then start listening
        audio = r.listen(source) #it will listen to our microphone

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #using google to recognize speech and passing the audio
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please!")
        return "None" 

    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gmail id',"password")
    server.sendmail('sender gmail id',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\MRROBOT\\Desktop\\jarvis\\s.png")

def cpu():
    usage = str(psutil.cpu_percent()) #typecasting the cpu percent to str and then assigning it to usage
    speak("CPU is at " + usage)
    battery = psutil.sensors_battery() #it returns a list about battery percent and list cant be typecasted
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())



if __name__ == "__main__":  #main function
    wishMe()               #whenever we will start our AI assistance, wishme function will execute once
    while True:            #program will run until quit() is called
        query = takeCommand().lower() #taking the command using takeCommand func and changing its case to lower and assigning it to query

        if "time" in query: #if the "time" string in found in query then it will call the time func
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","") #replaces "wikipedia" will blank in the query
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
        elif "send email" in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = 'bickkysahani@gmail.com'  
                sendEmail(to,content)
                speak("Email has been sent to "+str(to))
            except Exception as e:
                print(e)
                speak("Unable to send the email")
        elif "search in chrome" in query:
            speak("what should I search?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            speak("Here we go to Chrome!")
            wb.get(chromepath).open_new_tab(search+'.com')

        elif "search youtube" in  query:
            speak("what should I search?")
            search_Term = takeCommand().lower()
            speak("Here we go to Youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif "search google" in  query:
            speak("what should I search?")
            search_Term = takeCommand().lower()
            speak("Here we go to Google!")
            wb.open('https://www.google.com/search?q='+search_Term)

        elif "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /a /t 1")
        elif "restart" in query:
            os.system("restart /r /t 1")
        elif "play songs" in query:
            songs_dir = 'G:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        elif "remember that" in query:
            speak("What should I remember sir?")
            data = takeCommand()
            speak("You said me to remember that "+ data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember = open('data.txt','r')
            speak("you said me to remember that "+remember.read())
        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
        elif "offline" in query:
            speak("Going offline sir!")
            quit()
        elif "word" in query:
            speak("Opening MS Word.....")
            ms_word = r'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE'
            os.startfile(ms_word)

