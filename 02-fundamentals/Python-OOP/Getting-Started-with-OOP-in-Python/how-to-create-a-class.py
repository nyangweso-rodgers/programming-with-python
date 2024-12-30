class Soldier:
    health = 5
    
    def take_damage(self, damage):
        self.health -= damage
    
# to create an instance of a Soldier, we simply call the class
first_soldier = Soldier()
print(first_soldier.health)

first_soldier.take_damage(2)
print(first_soldier.health)
# prints "3"