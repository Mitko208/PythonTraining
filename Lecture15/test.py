d = {"one":[1,[65,45,87],3], "two":[4,5,6]}

print(d)
print(d['one'])
print(d['two'])
print(d["one"][2])

print(d["one"][1])

d2 = {"oneOfTwo":1,"twoOfTwo":["hello", "this is getting pretty confusing"]}

d['three'] = d2

print(d)
print(d["three"]['twoOfTwo'])
new_el = "four"
d[new_el] = 2+2
print(d)

def hello_world():
    print("\n\t","*"*30)
    print(f"\n{"Hello World":^50}")
    print("\n\t","*"*30)

hello_world()

l1 = [0,1,2,3,4,5,6,7,8,9,10,11]
l2 = [n+2 for n in l1]
print(l2)