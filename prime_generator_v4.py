import math


def sieve_of_eratosthenes(n):
    primes = [True for y in range(n+1)]
    upper_bound = int(math.sqrt(n)) + 1

    for j in range(2, upper_bound):
        if primes[j]:
            for k in range(j, n+1, j):
                primes[k] = False

    # Below Code outputs the prime numbers
    for k in range(2, len(primes)):
        if primes[k]:
            print(k, end=", ")


if __name__ == "__main__":
    sieve_of_eratosthenes(100)


