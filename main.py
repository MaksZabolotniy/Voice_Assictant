# Import all required modules
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from pyowm import OWM
from pyowm.utils.config import get_default_config

# Initialize the pyttsx3 module
start = pyttsx3.init()

hello = 'Здраствуйте, как мне вас называть?'   # Greet the user and ask for their name
start.say(hello)
start.runAndWait()
my_name = input(hello)
start.say(f'Хорошо, {my_name}')
start.runAndWait()

def listen():   # Define a function to listen for user input using speech recognition module
    r = sr.Recognizer()     # Initialize the speech recognition module
    with sr.Microphone() as source:     # Start the microphone and adjust for ambient noise
        print(f'Жду вопроса, {my_name}')
        r.pause_threshold = 1 # stop
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)    # Listen for audio input from the microphone
        try:    # Try to recognize the audio input
            task = r.recognize_google(audio, language="ru-RU").lower()
            print(task)
        except:     # If no audio is recognized, prompt user to try again
            task = listen()
        return task     # Return the recognized audio as a string     return task
                        # Define a function to process user requests
def requst(task):    # This line of code initializes a list of tasks that the program can do task = ["создать папку", "переименуй только что созданную папку", "погода", "поиск в интернете"]
    name_folder = 'new folder'
    name_folder2 = name_folder
    if "пока" in task:
        text = "Досвидания"
        start.say(text)
        start.runAndWait()
        quit()
        # If user says "goodbye", quit program
    if "создай папку на рабочем столе" in task:
        txt = "Выполняю"
        start.say(txt)
        start.runAndWait()
        os.mkdir(f'C:/Users/Admin/Desktop/{name_folder}')
        # If user requests to create a folder on desktop, do so
    if "переименуй только что созданную папку" in task:
        ext = "На какое имя хотите переименовать?"
        start.say(ext)
        start.runAndWait()
        new = input()
        os.rename(f'C:/Users/Admin/Desktop/{name_folder2}', f'C:/Users/Admin/Desktop/{new}')
        # If user requests to rename newly created folder, do so
    if "погода" in task:

        config_dict = get_default_config()  # Инициализация get_default_config()
        config_dict['language'] = 'ru'  # Установка языка
        city_name = "Введите ваш город"
        start.say(city_name)
        start.runAndWait()
        place = input("Введите ваш город: ")  # Переменная для записи города
        code_of_the_country = "Введите код вашей страны"
        start.say(code_of_the_country)
        start.runAndWait()
        country = input("Введите код вашей страны: ")  # Переменная для записи страны/кода страны
        country_and_place = place + ", " + country  # Запись города и страны в одну переменную через запятую

        owm = OWM('2baccc8dde391cff0003273e68813ea8')  # Ваш ключ с сайта open weather map
        mgr = owm.weather_manager()  # Инициализация owm.weather_manager()
        observation = mgr.weather_at_place(country_and_place)
        # Инициализация mgr.weather_at_place() И передача в качестве параметра туда страну и город

        w = observation.weather

        status = w.detailed_status  # Узнаём статус погоды в городе и записываем в переменную status
        w.wind()  # Узнаем скорость ветра
        humidity = w.humidity  # Узнаём Влажность и записываем её в переменную humidity
        temp = w.temperature('celsius')['temp']  # Узнаём температуру в градусах по цельсию и записываем в переменную temp
        start.say("В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
                  "Температура " + str(
                round(temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
                  "Влажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
                  "Скорость ветра " + str(w.wind()['speed']) + " метров в секунду")  # Узнаём и выводим скорость ветра
        start.runAndWait()

        print("В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
                  "\nТемпература " + str(
                round(temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
                  "\nВлажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
                  "\nСкорость ветра " + str(w.wind()['speed']) + " метров в секунду")  # Узнаём и выводим скорость ветра
    elif "поиск в интернете" in task:   # search goggle
        tex = 'Введите ваш запрос: '
        start.say(tex)
        start.runAndWait()
        q = input(tex)
        webbrowser.open('https://www.google.com/search?q=' + q)
    elif "открой фриланс сайт" in task:
        fivver = 'Выполняю'
        start.say(fivver)
        start.runAndWait()
        webbrowser.open('https://www.fiverr.com/')
    elif "открой github" in task:
        github = 'Выполняю'
        start.say(github)
        start.runAndWait()
        webbrowser.open('https://github.com/')
while True:
    requst(listen())