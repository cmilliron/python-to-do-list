import PySimpleGUI as sg

def convert_to_meters(feet, inches):
    total_inches = feet * 12 + inches
    return float(total_inches) * .0254

label_feet = sg.Text("Enter Feet")
input_feet = sg.InputText(tooltip="Enter feet", key="feet")

label_inches = sg.Text("Enter inches")
input_inches = sg.InputText(tooltip="Enter inches", key="inches")

button = sg.Button('Convert')

resposne = sg.Text(key="response")

row1 = [label_feet, input_feet]
row2 = [label_inches, input_inches]
row3 = [button, resposne]

window = sg.Window(title='Coverter',
                   layout=[row1, row2, row3])

while True:
    event, value = window.read()
    print(event)
    print(value)
    meters = convert_to_meters(int(value['feet']), int(value['inches']))
    print(meters)
    window['response'].update(meters)
    sg.Popup(f"{value['feet']}ft {value['inches']}in is {meters} in meters.")
window.close()