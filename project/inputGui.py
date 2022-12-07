from PySimpleGUI import *
from embedClass import *

def sendEmbed():
    print('test')

theme('SandyBeach')
embed = embedClass()

layout = [
    [Text('Masukkan URL Webhook:\t'), InputText()],
    [Text('Masukkan Content:\t'), InputText()],
    [Text('Masukkan URL Thumbnail:\t'), InputText()],
    [Text('Masukkan Author:\t\t'), InputText()],
    [Text('Masukkan Title:\t\t'), InputText()],
    [Text('Masukkan Desc:\t\t'), InputText()],
    [Submit(), Cancel()]
]

Window = Window('Webhook Discord', layout)
event, val = Window.read()
Window.close()

webhookUrl = val[0]; embed.setWebhookUrl(webhookUrl)
content = val[1]; embed.setContent(content)
thumbnailUrl = val[2]; embed.setThumbnailUrl(thumbnailUrl)
author = val[3]; embed.setAuthorName(author)
title = val[4]; embed.setTitle(title)
desc = val[5]; embed.setDesc(desc)

print(webhookUrl)
print(content)
print(thumbnailUrl)
print(author)
print(title)
print(desc)
