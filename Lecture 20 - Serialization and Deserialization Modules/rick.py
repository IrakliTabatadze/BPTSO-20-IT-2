import requests

character_url = 'https://rickandmortyapi.com/api/character'

characters = requests.get(character_url).json()

for character in characters['results']:
    for episode in character['episode']:
        print(episode)