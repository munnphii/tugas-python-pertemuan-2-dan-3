import PySimpleGUI as sg
sg.theme("DarkRed2")
sg.theme_text_color("Blue")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("NPM    : 2210010358")],
                            [sg.Text("Nama   : Muhammad Taufiq Hidayat")],
                            [sg.Text("Kelas  : 5O Regluer Banjarmasin")],
                            [sg.Text("Matkul :Pemrograman Visual 3")]
                            ], size=(400,200))
window()
window.close()