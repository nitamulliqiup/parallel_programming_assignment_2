import multiprocessing
from prime_numbers import PrimeNumbers

prime_object = PrimeNumbers()

primes_till = 10000000
primes = multiprocessing.Array('b',primes_till)
counter = 0
print('Parallel Programming Assignment 2')
print('*********************************')


def increase_counter(number):
    global primes
    global prime_object
    if prime_object.is_prime(number):
        primes[number-1] = True


pool = multiprocessing.Pool(processes=8)
pool.map(increase_counter, range(1, primes_till+1))

print(f'{primes[:].count(1)} prime numbers found from {1} till {primes_till}')
