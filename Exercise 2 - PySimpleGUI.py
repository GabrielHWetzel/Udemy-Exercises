import PySimpleGUI as sg
from Functions import FeetInchCovertor as fic

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inch_label = sg.Text("Enter inches:")
inch_input = sg.Input(key="inch")

convert = sg.Button("Convert")
meter_text = sg.Text()

exit_button = sg.Button("Exit")

left_column = sg.Column([[feet_label], [inch_label]])
right_column = sg.Column([[feet_input], [inch_input]])
window = sg.Window("Convertor",
                   layout=[[left_column, right_column],
                           [convert, meter_text, sg.Push(), exit_button]])
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            try:
                meter_text.update(f"{fic.convert(float(values['feet']),float(values['inch']))} meters")
            except ValueError:
                sg.Popup("Please provide two numbers")
        # Quit
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
