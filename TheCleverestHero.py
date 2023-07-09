import requests

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
data = response.json()

hero_dict = {}


for hero_data in data:
    hero_name = hero_data['name']
    hero_intelligense = hero_data["powerstats"]["intelligence"]
    hero_dict[hero_name] = int(hero_intelligense)

# print(hero_dict)


our_heroes_dict = {}

for hero_name, hero_intelligense in hero_dict.items():
    if hero_name in ['Hulk', 'Captain America','Thanos']:
        our_heroes_dict[hero_name] = hero_intelligense


smartest = max(our_heroes_dict)
print(f' Самый умный из наших героев это: {smartest}')