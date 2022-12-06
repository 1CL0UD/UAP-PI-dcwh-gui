from PySimpleGUI import *
from embedClass import *

def sendEmbed():
    print('test')

theme('SandyBeach')

layout = [
    [Text('Masukkan URL Webhook: '), InputText()],
    [Submit(), Cancel()]
]

Window = Window('Webhook Discord', layout)
event, values = Window.read()
Window.close()

print(values[0])
