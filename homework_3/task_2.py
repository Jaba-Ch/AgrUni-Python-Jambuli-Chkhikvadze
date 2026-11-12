import random

suits = ['♣', '♦', '♥', '♠']
values = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

suit = random.choice(suits)
value = random.choice(values)
print(f"{suit}{value}")