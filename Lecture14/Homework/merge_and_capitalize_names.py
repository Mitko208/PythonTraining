first_names = ["ivan", "maria", "petar"]
sur_names = ["ivanov", "popova", "petrov"]
full_name = []
for el in range(len(first_names)):
    full_name.append(first_names[el].capitalize() + " " + sur_names[el].capitalize())

print(full_name)