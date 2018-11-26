import multiprocessing
from prime_numbers import PrimeNumbers

prime_object = PrimeNumbers()

primes_till = 100000000
primes = multiprocessing.Array('b',primes_till)
counter = 0
print('Parallel Programming Assignment 2')
print('*********************************')


def increase_counter(number):
    global primes
    global prime_object
    if prime_object.is_prime(number):
        primes[number-1] = True


running = True
while running:
    primes_till = eval(input("Enter max number: "))
    processors_count = multiprocessing.cpu_count()
    chosen_processors = eval(input(f'Chose number of processors from 1 to {processors_count}: '))
    print(f'Calculating with {chosen_processors} processors...')
    pool = multiprocessing.Pool(processes=5)
    pool.map(increase_counter, range(1, primes_till + 1))
    prime_count = primes[:].count(1)
    print(f'{prime_count} prime numbers found from {1} till {primes_till}')
    end_response = input("Do you want to continue? (Y/N): ")
    if end_response not in ('Y', 'y'):
        running = False

print('*********************************')
