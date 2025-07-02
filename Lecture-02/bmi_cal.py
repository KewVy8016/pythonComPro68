weight = int(input("Enter your weight in kg: "))
height_cm = int(input("Enter your height in centimeter: "))

height_m = height_cm / 100  
cal_bmi = weight / (height_m * height_m)
print(f"your bmi is : {cal_bmi:.2f}")
