import PySimpleGUI as sg
import zipCreator

text_1 = sg.Text("Select Files to Compress :")

input_1 = sg.Input()
input_2 = sg.Input()

text_2 = sg.Text("Select Destination Folder :")

btn_1 = sg.FilesBrowse("Choose", key="files")
btn_2 = sg.FolderBrowse("Choose", key="folder")
btn_3 = sg.Button("Compress", key="compress")

window = sg.Window("File Compressor", layout=[[text_1, input_1, btn_1], [text_2, input_2, btn_2], [btn_3]],
                   font=("Nerko One", 15))

while True:
    events, dict = window.read()
    print(events, dict)
    filePaths = dict['files'].split(";")
    folder = dict['folder']
    zipCreator.make_archive(filePaths, folder)

window.close()
