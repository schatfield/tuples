# Create a tuple named zoo that contains 10 of your favorite animals.

zoo = ("bear", "elephant", "lion", "tiger", "flamingo", "penguin", "meercat", "monkey", "giraffe", "sea turtle")



# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1

print(zoo.index("lion"))


# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found

# STOP: what are you trying to do? You are trying to "find" a specific animal in your tuple and print out that you found it. 

animal_to_find = "monkey"
print(animal_to_find)
if animal_to_find in zoo:
    print(zoo)
    if animal_to_find: 
        print(f'The {animal_to_find} was found')
        print()

        # if you set animal_to_find's value to an animal that isn't in zoo, nothing will print! It is also case sensitive.


# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"


# Create a variable for the animals in your zoo tuple, and print them to the console.

(animal_1, animal_2, animal_3, animal_4, animal_5, animal_6, animal_7, animal_8, animal_9, animal_10) = zoo

print(animal_1) 
print(animal_2)
print(animal_3)
print(animal_4)
print(animal_5)
print(animal_6)
print(animal_7)
print(animal_8)
print(animal_9)
print(animal_10)
print()


# Convert your tuple into a list.

# One way to do it:
zoo = list(zoo)
print('tuple into a list', zoo)
print()


# Use extend() to add three more animals to your zoo.

zoo.extend(["lemur", "tree frog", "kangaroo"])
print(zoo)
print()

# Convert the list back into a tuple.
zoo =tuple(zoo)
print('list into a tuple', zoo)
print()



# -----------------------------------------------------------------
# Joe's example for list to set:

# Turn a list into a set, then back into a list. Trick for removing duplicate values from your list
# list_of_names = ["Mary", "Joseph", "Bob", "Joseph"]
# unique_list = list(set(list_of_names))
# # variable / list method / set method to complete the action / pass in the list you want turned into a set.
# print('no dupes!', unique_list)


# My attempt at applying the above example to turning tuple into list:

# Tried to assign zoo tuple to a variable to convert like Joe's example above with sets into lists- why didn't this work?

# zoo_list = list(zoo)
# variable / list method / tuple method to complete the action / pass in the list you want turned into a set.
# print('tuple into a list', zoo)