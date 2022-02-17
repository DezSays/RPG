# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
        
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power 
    
    def attack(self, enemy):
        enemy.health-=self.power
    
    def print_status(self):
        print(f'You have {self.health} health and {self.power} power.')



class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power 
    
    def attack(self, enemy):
        enemy.health-=self.power
    
    def print_status(self):
        print(f'The goblin has {self.health} health and {self.power} power.')



def main():
    hero = Hero(10,5)
    goblin = Goblin(6,2)

    while goblin.alive() > 0 and hero.alive() > 0:
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if not goblin.alive():
                print("The goblin is dead.")
                break
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does {} damage to you.".format(goblin.power))
            if not hero.alive():
                print("You are dead.")

main()














