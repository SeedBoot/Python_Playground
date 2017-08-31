print('hey')

print(2+3)
print(float(9))
print((10.0).is_integer())
print((10.1).is_integer())

stringy = "Wazzup"
name = "Codey McCodeFace"
name2 = "code"

print(stringy)

print("Hi! My name is " + name + ", nice to meet you.")
print(len(name))
print(name[0:5])
print(name2.capitalize())

#format values into strings like line 12, but... cooler
greeting = "Hi! My name is {}".format(name) + ", nice to meet you."
print(greeting)
#

#remove trailing whitespace
are_you = "  yes    I am     "
print(are_you.strip())
#

fruit = [
  "banana",
  "apple",
  "grapes",
  "dragonfruit",
  "peaches",
  "cherries",
  "olives?"]

print(fruit[3])

#lots_of_tiny_fruit = fruit[2, 4, 5, 6] INVALID!
some_tiny_fruit = fruit[4:]
print(some_tiny_fruit)

print(fruit[-1])
print(fruit[-2])

fruit.append("blueberries")
print(fruit)

fruit.sort()
print(fruit)

#tuple is an immutable list
tuple_1 = (1, 2)
print(tuple_1)

#make a list out of tuple
tuple_1_list = list(tuple_1)
print(tuple_1_list)

my_dict = {
  "Name": "Oli",
  "Number": 912384092384}
