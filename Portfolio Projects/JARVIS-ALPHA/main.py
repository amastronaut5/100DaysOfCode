# Project J.A.R.V.I.S. - Alpha Build (MVP)

# === SETUP ===
# Requirements: openai, pyttsx3, whisper, speechrecognition, python-dotenv, requests
# (Install via pip: pip install openai pyttsx3 SpeechRecognition requests python-dotenv)

import os
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import requests

from dotenv import load_dotenv

# === LOAD ENV ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# === TEXT-TO-SPEECH ENGINE ===
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

# === SPEECH RECOGNITION ===
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there's a network issue.")
            return ""

# === GPT FUNCTION ===
def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"GPT Error: {str(e)}"

# === COMMAND FUNCTIONS ===
def tell_time():
    now = datetime.datetime.now()
    speak(f"Current time is {now.strftime('%I:%M %p')}")

def open_website(site):
    urls = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "github": "https://github.com"
    }
    if site in urls:
        speak(f"Opening {site}")
        webbrowser.open(urls[site])
    else:
        speak(f"I can't find the URL for {site}.")

def get_weather():
    try:
        city = "New Delhi"
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        data = response.json()
        condition = data['current']['condition']['text']
        temp = data['current']['temp_c']
        speak(f"The weather in {city} is {condition} and {temp} degrees Celsius.")
    except:
        speak("Sorry, I can't fetch weather data right now.")

# === MAIN LOOP ===
def main():
    speak("Hello sir, I am JARVIS, your AI assistant. How can I help you today?")
    while True:
        command = listen()

        if "time" in command:
            tell_time()
        elif "open" in command:
            site = command.split("open")[-1].strip()
            open_website(site)
        elif "weather" in command:
            get_weather()
        elif "exit" in command or "quit" in command:
            speak("Goodbye, sir.")
            break
        elif command:
            reply = ask_gpt(command)
            speak(reply)

if __name__ == "__main__":
    main()
