heroes = ["Ironman", "Thor", "Hulk", "superman", "spiderman"]
h2 = ["Doctor Strange", "Captain America", "Black panther", "Antman"]

heroes.insert(0,h2[0])
print(heroes)
heroes.append(h2[1])
print(heroes)
heroes.remove("superman")
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)