with open("example.txt","w") as file:
    file.write("Hello world\n")
    file.write("This is a new line.\n")
    
with open("example.txt","a") as file:
    file.write("This is an append line\n")

with open("example.txt","r") as file:
    contents = file.read()
    print(contents)
    
