work_time =  int(input("Enter work time in hours: "))
pay_rate = int(input("Enter pay rate: "))

if work_time <= 40:
    print (f"The gross pay is {work_time*pay_rate}")
else:
    overtime = work_time - 40
    gross_pay = (40 * pay_rate) + (overtime * pay_rate * 1.5)
    print(f"The gross pay is ${gross_pay:,.2f}")
    