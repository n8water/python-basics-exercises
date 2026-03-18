""" Python Basiscs: A Practical Introduction - 9.6 Store Relationships in Dictionaries """
capitals = {
    "California": "Sacramento",
    "New York": "Albany",
    "Texas": "Austin"
}

key_value_pairs = (
    ("California", "Sacramento"),
    ("New York", "Albany"),
    ("Texas", "Austin")
)

capitals2 = dict(key_value_pairs)

print(capitals)
print(key_value_pairs)
print(capitals2)

# access dictionary values
print("Access capital of Texas")
print("capitals[\"Texas\"]")
print(capitals["Texas"])

# adding and removing values in a dictionary
capitals["Colorado"] = "Denver"
print(capitals)

del capitals["Texas"]
print(capitals)

#checking the existence of dictionary keys
try:
    print(capitals["Arizona"])
except KeyError:
    print("Key not found")

result = "Arizona" in capitals
print(f"Arizona in capitals? {result}")

result = "California" in capitals
print(f"California in capitals? {result}")

if "Arizona" in capitals:
    print(f"The capital of Arizona is {capitals['Arizona']}.")

# in checks for the existence of keys not values!
print("Sacramento in capitals?", "Sacramento" in capitals)

# iterating over dictionaries

for key in capitals:
    print(f"The capital of {key} is {capitals[key]}")

print(capitals.items())

print(type(capitals.items()))

for state, capital in capitals.items():
    print(f"The capital of {state} is {capital}.")

# dictionary keys and immutability
capitals[50] = "Honolulu"

print(capitals)

# nested dictionaries

states = {
    "California": {
        "capital": "Sacramento",
        "flower": "California Poppy"
    },
    "New York": {
        "capital": "Albany",
        "flower": "Rose"
    },
    "Texas": {
        "capital": "Austin",
        "flower": "Bluebonnet"
    }
}

print(states["Texas"])

# get the Texas state flower
print(states["Texas"]["flower"])