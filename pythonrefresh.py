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
del(dognames[2])

dognames[1] = "Juanita"

#print(len(dognames))
print(dognames)

shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"]