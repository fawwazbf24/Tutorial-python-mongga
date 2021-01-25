import PySimpleGUI as sg

kolom1=[
    [sg.In(size=(40,1),key="-INPUT-")],
    [sg.Button("Tombol Ganti Text",key="-TOMBOL1-")],
    [sg.Submit("Submit")]
]
kolom2=[
    [sg.Text("Text akan berubah",key="-TEXT-")],
]
layout=[
    [sg.Column(kolom1)],
    [sg.VSeparator()],
    [sg.Column(kolom2)]
]

window=sg.Window("Tes UI",layout)

while True:
    event, values = window.read()
    if event=="EXIT" or event==sg.WIN_CLOSED:
        break
    if event=="-TOMBOL1-":
        text=values["-INPUT-"]
        window["-TEXT-"].update(text)

window.close()