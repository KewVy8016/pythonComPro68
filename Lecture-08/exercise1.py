with open("employee.txt", "r") as employee:
        lib_emplo = {}
        read = employee.readlines()
        print(len(read))
        counter = 0
        for i in range(0,3):
            co = 0
            print("out: ",i)
            for j in range(3):
                counter += 1 
                if counter == co:
                    
                    print("in: ",j)
                    print(f"Count: {counter}")
                
                        
            
        
            
        # print(f"Name: {name}, Id: {emp_id}, Dept: {dept}")
        
        
    