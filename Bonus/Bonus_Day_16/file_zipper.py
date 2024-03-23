import PySimpleGUI as sg

label_compress = sg.Text("Select Files to compress:")
input_compress = sg.Input();
choose_button = sg.FileBrowse("Choose")

label_destination = sg.Text("Select destination folder:")
input_destination = sg.Input()
destination_button = sg.FolderBrowse("Choose")

compress_button = sg.Button('Compress')

window = sg.Window("File Compressor",
                   layout=[[label_compress, input_compress, choose_button],
                           [label_destination, input_destination, destination_button],
                           [compress_button]])

window.read()

window.close()


