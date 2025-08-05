inventory = [
    ["Apple",50,0.75],
    ["Banana",100,0.50],
    ["Orange",75,0.80],
]


def update_inventory(inventory,item_name,quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            print (item)

def cal_total():
    total = 0
    for item in inventory:
       total += item[1]
    return total

def find_expensive():
    max_price = 0
    max_name = None
    for item in inventory:
        if item[2] > max_price:
            max_price = item[2]
            max_name = item[0]
    return max_price,max_name



Ischoice = True
last_command = ""
while Ischoice:
    print(f"Menu 1:update 2:calculate 3:Most expensive 4:cancel")
    print(f"Last command: {last_command} ")
    print(f"show inventory: {inventory}")
    choice = int(input("Enter choice: "))
    if choice == 1:
        item_name = input("Enter item name: ")
        sold = input("Enter sold quantity: ")
        update_inventory(inventory,item_name,int(sold))
        last_command = f"Update {item_name} sold:{sold}"
        print("update")
    
    if choice == 2:
        print("calculate total value:",cal_total())

    if choice == 3:
        price,name = find_expensive()
        last_command = f"Most expensive is {name} = {price} Baht"
 
    if choice == 4:
        Ischoice = False
        print("cancel")