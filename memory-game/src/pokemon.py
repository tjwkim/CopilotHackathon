import requests
from io import BytesIO
from PIL import Image
import os

# 이미지 저장 경로
save_path = '/workspaces/CopilotHackathon/memory-game/src/assets/pokemon'

# 디렉토리 생성
os.makedirs(save_path, exist_ok=True)

# Pokemon 이미지 다운로드 및 저장
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=8')
data = response.json()
for pokemon in data['results']:
    pokemon_data = requests.get(pokemon['url']).json()
    image_url = pokemon_data['sprites']['front_default']
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    image.save(os.path.join(save_path, f"{pokemon['name']}.png"))