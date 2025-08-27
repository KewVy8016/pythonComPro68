import struct
num_record  = int(input("How many cord do you want yo create? : "))

with open ("multi_record.bin","wb") as file:
    for _ in range(num_record):
        id_num = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gpa = float(input("Enter gpa: "))
        data = struct.pack("i20sif", id_num, name.encode(), age, gpa)
        file.write(data)
print(f"{num_record} record have been written to multi_record.bin")
        