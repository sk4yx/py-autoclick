# Developed By SkayZ

import PySimpleGUI as sg
import os
import configparser

layout = [

    [sg.Text("Left Click", size=(30, 2)), sg.Text("Right Click", size=(30, 2))],
    
    [sg.Text("KEY", size=(30, 2)), sg.Text("KEY", size=(30, 2))],
    [sg.Input(size=(30, 3), key="-Leftkey-"), sg.Input(size=(30, 3), key="-Rightkey-")],

    [sg.Text("CPS", size=(30, 3)), sg.Text("CPS", size=(30, 3))],
    [sg.Input(size=(30, 3), key="-leftput-"), sg.Input(size=(30, 3), key="-rightput-")],

    [sg.Button("Save"), sg.Button("Run")]

]

window  = sg.Window("Auto Click", layout = layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		os.system('taskkill /f /im py.exe')
		break
	if event == "Run":
		os.startfile('button_left.py')
		os.startfile('button_right.py')
	if event == "Save":
		config = configparser.ConfigParser()
		config.read(".config.ini")

		left_key    = values['-Leftkey-']
		left_put    = values['-leftput-']

		right_key    = values['-Rightkey-']
		right_put    = values['-rightput-']
        
		config['Configs']['left_key']  = f"{left_key}"
		config['Configs']['left_put']  = f"{left_put}"

		config['Configs']['right_key']  = f"{right_key}"
		config['Configs']['right_put']  = f"{right_put}"

		with open(".config.ini", "w") as file:
			config.write(file)
			file.close()
