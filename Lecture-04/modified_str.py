input_str = input("Enter string: ")

modified_str = ""

vowels = "aeiouAEIOU"

for char in input_str:
    upper_char = char.upper()
    if upper_char in vowels:
        modified_str += "*"
    else:
        modified_str += upper_char

print(f"Modified string : {modified_str}")
        