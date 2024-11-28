import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_info = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            planet_info.append((name, mass, orbit_period))
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planet_info

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda x: x[1])
    return heaviest

planets = fetch_planet_data()
name, mass, _ = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
