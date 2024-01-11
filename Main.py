import speech_recognition as sr
import pyttsx3
import requests
import datetime
import webbrowser
from googletrans import Translator

# initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# define a function to recognize speech and return the text
def recognize_speech():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print(f"Request error: {e}")

# define a function to perform arithmetic operations
def arithmetic_operation():
    speak("Which operation do you want to perform?")
    operation = recognize_speech()

    speak("Enter the first number.")
    num1 = float(recognize_speech())

    speak("Enter the second number.")
    num2 = float(recognize_speech())

    if operation == "addition":
        result = num1 + num2
        speak(f"The sum of {num1} and {num2} is {result}.")
    elif operation == "subtraction":
        result = num1 - num2
        speak(f"The difference between {num1} and {num2} is {result}.")
    elif operation == "multiplication":
        result = num1 * num2
        speak(f"The product of {num1} and {num2} is {result}.")
    elif operation == "division":
        result = num1 / num2
        speak(f"The quotient of {num1} and {num2} is {result}.")
    else:
        speak("Invalid operation. Please try again.")

# define a function to perform logical operations
def logical_operation():
    speak("Which logical operation do you want to perform?")
    operation = recognize_speech()

    speak("Enter the first value.")
    value1 = bool(recognize_speech())

    speak("Enter the second value.")
    value2 = bool(recognize_speech())

    if operation == "and":
        result = value1 and value2
        speak(f"The result of {value1} and {value2} is {result}.")
    elif operation == "or":
        result = value1 or value2
        speak(f"The result of {value1} or {value2} is {result}.")
    elif operation == "not":
        result = not value1
        speak(f"The negation of {value1} is {result}.")
    else:
        speak("Invalid operation. Please try again.")

# define a function to perform tasks based on user input
def perform_task():
    speak("What task do you want me to perform?")
    task = recognize_speech()

    if "arithmetic" in task:
        arithmetic_operation()
    elif "logic" in task:
        logical_operation()
    elif "weather" in task:
        city_name = input("Enter the name of the city: ")
        url = f"https://wttr.in/{city_name}?format=%C\n%t\n%A\n"
        response = requests.get(url)
        speak(response.text)
    elif "time" in task:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "search" in task:
        speak("What do you want me to search for?")
        query = recognize_speech()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    elif "translate" in task:
        speak("What text do you want me to translate?")
        text = recognize_speech()
        speak("What language do you want to translate it to?")
        language = recognize_speech()
        translator = Translator()
        translation = translator.translate(text, dest=language)
        speak(translation.text)
    else:
        speak("Sorry, I don't know how to do that.")

# start the voice assistant
speak("Hi, I'm your voice assistant. How can I help you?")
while True:
    perform_task()
    speak("Do you want me to perform another task?")
    response = recognize_speech()
    if "no" in response:
        speak("Goodbye!")
        break
