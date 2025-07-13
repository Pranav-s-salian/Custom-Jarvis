import datetime
import time
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pyautogui
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser






def intialize_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate",130)
    engine.setProperty("volume",70)
    return engine

def speak(text):
    engine = intialize_engine()
    engine.say(text)
    engine.runAndWait()




import speech_recognition as sr
import whisper
import speech_recognition as sr

def voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening....")
        r.pause_threshold = 0.8
        r.phrase_threshold = 0.1
        r.sample_rate = 16000
        r.dynamic_energy_threshold = True
        r.operation_timeout = None
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment_damping = 0.15
        r.energy_threshold = 300
        r.phrase_time_limit = None
        audio = r.listen(source)

    
    file_name = "audio.wav"
    with open(file_name, "wb") as f:
        f.write(audio.get_wav_data())

    try:
        print("recognizing.....")
        
        model = whisper.load_model("base") 
        result = model.transcribe(file_name)
        query = result['text']
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "none"
    
 
def get_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1:"Monday",
        2:"tuesday",
        3:"wednesday",
        4:"thursday",
        5:"friday",
        6:"saturday",
        7:"sunday"
    }
    
    if day in day_dict.keys():
        day_week = day_dict[day]
        print(day_week)
        return day_week
        
        
    
    
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = get_day()
    if (hour >=0) and (hour <=12) and ('AM in t'):
        speak(f"good morning boss, it's{day} and the time is {t}")
    elif (hour >=12) and (hour <=16) and ('PM in t'):
        speak(f"good afternoon boss, it's{day} and the time is {t}")
    else:
        speak(f"good evening boss, it's{day} and the time is {t}")
        
        
def open_media(command):
    
    if 'facebook' in command:
     speak("opening your facebook sir")
     webbrowser.open("https://www.youtube.com/results?search_query=hbfs+line+follower")
    elif 'whatsapp' in command:
        speak("opening your whatsapp sir ")
        webbrowser.open ("https://www.whatsapp.com/")
    elif 'google' in command:
        speak("opening google sir")
        webbrowser.open("https://www.google.com/")
    elif 'gmail' in command:
        speak("opening your gmail sir")
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    else:
        speak("not found")
        
        
        



        
def my_tabel(command):
    day = get_day().lower()
    tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%A").lower()
    week = {
        "monday":"heavay",
        "tuesday":"n",
        "wednesday":"aii",
        "thursday":"oiii",
        "friday":"bii",
        "saturday":"hehehehehe",
         "sunday":"hy",
        
    }
    if 'today' in command:
        speak("todays schedule is sir")
        if day in week.keys():
            speak(week[day])
    elif 'tommorow' in command:
        speak("tommorows schedule is sir")
        if tomorrow in week.keys():
           speak(f"tommmorow is {tomorrow} and tommorows schedule is {week[tomorrow]}" )
            
    
    
def press_keys(keys):
    for key in keys:
        pyautogui.keyDown(key)
    for key in reversed(keys):
        pyautogui.keyUp(key)
    
def opencalc(command):
    if "open caluclator" in command:
        speak("opening arduino ide")
        os.startfile("c:\\Users\\prana\\AppData\\Local\\Programs\\Arduino IDE\\Arduino IDE.exe")
    elif("close caluclator" in command):
        speak("closing calucator")
        os.startfile("task kill /f/im arduino.ide")
    else:
        speak("sorry didn,t recognize it can you tell me once again")
        
def model(text):
    llm = ChatOllama(model="llama3.2")
    output = StrOutputParser()
    chain = llm|output
    respone = chain.invoke(text)
    speak(respone)
    
    
     
    
        

if __name__ == "__main__":
   """ wishme()"""
while True:
        query  = input("enter any ")
        if ("facebook" in query) or ("discord" in query)  or ("google" in query) or ("gmail" in query):
            print("facenook")
            open_media(query)   
        elif ("today " in query) or ("tommorow" in query):
          my_tabel(query)
        elif ("volume up" in query) or ("increase volume" in query):
         pyautogui.press("volumeup")
         speak("increasing volume sir")
        elif ("volume down" in query) or ("decrease volume" in query):
          pyautogui.press("volumedown")
          speak("decreasing volume sir")
        elif ("mute it" in query) or ("mute" in query):
         speak("muting  volume sir")
         pyautogui.press("volumemute")
        elif ("unmute it" in query) or ("unmute" in query):
         pyautogui.press("volumeunmute")
         speak("unmuted sir")
        elif ("increase keyboard light" in query) or ("backlit on" in query):
            speak("increasein brithness of the key sir")
            press_keys(['FN', 'up'])
        elif ("open caluclator" in query)  or ("close caliclator" in query):
            opencalc(query)
        elif ("wish me " in query) or ("time" in query):
            wishme()
        else:
            model(query)
        
        
        
        
        
           
        