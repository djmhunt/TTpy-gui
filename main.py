import PySimpleGUI as sg
import subprocess

sg.theme('LightGrey1')   # Add a touch of color
sg.SetOptions(element_padding=(0, 0))


menu_layout = [['File', ['Open', 'Save', 'Exit']],
               ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
               ['Help', 'About...'], ]

load_layout = [[sg.Text('Filename')],
               [sg.Input(), sg.FileBrowse()],
               [sg.OK(), sg.Cancel()]]

model_layout = [[sg.Text('Filename')]]

task_layout = [[sg.Text('Filename')]]

main_layout = [[sg.Menu(menu_definition=menu_layout, )],
               [sg.TabGroup([[sg.Tab(title='Load', layout=load_layout, tooltip='tip'),
                              sg.Tab(title='Model', layout=model_layout, tooltip='TIP2'),
                              sg.Tab(title='Task', layout=task_layout, tooltip='TIP2')]], tooltip='TIP2')],
               [sg.Output(size=(88, 20))]]
#sg.InputText(), sg.Button('Ok')

#sg.Print to print to debug
#window.Element(key).Update(value and settings)

# Create the Window
main_window = sg.Window(title='TTpy', layout=main_layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = main_window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    elif event is 'OK':
        print('You entered ', values[0])
    elif event == 'About...':
        sg.popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
    elif event == 'Open':
        filename = sg.popup_get_file('file to open', no_window=True)
        print(filename)

main_window.close()
