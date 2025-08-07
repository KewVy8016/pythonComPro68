def longest_unique_word_sequence(words: list[list[str]]) -> tuple:
    # function set เเปลง list เป็น set
    flattened_words = [word for sublist in words for word in sublist]

    max_length = 0
    result = []
    
    left = 0
    word_set = set()
    
    # 2. Use the Sliding Window technique
    for right in range(len(flattened_words)):
        current_word = flattened_words[right]
        
        # If the word is already in the current window, shrink the window from the left
        while current_word in word_set:
            word_set.remove(flattened_words[left])
            left += 1
        
        # Add the new word to the window
        word_set.add(current_word)
        
        # Get the length of the current window
        current_length = right - left + 1
        
        # 3. Update the results based on the current length
        if current_length > max_length:
            max_length = current_length
            result = [flattened_words[left:right + 1]]
        elif current_length == max_length:
            result.append(flattened_words[left:right + 1])
            
    return (max_length, result)




    
words = [["apple", "banana"], ["apple"], ["cherry", "banana"]]
print(longest_unique_word_sequence(words))
# ผลลัพธ์: (3, [['banana', 'apple', 'cherry'], ['apple', 'cherry', 'banana']])

words2 = [["dog", "cat"], ["mouse", "cat"], ["bird", "dog"]]
print(longest_unique_word_sequence(words2))
# ผลลัพธ์: (4, [['mouse', 'cat', 'bird', 'dog']])
