name = "Bro Code"

print(name[:5])

first_name = name[0:3] # starting index inclusive, stopping index exclusive
last_name = name[-4:] # name[4:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "https://www.google.com"

slice = slice(12, -4)
print(website[slice])