import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import time

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def open_address(addre): 
    if 'sir'in addre:
        return 'sir'
    elif 'madam' in addre:
        return 'madam'   

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak ("Good Morning "+ address ) 

    elif hour>= 12 and hour <18:
        speak("Good Afternoon "+ address )
    
    else:
        speak("Good Evening "+ address)

    speak("How can I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1.3
        r.energy_threshold=300
        audio= r.listen(source)
    
    try:
        print("Recognizing.....")
        word = r.recognize_google(audio , language='en-in').lower()
        print("User said:"+ word)

    except:
        print("Not able to hear you, Can you please repeat?")
        time.sleep(2) 
        return "None"
    
    return word

def open_wikipedia(word):
    speak("Searching " + word + " in wikipedia .....")
    print("Searching  Wikipedia.....please wait")
    word=word.replace("wikipedia","")
    results= wikipedia.summary(word,sentences=2)
    print(results)
    speak("Acccording to Wikipedia")
    speak(results)
        
def open_youtube(word):
    webbrowser.open("https://www.youtube.com")
    speak("Opening youtube.....")
    speak("What would you like to search "+ address +"....")
    new_word= takeCommand()
    if new_word=="None":
        speak("Sorry "+address+ "!! not able to search")
    else:
        open_vid(new_word)

def open_google(word):
    webbrowser.open("https://www.google.com")
    time.sleep(2)
    speak("Opening Google.......")
    speak("What would you like to search "+ address +"....")
    new_word= takeCommand()
    if new_word=="None":
        speak("Sorry "+address+ "!! not able to search")
    else:
        open_search(new_word)

def play_music(word):
    music_dir='C:\\Users\\manoj\\AppData\\Roaming\\Spotify\\Spotify.exe'
    os.startfile(music_dir)   
    speak("Opening Spotify.....") 

def open_search(word):
    if 'search' in word:
        word= word.replace('search',"")
    else:
        word=word.replace('define',"")
    if word == "":
        return "sorry"
    speak("Searching " + word + " .....")
    results= webbrowser.open("https://www.google.com/search?q=meaning+of "+ word )
    try:
        speak(""+address +"!!! would you like me to tell its meaning")
        command= takeCommand()
        time.sleep(3) 
        if 'yes'in command:
            open_wikipedia(word)
            return "None"
        else:
            speak("Ok "+address)
            return "None"
    except:
        speak("Sorry "+ address +", I am unable to find its meaning in wikipedia...")
        return "None"

def open_vid(word):
    if 'search' in word:
        word= word.replace('search',"")
    else:
        word=word.replace('define',"")
    if word == "":
        return "sorry"
    speak("Opening " + word + " .....")
    results= webbrowser.open("https://www.youtube.com/search?q= "+ word )

def cant_process(word):
    if not'sorry' in word:
        whats_next()
    else:
        speak("Sorry!! Unable to process this task " + address +"..")
        whats_next()

def whats_next():
    time.sleep(2)
    speak("what would you like me to do next?")
    
if __name__ == '__main__':
    speak("Welcome to Desktop Assistant...")
    speak("I am Groot")
    print("How would you like me to address you? By Sir or By Madam")
    speak("How would you like me to address you? By Sir.... or By Madam...")    
    addre=takeCommand().lower()
    if 'sir' in addre or 'madam' in addre:
        address=open_address(addre)
    else:
        address='sir'
    
    wishme()
    
    while True:
        word =takeCommand().lower()
        
        if 'wikipedia' in word:
            open_wikipedia(word)
            whats_next()

        
        elif 'open youtube' in word:
            open_youtube(word)
            whats_next()

        
        elif 'open google' in word:
            open_google(word)
            whats_next()

            
        elif 'play music' in word or 'open spotify' in word:
            play_music(word)
            whats_next()      


        elif 'search' in word or 'define' in word:
            word=open_search(word)
            cant_process(word)
            

        elif 'goodbye' in word or 'good bye' in word: 
            speak("Good bye "+address+"!!, Have a good day")
            break
        

        elif 'thank you'in word or 'thankyou' in word:
            speak("You are Welcome....... ,Have a good day "+ address +"")
            break

        elif word=='open':
            speak("Sorry "+ address +", Can you please specify the command ")        