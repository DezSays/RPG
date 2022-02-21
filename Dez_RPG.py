from audioop import add
import math
import random

# ## Items - still needs work.
# 1. Make a `SuperTonic` item to the store, it will restore the hero back to 10 health points. # Dez comments# make a class called items. need method called supertonic.  
# 2. Add an `Armor` item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
# 3. Add an `Evade` item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
# 4. Come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.




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
        
        elif(self.character_name == "Kevin the Bulldog"):
            print(f'The {self.character_name} inflicted {self.power} damage. ')
        
        elif(self.character_name == "Doug the Pug"):
            print(f'The {self.character_name} inflicted {self.power} damage. ')        
        
        elif(self.character_name == "Urrrhhhgggaaarrruu"):
            print(f"The {self.character_name} inflicted {self.power} damage on {enemy.character_name}!")
    
    
    
    def print_status(self): #These could be shortened using else, but formatting it the long way is easier for me to keep track.
        if(self.character_name == "Hero Velvet Thunder"):
            print(f'{self.character_name} has {self.health} health and {self.power} power.')
        
        elif(self.character_name == "Dr. Newlon"):
            print(f'{self.character_name} has {self.health} health and {self.power} power. ')
        
        elif(self.character_name == "La Sombra"):
            print(f'{self.character_name} has {self.health} health and {self.power} power. ')
        
        elif(self.character_name =="Giant Green Goblin"):
            print(f'{self.character_name} has {self.health} health and {self.power} power. ')
        
        elif(self.character_name =="Kevin the Bulldog"):
            print(f'{self.character_name} has {self.health} health and {self.power} power. ')
        
        elif(self.character_name =="Doug the Pug"):
            print(f'{self.character_name} has {self.health} health and {self.power} power. ')
        
        elif(self.character_name == "Urrrhhhgggaaarrruu"):
            print(f'{self.character_name} has {self.health} health and {self.power} strength. {self.character_name} is of the Zombie class and cannot be killed. Run! ')
    








class Hero(Character):
    
    def __init__(self, health, power):
        self.character_name = "Hero Velvet Thunder"
        super(Hero, self).__init__(health,power)

    
    def attack(self, enemy): #Hero attack mathod that allows for different abilities (the zombie cannot die)(the shadow only takes a hit 10% of the time)

        if(enemy.character_name == "La Sombra"): 
            print(self.Shining_Light(enemy))
            print(self.Spoils_of_War(enemy))
            
        elif(enemy.character_name =="Kevin the Bulldog"):
            print(self.Bulldog_Bite(enemy))
            print(self.Spoils_of_War(enemy))
            
        elif(enemy.character_name =="Doug the Pug"):
            print(self.Cuddle_Buddy(enemy))
            print(self.Spoils_of_War(enemy))
                
        elif(enemy.character_name != "Urrrhhhgggaaarrruu" ):
            enemy.health-=self.power
            print(self.getPower(enemy))
            print(self.Spoils_of_War(enemy))
        
    def Cuddle_Buddy(self, enemy):
        enemy.health-=self.power
        d = random.randint(1,4)
        if d == 1 and (enemy.character_name != "Urrrhhhgggaaarrruu"):
            power_of_love = self.power-enemy.power
            self.power = power_of_love
            return f'{enemy.character_name} is so cute, that he has weakened your power! Your power is now at {self.power}'
        else:
            return f'{enemy.character_name} has been hit with {self.power} damage. '
    
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
            enemy.health-=self.power
            return f'WOW! {DoubleTrouble} damage was dealt to {enemy.character_name} this turn!'
        else:
            return f'{self.character_name} took {self.power} damage this turn. '   
    
    def Bulldog_Bite(self, enemy): #this gives my warrior a 25% chance of hitting the hero 4x harder if the hero's health is under a set amount. 
        b = random.randint(1,4)
        bite_power = self.health <= 20
        if b ==1 and bite_power and (enemy.character_name != "Urrrhhhgggaaarrruu"):
            x = (enemy.power + enemy.power + enemy.power) 
            Bite = self.health - x
            self.health=Bite
            dirty_mouth = enemy.power + x
            return f'{enemy.character_name} Special Power Activated! {dirty_mouth} damage was dealt to {self.character_name} this turn!'
        else:
            dental_insurance = enemy.health - self.power
            enemy.health = dental_insurance
            return f'{enemy.character_name} took {self.power} damage this turn. ' 

    def Spoils_of_War(self, enemy):
        self.chest = []
        self.bounty = "0"
        if enemy.health <= 0:
            coins = self.chest.append(enemy.bounty)
            self.chest = coins
            print(f'{self.chest}')
            return f'{self.character_name} has successfully defeated {enemy.character_name} and has collected a bounty of {enemy.bounty} coins! '
        else:
            False 




class Goblin(Character): #Starter character
    def __init__(self, health, power):
        self.bounty = "5"
        self.character_name = "Giant Green Goblin"
        super(Goblin, self).__init__(health,power)
        


class Zombie(Character): #health not affected
    def __init__(self, health, power):
        self.bounty = "10"
        self.character_name = "Urrrhhhgggaaarrruu"
        super(Zombie, self).__init__(health,power)




class Shadow(Character): #only gets hit 10% of the time
    def __init__(self, health, power):
        self.bounty = "7"
        self.character_name = "La Sombra"
        super(Shadow, self).__init__(health,power)    



class Warrior(Character):#25% chance of hitting the hero 4x harder if the hero's health is under a set amount.
    def __init__(self, health, power):
        self.bounty = "12"
        self.character_name = "Kevin the Bulldog"
        super(Warrior, self).__init__(health,power)



class Mage(Character):#attacks heros power 25% of time instead of hero health. If hero power drops below 0, mage heals.
    def __init__(self, health, power):
        self.bounty = "17"
        self.character_name = "Doug the Pug"
        super(Mage, self).__init__(health,power) 



class Medic(Character):
    def __init__(self, health, power):
        self.bounty = "10"
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
        






hero = Hero(25,4)
goblin = Goblin(6,2)
zombie = Zombie(50,1)
medic = Medic(30, 2)
shadow = Shadow(1,1)
warrior = Warrior(25,4)
mage = Mage(30, 3)




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
                print(f"{enemy.character_name} has been defeated.")
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

main(mage)















