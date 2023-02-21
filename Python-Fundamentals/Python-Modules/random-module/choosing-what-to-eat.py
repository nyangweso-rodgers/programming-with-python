from random import seed, choice 
counter = 1  # += 1 every time the script is run.. 
coin_throws = 0b1  # To be extended one bit at a time 
lottery_numbers = 1345443315  # It's your lucky numbers! 
seed((coin_throws^lottery_numbers)*counter) 
choices = ["Liver + Ugali", "Spinach + Ugali + Mala", "Pilau + Meat", "Fish + Ugali + Spinach", "Spagetti + Eggs"] 
print("today we will eat", choice(choices)) 