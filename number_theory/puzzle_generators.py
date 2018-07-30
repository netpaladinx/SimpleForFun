import random

class PuzzleForInteger(object):
    def __init__(self, N=100):
        for i in xrange(N):
            x = random.randint(-9999, 9999)
            assert self._is_integer(x), "not integer"
            o = {
                '_is_even': self._is_even(x),
                '_is_multiple_of_3': self._is_multiple_of_3(x),
                '_is_multiple_of_4': self._is_multiple_of_4(x),
                '_is_multiple_of_5': self._is_multiple_of_5(x),
                '_is_multiple_of_6': self._is_multiple_of_6(x),
                '_is_multiple_of_7': self._is_multiple_of_7(x),
                '_is_multiple_of_8': self._is_multiple_of_8(x),
                '_is_multiple_of_9': self._is_multiple_of_9(x),
                '_is_multiple_of_10': self._is_multiple_of_10(x),
                '_is_multiple_of_11': self._is_multiple_of_11(x),
                '_last_digit': self._last_digit(x),
                '_last_two_digits': self._last_two_digits(x),
                '_last_three_digits': self._last_three_digits(x),
                '_last_digit_removed': self._last_digit_removed(x),
                '_sum_of_digits': self._sum_of_digits(x),
                '_sum_of_digits_on_even_positions': self._sum_of_digits_on_even_positions(x),
                '_sum_of_digits_on_odd_positions': self._sum_of_digits_on_odd_positions(x)
            }
            print(x)
            print(o)


    def _is_integer(self, x):
        return isinstance(x, int)

    def _is_even(self, x):
        return x % 2 == 0

    def _is_multiple_of_3(self, x):
        return x % 3 == 0

    def _is_multiple_of_4(self, x):
        return x % 4 == 0

    def _is_multiple_of_5(self, x):
        return x % 5 == 0

    def _is_multiple_of_6(self, x):
        return x % 6 == 0

    def _is_multiple_of_7(self, x):
        return x % 7 == 0

    def _is_multiple_of_8(self, x):
        return x % 8 == 0

    def _is_multiple_of_9(self, x):
        return x % 9 == 0

    def _is_multiple_of_10(self, x):
        return x % 10 == 0

    def _is_multiple_of_11(self, x):
        return x % 11 == 0

    def _last_digit(self, x):
        return abs(x) % 10

    def _last_two_digits(self, x):
        return abs(x) % 100

    def _last_three_digits(self, x):
        return abs(x) % 1000

    def _last_digit_removed(self, x):
        return abs(x) / 10

    def _sum_of_digits(self, x):
        x = abs(x)
        s = 0
        while x > 0:
            s += x % 10
            x /= 10
        return s

    def _sum_of_digits_on_even_positions(self, x):
        x = abs(x)/10
        s = 0
        while x > 0:
            s += x % 10
            x /= 100
        return s

    def _sum_of_digits_on_odd_positions(self, x):
        x = abs(x)
        s = 0
        while x > 0:
            s += x % 10
            x /= 100
        return s

if __name__ == "__main__":
    PuzzleForInteger()