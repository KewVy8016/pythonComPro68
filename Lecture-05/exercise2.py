def generate_prime_number(num):
    result = []
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(i)
    return result

print(generate_prime_number(10))  