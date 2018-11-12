from math import floor, sqrt


class PrimeNumbers(object):
    def is_prime(self, number):
        if number == 0:
            return False
        elif number == 1 or number == 2 or number == 3:
            return True
        else:
            return number % 2 != 0 and number % 3 != 0 and self.is_prime_internal(number)

    def is_prime_internal(self, number):
        if number < 380000:
            squared = sqrt(number)
            floored_and_squared = floor(squared)
            for x in range(3, floored_and_squared +1):
                if number % x == 0:
                    return False
        else:
            divider = 6
            while divider*divider - 2*divider+1 <= number:
                if number % (divider-1) == 0:
                    return False
                if number % (divider + 1) == 0:
                    return False
                divider += 6

        return True
