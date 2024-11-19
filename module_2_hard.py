def generate_password(n):
    result = ""
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                pair_str = f"{i}{j}"
                if pair_str not in pairs:
                    pairs.append(pair_str)
                    result += pair_str

    return result


for test_number in range(3, 21):
    password = generate_password(test_number)
    print(f"{test_number} - {password}")