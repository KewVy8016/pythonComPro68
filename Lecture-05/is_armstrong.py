def is_arm_strong(number):
    numbers = str(number)
    num_digit = len(numbers)
    total = 0

    for num in numbers:
        total += int(num)**int(num_digit)
        
    if int(number) == total:
        return print(f"True")
    else:
        return print("False") 
    

is_arm_strong(123)