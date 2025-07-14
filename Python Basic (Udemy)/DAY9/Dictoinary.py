programmingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123 : "Just an number 123."
}

#Retrieving items from dictionary
print(programmingDictionary["Bug"])
print(programmingDictionary["Loop"])
print(programmingDictionary[123])

#Adding new items to dictionary
programmingDictionary["Program"] = "A piece of code that done a specific job."

print(programmingDictionary)

#Edit an item in a dictionary
programmingDictionary["Bug"] = "A moth in your computer."
print(programmingDictionary["Bug"])

#Loop through a dictionary
for key in programmingDictionary :
    print(key)
    print(programmingDictionary[key])

#Wipe an existing dictionary 
programmingDictionary = {}

print(programmingDictionary)

#Create an empty dictionary
emptyDictionary = {}

# making an randon dictionary
randomDictionary = {
    "a": 1,
    "b": 2
}

print(randomDictionary["a"])
print(randomDictionary["b"])