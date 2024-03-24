import PySimpleGUI as sg
from pprint import pprint
from unzip import extract_archive

add_label = sg.Text("File")
add_input = sg.Input(key='add_input')
add_file = sg.FileBrowse(initial_folder="~/Download", key="file")

dest_label = sg.Text("Destination")
dest_input = sg.Input(key='dest_input')
dest_file = sg.FolderBrowse(initial_folder="~/Download", key="dest_folder")

extract_button = sg.Button("Extract", key="extract")
output_label = sg.Text(key='output', text_color='green')
exit_button = sg.Button("Exit", key="exit")

# Layout with columns
col1 = sg.Column(layout=[[add_label], [dest_label], [extract_button]], vertical_alignment='top')
col2 = sg.Column(layout=[[add_input], [dest_input], [output_label]], vertical_alignment='top')
col3 = sg.Column(layout=[[add_file], [dest_file], [exit_button]], vertical_alignment='top')

# Original Layout
# layout = [[add_label, add_input, add_file],
#           [dest_label, dest_input, dest_file],
#           [extract_button, output_label]]

window = sg.Window(title="Unzipper",
                   layout=[[col1, col2, col3]])

while True:
    event, values = window.read()
    print(event)
    pprint(values)
    archive_path = values['file']
    dest_folder = values['dest_folder']
    extract_archive(archive_path, dest_folder)
    window['output'].update(value="Completed")

window.close()