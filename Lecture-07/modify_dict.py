# Creating a dictionary
student = {"name": "Alice", "age": 25, "grade": "A"}

# Adding and updating values
student["age"] = 26
student["major"] = "Computer Science"
print(student)  # Output: {'name': 'Alice', 'age': 26, 'grade': 'A', 'major': 'Computer Science'}

# Removing a key-value pair using del
del student["grade"]
print(student)  # Output: {'name': 'Alice', 'age': 26, 'major': 'Computer Science'}

# Removing a key-value pair using pop and getting the removed value
removed_major = student.pop("major")
print(removed_major)  # Output: 'Computer Science'
print(student)        # Output: {'name': 'Alice', 'age': 26}