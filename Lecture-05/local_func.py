global_varieble = "I am local to my_function"

def my_function():
    print("Local scope: ",global_varieble)

my_function()
print("Global scope: ", global_varieble)