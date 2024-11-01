class Soldier:
    def __init__(self, armor, num_of_weapons):
        self.armor = armor
        self.num_of_weapons = num_of_weapons
        
soldier_one = Soldier(5, 10)
print(soldier_one.armor)
print(soldier_one.num_of_weapons)