cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}

cities_in_C = {key: round(((value - 32) * 5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_F)
print(cities_in_C)

weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities_in_F.items()}
print(desc_cities)


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


desc_temp_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(desc_temp_cities)
