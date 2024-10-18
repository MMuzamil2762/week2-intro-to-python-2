from ex1_is_prime import is_prime

def first_100_primes():
    first_100_pr = []
    n = 2
    while len(first_100_pr) < 100:
        if is_prime(n):
            first_100_pr.append(n)

        n += 1

    return first_100_pr

