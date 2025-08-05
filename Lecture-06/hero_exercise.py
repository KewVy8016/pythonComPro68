heroes = ["Ironman", "Thor", "Hulk", "spiderman"]
is_typing = True


def Display_hero():
    return print(heroes)

def Add_hero(hero):
    heroes.append(hero)
    return print ("Add hero success")



while is_typing:
    print(f"1.DisplayHero\n2.Add Hero\n3.Insert Hero\n4.Remove Hero\n5.Display Sorted Heroes")

   