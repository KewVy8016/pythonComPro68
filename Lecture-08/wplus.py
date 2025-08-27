def exampale_w_plus_mode():
    with open("exampale_w+.txt","w+") as file:
        file.write("This is the first line in the file.\n")
        file.write("This is the seconds line in the file.\n")
        
        file.seek(0)
        content = file.read()
        print("Content of this file")
        print(content)

exampale_w_plus_mode()