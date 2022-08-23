""" Assistant that can: respond to voice commands; interpret mathematical functions; plot mathematical functions"""

import tkinter as tk
from tkinter import ttk

import speech_recognition as sr
import matplotlib.pyplot as plt

import webbrowser


def plotter(function, variables=None, x_axis=None, y_axis=None, color=None):
    print(f'Plotting function: {function}...')
    variable = 
    plt.plot(variable, function)
    


r = sr.Recognizer()

def record_audio():
    """Records audio and recognizes what should be done with the command.
    """
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=0.6)
        
        try:
            text = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            print('Sorry I did not get that')

        return text.split()

command = record_audio()

if command[0] == 'computer': #Recognize the computer is adressed.
    print("How can I help you?")

    command = record_audio()
    for index, element in enumerate(command):

        if element == 'plot': 
            if command[index+1] == 'function':
                plotter(command[index+2:])
            else:
                plotter(command[index+1:])
        if element == 'function':
            plotter(command[index+1:])

        if element == 'open':
            print("What application would you like me to open?")
            command = record_audio()



        


