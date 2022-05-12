programming_dictionary = {
    "Bug": "An error in a program that prevents the prgoram from running as expected",
    "Fucntion": "A piece of code that you can easily call over and over again.",
}

#print(programming_dictionary["Bug"])

#adding new intems to dict.

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

#creates an empty dictionary
empty_dictionary = {}

#wipe an eexiting dictionary
#programming_dictionary = {}

#edit an item in dictionary
programming_dictionary["Bug"] = "Testing a new value for exting key"
print(programming_dictionary)

#looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
