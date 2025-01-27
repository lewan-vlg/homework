def is_prime(func):
    def wrapper(*args):
        total = func(*args)
        if total <= 1:
            print("Составное")
            return total
        for i in range(2, int(total ** 0.5) + 1):
            if total % i == 0:
                print("Составное")
                return total
        print("Простое")
        return total

    return wrapper
@is_prime
def sum_three(*args):
    total= sum(args)
    return total

result = sum_three(2, 3, 6)

print(result)