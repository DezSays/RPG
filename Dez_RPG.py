from audioop import add
import math
import random

# Come up with at least two other characters with their individual characteristics, and implement them. warrior and mage - potential powers: deal double damage if health is below 50%, attacks enemy health and power.

# Give each enemy a bounty. For example, the prize for defeating the `Goblin` is 5 coins, for the Wizard it is 6 coins. // ideas for this// create a new method within the hero class that tracks coints - see bank example perhaps?


class Character:
    def __init__(self,health,power):
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    
    def attack(self, enemy):
        enemy.health-=self.power
        
        if(self.character_name == "Hero Velvet Thunder"):
            print(f'You inflicted {self.power} damage to the {enemy.character_name}! ')
            
        elif(self.character_name == "Dr. Newlon"):
            print(f'The {self.character_name} inflicted {self.power} damage. ')
        
        elif(self.character_name == "Giant Green Goblin"):
            print(f'The {self.character_name} inflicted {self.power} damage. ')
        
        
        elif(self.character_name == "Urrrhhhgggaaarrruu"):
            print(f"The {self.character_name} inflicted {self.power} damage on {enemy.character_name}!")
    
    
    
    def print_status(self):
        if(self.character_name == "Hero Velvet Thunder"):
            print(f'{self.character_name} has {self.health} health and {self.power} power.')
        elif(self.character_name == "Dr. Newlon"):
            print(f'The {self.character_name} has {self.health} health and {self.power} power. ')
        elif(self.character_name == "La Sombra"):
            print(f'The {self.character_name} has {self.health} health and {self.power} power. ')
        elif(self.character_name =="Giant Green Goblin"):
            print(f'The {self.character_name} has {self.health} health and {self.power} power. ')
        elif(self.character_name == "Urrrhhhgggaaarrruu"):
            print(f'{self.character_name} has {self.health} health and {self.power} strength. {self.character_name} is of the Zombie class and cannot be killed. Run! ')







class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "Hero Velvet Thunder"
        super(Hero, self).__init__(health,power)
    
    def attack(self, enemy): #Hero attack mathod that allows for different abilities (the zombie cannot die)(the shado only takes a hit 10% of the time)
        if(enemy.character_name == "La Sombra"): 
            print(self.Shining_Light(enemy))
        elif(enemy.character_name != "Urrrhhhgggaaarrruu" ):
            enemy.health-=self.power
            print(self.getPower(enemy)) 
        
    def Shining_Light(self, enemy): #This allows the shadow to evade being hit 90% of the time, and kills it once it is finally hit.
        s = random.randint(1,10)
        if s == 1 and (enemy.character_name != "Urrrhhhgggaaarrruu"):
            night_vision = enemy.health-self.power
            enemy.health = night_vision
            return f'WOW! {self.character_name} was able to hit {enemy.character_name}! '
        else:
            return f'{enemy.character_name} is of the Shadow Class. It is hard to hit what you cannot see! '
    
    def getPower(self, enemy): #This allows the hero to hit with double the power 20% of the time.
        r = random.randint(1,5)
        if r ==3 and (enemy.character_name != "Urrrhhhgggaaarrruu"):
            DoubleTrouble = (self.power + self.power)
            enemy.health-self.power
            return f'WOW! {DoubleTrouble} damage was dealt to {enemy.character_name} this turn!'
        else:
            return f'{self.character_name} took {self.power} damage this turn. '   




class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "Giant Green Goblin"
        super(Goblin, self).__init__(health,power)




class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "Urrrhhhgggaaarrruu"
        super(Zombie, self).__init__(health,power)



class Shadow(Character):
    def __init__(self, health, power):
        self.character_name = "La Sombra"
        super(Shadow, self).__init__(health,power)    



class Medic(Character):
    def __init__(self, health, power):
        self.character_name = "Dr. Newlon"
        super(Medic, self).__init__(health,power)
    def attack(self, enemy):
        if(enemy.character_name != "Urrrhhhgggaaarrruu"): 
            enemy.health-=self.power
        print(self.getHealed(enemy))       
    def getHealed(self, enemy):
        r = random.randint(1,5)
        if r ==1:
            Heal_Me = (self.health + 2)
            self.health = Heal_Me
            return f'{self.character_name} has healed! He now has {Heal_Me} health!'
        else:
            return f'{enemy.character_name} took {self.power} damage this turn. '
        
        
        





hero = Hero(10,5)
goblin = Goblin(6,2)
zombie = Zombie(50,1)
medic = Medic(30, 1)
shadow = Shadow(1,1)




def main(enemy):

        
    while enemy.alive() > 0 and hero.alive() > 0:
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)          
            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
                break
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        if enemy.alive:
            enemy.attack(hero)
            
            if not hero.alive():
                print("You have been defeated.")

main(shadow)















