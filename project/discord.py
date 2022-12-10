import requests
import classEmbed
#class embed

def discord(whUrl, content, thumbUrl, authorName, title, desc, imgUrl):
    embed = classEmbed.classEmbed()
    #embeds input
    data = {
        #webhook profile picture
        'avatar_url' : 'https://images.pexels.com/photos/15286/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500',
        'username' : 'Webhook',
        'content' : '@everyone ' + content,
        'embeds' : [{
            'thumbnail' : {
                'url' : thumbUrl
            },
            'author' : {
                'name' : authorName
            },
            'title' : title,
            'description' : desc,
            'image' : {
                'url' : imgUrl
            },
            'allowed_mentions' : {
                'parse' : ['everyone', 'users'],
                'roles' : ['role-id']
            }
        }]
    }

    #post msg ke server
    disc = requests.post(whUrl, json=data)

    #print status response
    print(disc)
    if str(disc) == '<Response [204]>':
        print('Pesan Terkirim')
        # time.sleep(200)
    else:
        print('Pesan Gagal Terkirim')
