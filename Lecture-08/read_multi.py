import struct
with open("multi_record.bin","rb") as file:
    record_size = struct.calcsize("is20sif")
    while True:
        data = file.read(record_size)
        if not data or len(data) < record_size:
            break
        record = struct.unpack("is20sif",data)
        record = (record[0], record[1], record[2].decode().strip('\x00'), record[3])
        print(f"ID : {record[0]},Name: {record[1]},Age: {record[2]},GPA: {record[3]} ")