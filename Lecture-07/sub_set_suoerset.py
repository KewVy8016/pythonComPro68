set_a = {1, 2, 3, 4}
set_b = {1, 2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 5}

print("Is set_a a subset of set_b?", set_a >= set_b)  # Output: False
print("Is set_b a subset of set_a?", set_b <= set_a)  # Output: True

print("Is set_a a superset of set_b ?", set_a >= set_b)  # Output: True
print("Is set_a a superset of set_a?", set_b < set_a)  # Output: True

print("Area set_a and set_c equal?", set_a == set_c)  # Output: False

print("Is set_b a subset of set_d and not equal?", set_b <= set_a and set_d != set_b)  # Output: True