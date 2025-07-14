import random
import myModule
numbers = ['1', '2', '3']

# return random integer including 1 and 5
randomInt = random.randint(1, 5)
print(randomInt)

# return random floating number between 0 to 1
randomFloat = random.random()
print(randomFloat)

#return random floating numbe between 5 to 10
randomFloat = random.uniform(5,10)
print(randomFloat)

#return randomly a members of list
randomMember = random.choice(numbers)
print(randomMember)

#just random module , we can also add our modules
print(f"pi is {myModule.pi}")
