store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = list(map(to_euros, store))  # map() applies function to each item in an iterable (list, tuple, etc.)
for i in store_euros:
    print(i)
