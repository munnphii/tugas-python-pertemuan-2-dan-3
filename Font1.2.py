import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile", 
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial", 25))],
                            [sg.Text("NPM    : 2210010358")],
                            [sg.Text("Nama   : Muhammad Taufiq Hidayat")],
                            [sg.Text("Kelas  : 5O Regluer Banjarmasin")],
                            ], 
                        size=(500,200), 
                        font=("Times", 18))
window()
window.close()