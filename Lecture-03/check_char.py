inchar = input("Enter a character: ")

if inchar >= 'A' and inchar <= 'Z':
    print(f"The character is uppercase.{inchar}")
elif inchar >= 'a' and inchar <= 'z':
    print(f"The character is Lowercase.{inchar}")
elif inchar >= '0' and inchar <= '9':
    print(f"The character is number.{inchar}")
else:
    print("Is'n a letter or number")