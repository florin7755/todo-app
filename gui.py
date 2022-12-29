import functions
import PySimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo")
add_button=sg.Button("Add")

window=sg.Window('My To-Do App',
                 layout=[[label], [input_box, add_button]],
                 font=('Helvetica', 15))
while True:
    event, values=window.read()
    print(event)
    print(values)
    match event:
       case "Add":
window.close()

