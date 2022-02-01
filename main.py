# Our main file.

import speech_recognition as sr

# Criar um reconhecedor
r = sr.Recognizer()

#Abrir o microfone para captura
with sr.Microphone() as soure:
    while True:
        audio = r.listen(soure) # Define microfone como fonte de áudio

        print(r.recognize_google(audio, language='pt'))