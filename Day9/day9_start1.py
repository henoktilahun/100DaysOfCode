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

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary

tarval_log = {
    "France": ["paris", "Lille", "Digjon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting dictionary in a dictionary

tarval_log_ = {
    "France": {"cities_visitied": ["paris", "Lille", "Digjon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a List

tarval_log_ = [
    {
        "country": "France", 
        "cities_visited": ["paris", "Lille", "Digjon"], 
        "total_visits": 12
        },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        },
]