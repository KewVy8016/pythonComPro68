fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("grape")  #ใช้ลบสมาชิก โดยที่ไม่มีสมาชิกตรงกับ parameter ไม่เกิดข้อผิดพลาด
print(fruits)

remove_item = fruits.pop()
print(f"{remove_item}")
print(fruits)

fruits.clear()
print(fruits)