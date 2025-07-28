import random

Head = 1
Tails = 2
Tosses = 10

def toss_coin():
    for toss in range(Tosses):
        if random.randint(Head, Tails) == Head:
            print("Heads")
        else:
            print("Tails")
toss_coin()