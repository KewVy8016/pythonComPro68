try:
    value = int(input("Enter a numeber: "))
    result = 10/value
except ValueError:
    print("Invalid input ! Please enter number.")
except:
    print("Can not divide zero!")


print("End of program")