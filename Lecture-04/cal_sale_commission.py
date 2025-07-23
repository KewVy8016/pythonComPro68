is_going = "y"

while is_going.lower() == "y":
    sales = float(input("Enter the amount of sale: "))
    comm_rate = float(input("Enter commission rate : "))
    
    commission = sales * comm_rate

    print(f"The commission is {commission:,.2f} baht")

    is_going = input("Do you want to calculate another"+" "+"commission (Enter y or n): ")

print("End the program")