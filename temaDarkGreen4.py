import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("NPM    : 2210010358")],
                            [sg.Text("Nama   : Muhammad Taufiq Hidayatn")],
                            [sg.Text("Kelas  : 5O Regluer Banjarmasin")],
                            [sg.Text("Matkul :Pemrograman Visual 3")]
                            ], size=(400,200))
window()
window.close()