capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "Australia": "Canberra",
            "Russia": "Moscow"}

print(capitals["Russia"])

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop("Australia")

print(capitals.get("Germany"))

print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

capitals.clear()