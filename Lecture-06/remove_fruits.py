fruits_with_duplicates = ["apple", "banana", "cherry", "apple", "banana","kiwi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"Fruits list after removing duplicates: {fruits_with_duplicates}")
