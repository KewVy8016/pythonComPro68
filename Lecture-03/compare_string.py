str1 = "Mark"
str2 = "Mary"

if str1 == str2:
    print(f"{str1} and {str2} are eqaul ")
else:
    print(f"{str1} and {str2} are not eqaul ")

if str1 < str2:
    print(f"{str1} come before {str2} in lexicographical order")
elif str1 > str2:
    print(f"{str1} come after {str2} in lexicographical order")

if str1.lower() == str2.lower():
    print(f"{str1} and {str2} are eqaul when case is ignored ")
else:
    print(f"{str1} and {str2} are not eqaul when case is ignored ")
    