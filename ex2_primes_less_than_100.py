from ex1_is_prime import is_prime

def primes_less_than_100():
    prime_lst = []
    for i in range(2, 100):
        if is_prime(i):
            prime_lst.append(i)

    return prime_lst