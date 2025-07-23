
is_going = "y"
whole_sale = float(input("Enter whole sale: "))

while is_going.lower() == "y":
    retail_price = whole_sale * 2.5
    print(f"Whole sale price: {whole_sale:.2f}")
    print(f"Retail price: {retail_price:.2f}")
    is_going = input("Do you have another item: (enter y for yes)")