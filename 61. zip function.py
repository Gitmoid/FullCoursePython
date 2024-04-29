usernames = ["Dude", "Bro", "Mister"]
passwords = ("password", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users_zip = zip(usernames, passwords, login_date)  # aggregate elements from two or more iterables (list, tuples, sets)
print(type(users_zip))
for i in users_zip:
    print(i)

users_list = list(zip(usernames, passwords))
print(type(users_list))
for i in users_list:
    print(i)

users_dict = dict(zip(usernames, passwords))
print(type(users_dict))
for key, value in users_dict.items():
    print(key, value)
