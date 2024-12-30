# Here is how to flip a coin where heads is twice as likely as an ouput as tails.

import random
faces = ["heads", "tails"]
weights = [2, 1] # heads is twice as likely as tails
print(random.choices(faces, weights, k = 10))