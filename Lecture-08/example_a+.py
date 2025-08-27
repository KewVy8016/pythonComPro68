# Example using a+ mode (append and read)
def example_a_plus_mode():
    # Open the file for reading and writing (appending)
    with open('example_a+.txt', 'a+') as file:
        # Move the file pointer to the beginning to read the content
        file.seek(0)

        # Read the current content of the file
        content = file.read()
        print("Current content of the file:")
        print(content)

        # Append new content to the file
        file.write("Appending a new line at the end.\n")

        # Move the file pointer to the beginning again to read the updated content
        file.seek(0)
        updated_content = file.read()
        print("Updated content of the file:\n")
        print(updated_content)

example_a_plus_mode()