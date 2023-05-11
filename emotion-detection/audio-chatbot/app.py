import speech_recognition as sr
import pyttsx3
import pywhatkit
from flask import Flask, render_template, request

listener = sr.Recognizer()
player = pyttsx3.init()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play_music", methods=["POST"])
def play_music():
    command = listen()
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
    return "success"

def listen():
    with sr.Microphone() as source:
        voice_content = listener.listen(source)
        text_command = listener.recognize_google(voice_content)
        print(text_command)
    return text_command.lower()

if __name__ == "__main__":
    app.run(debug=True)
