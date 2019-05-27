import time


def is_prime(n):
    for k in range(2, n):
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
    start = time.time()
    generate_primes(1000000)
    end = time.time()
    print(end - start)

