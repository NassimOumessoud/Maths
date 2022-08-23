""" Assistant that can: respond to voice commands; interpret mathematical functions; plot mathematical functions"""

import tkinter as tk
from tkinter import ttk

import speech_recognition as sr
import matplotlib.pyplot as plt
import numpy as np

import webbrowser


def plotter(function, start=-10, stop=10, steps=100, color=None):
    translator = {'^': '**'}
    parameters = {'from': start, 'to': stop, 'steps': steps, 'color': color}

    for index, element in enumerate(function):
        if element in translator.keys():
            function[index] = translator[element]
    print("Would you like to specify parameters?")
    command = record_audio()
    
    if command == 'no':
        pass
    else:
        for index, element in enumerate(command):
            if element in parameters:
                parameters[element] = command[index+1]

    print(parameters)
    #variable = record_audio()
    #index = function.index(variable)
    #function[index] = 'x'
  
    function = ''.join(function)
    print(f'Plotting function: {function}')
    x = np.linspace(float(parameters['from']), float(parameters['to']), parameters['steps'])
    y = (eval(function))

    plt.plot(x, y, color=parameters['color'])
    plt.show()

r = sr.Recognizer()

def record_audio():
    """Records audio and recognizes what should be done with the command.
    """
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=0.6)
        
        try:
            text = r.recognize_google(audio).lower()
            text = text.split()
            return text

        except sr.UnknownValueError:
            print('Sorry I did not get that')
            return record_audio()
        
while 1:
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

            if command[0] == 'goodbye':
                print('Shutting down program...')
                exit()
            


