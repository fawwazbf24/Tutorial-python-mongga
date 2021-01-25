import PySimpleGUI as sg
import os.path

print(dir(sg))
#size (x,y) dalam jumlah karakter
kolom1=[
    [

        sg.Text("Image Folder"),

        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),

        sg.FolderBrowse()

    ],

    [

        sg.Listbox(

            values=[], enable_events=True, size=(40,20), key="-FILE LIST-"

        )

    ]

]

kolom2=[

    [

        sg.Text("Choose an Image from list from left")

    ],

    [

        sg.Text(size=(40,1), key="-TOUT-")

    ],

    [

        sg.Image(key="-IMAGE-")

    ]

]

layout= [

    [

        sg.Column(kolom1),

        sg.VSeparator(),

        sg.Column(kolom2),

    ]

]

window = sg.Window("UI Testing",layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":

        break

    if event == "-FOLDER-":

        folder = values["-FOLDER-"]

        try:

            file_list = os.listdir(folder)

        except :

            file_list = []

        fnames = [

            f

            for f in file_list

            if os.path.isfile(os.path.join(folder, f))

            and f.lower().endswith((".png", ".jpg", ".jpeg"))

        ]

        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":

        try:

            filename = os.path.join(

                values["-FOLDER-"], values["-FILE LIST-"][0]

            )

            window["-TOUT-"].update(filename)

            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()