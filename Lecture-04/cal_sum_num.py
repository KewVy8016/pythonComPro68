max = 5 

total = 0.0
print("This program calculate the sum of : ")
print(max,"numbers your will enter.")

for counter in range(max):
    number = int(input("Enter a numeber : "))
    total = total + number
print ("The total is ", total)