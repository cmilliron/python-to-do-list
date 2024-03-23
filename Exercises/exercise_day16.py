import PySimpleGUI as sg


label_feet = sg.Text("Enter Feet:")
input_feet = sg.InputText()

label_inches = sg.Text("Enter Inches")
input_inches = sg.InputText()

covert_button = sg.Button('Convert')

window = sg.Window(title="Converter",
                   layout=[[label_feet, input_feet],
                           [label_inches, input_inches],
                           [covert_button]])

window.read()

window.close()
