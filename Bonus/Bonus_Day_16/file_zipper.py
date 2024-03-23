import PySimpleGUI as sg
from pprint import pprint
from zip_creator import make_archive


label_compress = sg.Text("Select Files to compress:")
input_compress = sg.Input();
choose_button = sg.FilesBrowse(button_text="Choose", key="file")


label_destination = sg.Text("Select destination folder:")
input_destination = sg.Input()
destination_button = sg.FolderBrowse(button_text="Choose",
                                     key="destination_button",
                                     initial_folder="~/Downloads")

compress_button = sg.Button('Compress')
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label_compress, input_compress, choose_button],
                           [label_destination, input_destination, destination_button],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    pprint(event)
    pprint(values)
    filepaths = values['file'].split(';')
    # pprint(filepaths)
    destination_path = values['destination_button']
    make_archive(filepaths, destination_path)
    window['output'].update(value='Compression Completed')


window.close()


