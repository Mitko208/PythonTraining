# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
Create a dictionary named 'person' with keys 'name', 'age', and 'city' and assign appropriate values to each.
"""

### YOUR CODE HERE:
person = {'name':'Alice', 'age': 30, 'city':'New York'}
### TEST:
print(person)

### EXPECTED OUTPUT:
# {'name': 'Alice', 'age': 30, 'city': 'New York'}

# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
Add a new key 'job' with the value 'Engineer' to the 'person' dictionary created in Task 1.
"""

### YOUR CODE HERE:
person['job'] = 'Engineer'
### TEST:
print(person)

### EXPECTED OUTPUT:
# {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
Remove the 'age' key from the 'person' dictionary using the appropriate dictionary method.
"""

### YOUR CODE HERE:
del person['age']
### TEST:
print(person)

### EXPECTED OUTPUT:
# {'name': 'Alice', 'city': 'New York', 'job': 'Engineer'}

# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
Access and print the value of the 'city' key from the 'person' dictionary.
"""

### YOUR CODE HERE:
city_value = person['city']
### TEST:
print(city_value)

### EXPECTED OUTPUT:
# New York

# ---------------------------------- Task 5 ---------------------------------- #
""" DESCRIPTION:
Check if the key 'age' is still in the 'person' dictionary and print the result.
"""

### YOUR CODE HERE:
# Method 1
#def is_age(person_args):
#    for key in person_args.keys():
#        if key == 'age':
#            return True
#        else:
#            return False
#        
#is_age_present = is_age(person)


# Method 2
if 'age' in person:
    is_age_present = True
else: 
    is_age_present = False
    


# Method 3
#is_age = person.get('age')
#
#if is_age == None:
#    is_age_present = False
#else:
#    pass


### TEST:
print(is_age_present)

### EXPECTED OUTPUT:
# False
