from PySimpleGUI import *
import classEmbed
from discord import *
import time
import printData_deleteData as pd


theme('SandyBeach')
embed = classEmbed.classEmbed()

layout = [
    [Text('URL Webhook:\t'), InputText()],
    [Text('Content:\t\t'), InputText()],
    [Text('URL Thumbnail:\t'), InputText()],
    [Text('Author:\t\t'), InputText()],
    [Text('Title:\t\t'), InputText()],
    [Text('Desc:\t\t'), InputText()],
    [Text('Image Url:\t'), InputText()],
    [Button('Send'), Button('Cancel')]
]

Window = Window('Webhook Discord', layout)
while True:
    event, val = Window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Send':
        embed.setWebhookUrl(val[0])
        if '.txt' in val[1]:
            embed.setContent(pd.openData(val[1]))
        else:
            embed.setContent(val[1])
        embed.setThumbnailUrl(val[2])
        embed.setAuthorName(val[3])
        embed.setTitle(val[4])
        embed.setDesc(val[5])
        embed.setImgUrl(val[6])
        #function
        discord(embed.getWebhookUrl(), embed.getContent(), embed.getThumbnailUrl(), embed.getAuthorName(), embed.getTitle(), embed.getDesc(), embed.getImgUrl())
        break
    elif event == 'Cancel':
        break
Window.close()

# print(val)
