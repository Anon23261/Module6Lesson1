import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {pokemon_name}")
        return None

def display_pokemon_info(pokemon_data):
    if pokemon_data:
        name = pokemon_data['name']
        abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
        print(f"Name: {name}")
        print("Abilities:", ", ".join(abilities))

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data_list.append(data)
        display_pokemon_info(data)

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {average_weight}")
