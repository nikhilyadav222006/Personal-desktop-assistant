import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("Voice selected:", voices[1].id) 
engine.setProperty('voice', voices[0].id) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Hey! Good morning.")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I'm Algo, your assistant. How can I help today?")

def listen():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recog.pause_threshold = 1
        audio = recog.listen(source)

    try:
        print("Figuring out what you said...")
        query = recog.recognize_google(audio, language='en-in')
        print("You said:", query)
    except Exception as e:
        print("Didn't catch that. Can you try again?")
        return "None"
    
    return query.lower()

def run_task(query):
    if 'wikipedia' in query:
        speak("Let me check Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            print(result)
            speak(result)
        except:
            speak("Hmm... that was tricky. Try something more specific maybe?")

    elif 'open youtube' in query:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif 'open stack overflow' in query:
        speak("Heading to Stack Overflow.")
        webbrowser.open("https://stackoverflow.com")

    elif 'time' in query:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"It's {now}")

    elif 'open code' in query:
        path = "C:\\Users\\nikhi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Launching Visual Studio Code...")
        os.startfile(path)

    elif 'open spotify' in query:
        spotify = "C:\\Users\\nikhi\\AppData\\Roaming\\Spotify\\Spotify.exe"
        speak("Opening Spotify for you.")
        os.startfile(spotify)

    else:
        speak("Umm... I didn't quite get that.")

if __name__ == "__main__":
    greet()
    command = listen()
    if command != "None":
        run_task(command)
