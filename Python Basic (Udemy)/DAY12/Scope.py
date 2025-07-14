# Local Scope
 
def drink_potion() :
    potion_strength = 2  #Local variable
    print(potion_strength)

drink_potion()
#print(potion_strength)   # not acessible 

# Global Scope

player_health = 2   # global variable

def drink_potion1() :
    drink_potion = 2
    print(player_health)

drink_potion1()
print(player_health)

# modufying a global varibale

enemies = 1

def inncrease_enemies() :
    global enemies    # generally we don't use this type rather we go with line 29
    enemies +=1   # now this varible is not a new varibale
    print(f"enemies inside function: {enemies}.")
    #return enemies+1 

inncrease_enemies()
print(f"enemies outside function: {enemies}.")

# There is no Block Scope like cpp or java
# if/While/for mai agar koi varibale h to agar if/While/for kisi function
# mai h to variables ka scope us function tak hoga 
# agar kisi function mai nhi h to variables ka scope global ho jayega

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5 :
    ram = 3
while game_level <= 5 :
    new_enemy = "Gajendra"
    game_level += 1

print(new_enemy)