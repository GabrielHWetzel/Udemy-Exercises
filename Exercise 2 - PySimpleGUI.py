import PySimpleGUI as sg
from Functions import FeetInchCovertor as fic

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inch_label = sg.Text("Enter inches:")
inch_input = sg.Input(key="inch")

convert = sg.Button("Convert")
meter_text = sg.Text()

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inch_label, inch_input],
                           [convert, meter_text]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            meter_text.update(f"{fic.convert(float(values['feet']),float(values['inch']))} meters")
        # Quit
        case sg.WINDOW_CLOSED:
            break

window.close()
