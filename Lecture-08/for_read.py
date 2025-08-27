with open("example.txt","r") as file:
  lines = file.readline()
  for line in lines:
    print(line.strip())    