def is_prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n)):
        if n % j == 0:
            return False
    return True

