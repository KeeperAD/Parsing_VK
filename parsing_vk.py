import requests

# link = input('Введите ссылку на фотоальбом: ')
# album_id = str(link.split('/')[-1].split('_')[1])
# owner_id = str(link.split('/')[-1].split('_')[0].replace('album', ''))

# count = input('Введите количество фотографий: ')
token = '2ad36c1a2ad36c1a2ad36c1a9d2aae2d6022ad32ad36c1a486c8644454a292bfbdacf62'
version = '5.131'
owner_id = '194486811'
album_id = '239913394'
count = '50'

response = requests.get('https://api.vk.com/method/photos.get',
                        params={
                            'owner_id': owner_id,
                            'album_id': album_id,
                            'access_token': token,
                            'v': version,
                            'count': count}
                        )

# response = requests.get('https://api.vk.com/method/photos.getAll',
#                         params={
#                             'owner_id': '40886000',
#                             'access_token': token,
#                             'v': version,
#                             'count': '100'}
#                         )

# data = response.json()['response']['items'][0]['sizes'][6]['url']
data = response.json()['response']['items']

name = 1
for item in data:
    url = item['sizes'][6]['url']
    r = requests.get(url)

    with open(f'/Users/keeper/Downloads/image/{name}.jpg', 'wb') as f:
        f.write(r.content)
    name += 1
