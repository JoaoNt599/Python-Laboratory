import math

def is_prime(n):

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

def find_primes(n):
    return [i for i in range(2, n) if is_prime(i)]


if __name__ == "__main__":
   pass