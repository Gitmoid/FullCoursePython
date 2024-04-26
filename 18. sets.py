utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.update(dishes)
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

utensils.clear()
