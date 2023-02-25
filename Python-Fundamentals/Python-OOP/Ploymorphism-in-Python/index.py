class Creature():
    def move(self):
        print("the creature moves")
        
class Dragon(Creature):
    def move(self):
        print("the dragon flies")
        
class Kraken(Creature):
    def move(self):
        print("the kraken swims")
        
for creature in [Creature(), Dragon(), Kraken()]:
    print(creature.move())
    
# In this example the child classes, Dragon and Kraken are overriding the behavior of their parent class's move() method.