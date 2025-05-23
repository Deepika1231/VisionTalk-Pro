# utils/voice_assistant.py
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import uuid

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = f"temp_{uuid.uuid4()}.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("Speech synthesis error:", e)

def transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
