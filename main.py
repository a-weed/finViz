<<<<<<< HEAD
import PySimpleGUI as sg


print("Hello World!")

##sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

#Create the window
window = sg.Window("Demo", layout)

#Create an event loop
while True:
    event, values = window.read()
    #End if user closes window or presses OK
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close
=======
print("Hello World!")
>>>>>>> 3b11e8246439b46c6ccdffcea213e4d1aa07055e
