import sys
import keyword

#Function
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Ưu tiên toán tử: not, and, or 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#while 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # With the continue statement we can stop the current iteration, and continue with the next
  print(i)
#for loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#Adding item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

exit() 
#Dictionary 
cars = {'make': 'BMW', 'model': '550i', 'year': 2003}
print(cars)
print(cars['make'])
d = {}
d['one'] = 1
d['two'] = 2
print(d.keys())
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily.values())
print(myfamily.items())

#List 
cars = ["Audi", "Honda", "BMW"]
cars[2]= "Mec"
cars.append("Maybach")
cars.insert(1, "Jeep")
x = cars.index("Jeep")
print (x)
print (cars.pop()) #loai bo va tra ve phan tu cuoi cung 
print (cars)
new_car = cars[0:2]
print(new_car)
#sort, remove 

a = "1abc2abc3abc"
print (a.replace('abc', 'ABC'))

a = "I am a good student"[0]
b = "You can do it"
print (a)
print (b[0])
print (len(a))
print(b.lower())

x = 4
x = "Chau"
print (x) 

x = str(3)    # x will be '3'
print(type(x))
y = int(3)    # y will be 3
print(type(y))
z = float(3)  # z will be 3.0
print(type(z))

print(sys.version)
print(keyword.kwlist)

print("Hello, World!")
a = "Chau"
b = a 
print(a == b)


if 5 > 2:
  print("Five is greater than two!")