import requests
url = 'https://www.omdbapi.com/?t=hackers&apikey=caaebd73'
r = requests.get(url)

json_data = r.json()

for key in json_data.keys():
    print(key + ":" + str(json_data[key]))