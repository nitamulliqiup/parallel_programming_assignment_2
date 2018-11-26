import multiprocessing
import datetime
from prime_numbers import PrimeNumbers

prime_object = PrimeNumbers()

primes_till = 100000000
counter = 0
print('Parallel Programming Assignment 2')
print('*********************************')


def increase_counter(number):
    global primes
    global prime_object
    if prime_object.is_prime(number):
        primes[number-1] = True


running = True
table = []
while running:
    primes = multiprocessing.Array('b', primes_till)
    primes_till = eval(input("Enter max number: "))
    processors_count = multiprocessing.cpu_count()
    chosen_processors = eval(input(f'Chose number of processors from 1 to {processors_count}: '))

    if chosen_processors not in range(1, processors_count + 1):
        print(f'You chose {chosen_processors}, '
              f'that is not included in the expected range! We are proceeding with the maximum power.')
        chosen_processors = processors_count

    print(f'Calculating with {chosen_processors} processors...')

    pool = multiprocessing.Pool(processes=chosen_processors)
    start_time = datetime.datetime.now()
    pool.map(increase_counter, range(1, primes_till + 1))
    prime_count = primes[:].count(1)
    end_time = datetime.datetime.now()

    print(f'{prime_count} prime numbers found from {1} till {primes_till}')
    end_response = input("Do you want to continue? (Y/N): ")

    diff = end_time - start_time
    minutes = int((diff.seconds // 60) % 60)
    result = {"Number": primes_till, "Processors": chosen_processors, "Start Time": start_time.strftime("%H:%M:%S"),
              "End Time": end_time.strftime("%H:%M:%S"), "Primes found": prime_count,
              "Duration in minutes":minutes, "Duration in seconds": diff.seconds}
    table.append(result)
    if end_response not in ('Y', 'y'):
        running = False

print('*********************************')
print('Displaying Results')
for row in table:
    print(row)


