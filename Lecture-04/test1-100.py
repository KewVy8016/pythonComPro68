rows = int(input("Enter row: "))
max_number = 100 

numbers_per_full_row = max_number // rows
remaining_numbers = max_number % rows

current_number = 1 

for row_index in range(rows):
    current_numbers_in_this_row = numbers_per_full_row + 1 if row_index < remaining_numbers else numbers_per_full_row
    
    for _ in range(current_numbers_in_this_row):
        print(current_number, end=" ")
        current_number += 1 
    
    print() 