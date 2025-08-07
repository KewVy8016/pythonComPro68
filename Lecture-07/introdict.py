# ตัวอย่างการใช้งาน Dictionary ในภาษา Python

# สร้าง Dictionary สำหรับเก็บเบอร์โทรศัพท์
phonebook = {
    'Anirach': '777-1111',
    'Mickey': '777-2222',
    'Donald': '777-3333'
}

# แสดงข้อมูลทั้งหมดใน Dictionary
print(phonebook)

# ดึงค่าจาก key เฉพาะเจาะจง
print(phonebook['Mickey'])
print(phonebook.get('Donald'))

# ตรวจสอบ key ว่ามีอยู่ใน Dictionary หรือไม่
key = 'Pluto'
if key in phonebook:
    print(phonebook[key])
else:
    print(key + ' not in phonebook')

# เพิ่มหรือแก้ไขข้อมูลใน Dictionary
phonebook['Simpson'] = '777-4567'
phonebook['Pluto'] = '777-4444'
phonebook['Mickey'] = '777-2122'
print(phonebook)

# ลบข้อมูลจาก Dictionary
del phonebook['Simpson']
print(phonebook)