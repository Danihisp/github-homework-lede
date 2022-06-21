# APIs!!!!!
# Application
# Programming
# Interface

# https://pokeapi.co/api/v2/pokemon/ditto
# Visually it looks like a dictionary
# Technically speaking it's JSON
# JSON = JavaScript Object Notation
#   * doesn't need javascript!
# CSV = Comma-separated values
#   * doesn't need .... a comma programming language????


numbers = [1, 2, 3, 4, 5]
avg = sum(numbers) / 5


# package, or module, or library
# hey Python, you have some statistics stuff
# please let me use it!!!!
import statistics
statistics.mean(numbers)

# requests is a Python library
# it's great at getting stuff from
# the internet
# it doesn't come with Python though!!!
# you have to install it separately

# Import the requests library
import requests

# https://pokeapi.co/api/v2/pokemon/slowpoke
url = "https://pokeapi.co/api/v2/pokemon/slowpoke"

# Ask for the data from the website
response = requests.get(url)

# Turn the JSON into a dictionary
data = response.json()

# How much does slowpoke weigh??????
print(data['name'], "weighs", data['weight'])

# Print it out to see what it is
print(data['moves'])

# It's a list
# Let's just look at the first one
print(data['moves'][0].keys())

print("### PRINTING OUT SOME MOVES")

# How do we print the name?
for move in data['moves']:
    print("---------")
    # print(move)
    # print(move.keys())
    # print(move['move'])
    print(move['move']['name'])

# Turn this into a list comprehension!!!
# I want
# * A list of move names
# You have
# * A list of diccionaries
# * where move['move']['name'] gives you the name

move_names = [move['move']['name'] for move in data['moves']]
print(move_names)



# 1. What is the URL to the documentation?
# https://pokeapi.co/api/v2/{endpoint}/

# 2. What pokemon has the ID of 55?
# golduck

# 3. How tall is that pokemon?
# 17

# 4. How many versions of Pokemon games have been released?
# 19

# 5. Print out the name of every electric-type pokemon.

url = "https://pokeapi.co/api/v2/type/13/"

# Ask for the data from the website
response = requests.get(url)

# Turn the JSON into a dictionary
data = response.json()

print(data)

print(data.keys())

print(data['pokemon'])

for pokemon in data['pokemon']:
    print("---------")
    print(pokemon['pokemon']['name'])

# 6. What are electric-type Pokemon called in the Korean version of the game?

url = "https://pokeapi.co/api/v2/type/"

# Ask for the data from the website
response = requests.get(url)

# Turn the JSON into a dictionary
data = response.json()

print(data)

print(data.keys())

# print(data['name'])

"cannot be answered using the API."

# 7. Who has a higher speed stat, Eevee or Pikachu?

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

# Ask for the data from the website
response = requests.get(url)

# Turn the JSON into a dictionary
data = response.json()

print(data)

print(data.keys())

print(data['stats'])

for stat in data['stats']:
    print(stat['stat'])
    # print(stat['stat'].keys())
    print(stat['stat']['name'])

stat['stat']['name'] == speed
    
pikachu_speed = stat['stat']['name'] for stat in data['stats']
print(pikachu_speed)

