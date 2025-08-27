def main():
    infile = open('philosopher.txt','r')
    
    file_contents = infile.read()
    
    infile.close()
    
    print(file_contents)

main()