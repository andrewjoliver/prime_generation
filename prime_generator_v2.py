import math


def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def generate_primes(n):
    prime_list = list()
    for x in range(2, n):
        if is_prime(x):
            prime_list.append(x)
    print(prime_list)


if __name__ == "__main__":
    generate_primes(100)

