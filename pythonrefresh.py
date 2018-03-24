age = 34

name = "Joseph"

print("Hello my name is {} and I am {} years old".format(name, age))

today_is_cold = False

# whatever I want here

"""
this is some comment
with multiline
"""

if age > 18:
  print("You are older than 18")
  print("This is another line")
else:
  print("You are too young")

year = 1830

if year > 2000 and year < 2100:
  print("Welcome to the 21st century!")
else:
  print("You are before or after the 21st century")

def hello(name="Joe", age=0):
  return "Hello, {} is {} old.".format(name, age)

introduction = hello(name, age)

print(introduction)

def trippleprint(str):
  print(str * 3)

trippleprint("hello")

dognames = ["Max", "Christy", "Juanita"]

# dognames.insert(0, "Jane")
#del(dognames[2])

#dognames[1] = "Juanita"

#print(len(dognames))
print(dognames)

shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]

for dog in dognames:
  print(dog)

for x in range(1,len(dognames)):
  print(x)

num = 0

while num <= 18:
  print(num)
  num += 1

print("**********************************")

numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

for n in numbers:
  if n > 90:
      print(n)