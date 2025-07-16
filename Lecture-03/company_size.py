employess = int(input("Enter total employees in your company: "))

if employess < 1:
    print("Invalid total employees")
elif employess <50:
    print("Your company is small-size")
elif employess < 250:
    print("Your company is medium-size")
elif employess >= 250:
    print("Your company is Large-size")