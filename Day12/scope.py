################### Scope ####################

# Global scope

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#-----------------------------------------------------------------------

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# vairable NOT accessable outside drink_potion function
print(potion_strength)

#-------------------------------------------------------------------------

#Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()


#no scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


#Global Constants

PI = 3.14
URL = 'www.url.com' 