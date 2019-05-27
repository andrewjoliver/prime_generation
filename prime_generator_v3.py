from sympy.ntheory import isprime


def generate_primes(n):
    prime_list = list()
    for x in range(2, n):
        if isprime(x):
            prime_list.append(x)
    print(prime_list)


if __name__ == "__main__":
    generate_primes(100)

