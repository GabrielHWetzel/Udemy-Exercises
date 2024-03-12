import PySimpleGUI as sg
from Functions import ZipExtractor

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3],
                           [extract_button]])

while True:
    event, values = window.read()
    print(event, values)

    archivepath = values["archive"]
    destination = values["folder"]

    message = ZipExtractor.extract_archive(archivepath, destination)

    window["output"].update(value=message)

    if event == sg.WINDOW_CLOSED:
        break
window.close()
