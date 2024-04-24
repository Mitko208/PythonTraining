n = int(input("How many names are you going to enter? "))
while n <= 0:
    n = int(input("How many names are you going to enter? "))
    

names = []

for i in range(n):
    names.append(input("Enter a name, please: "))
    
print("*"*50)
print("The names you've entered are:")

for el in names:
    print(el)

