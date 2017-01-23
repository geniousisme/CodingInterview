import itertools


class BigInt(object):
    def __init__(self, num):
        if num == '':
            raise ValueError('Could not parse the value num')
        self.num = num

    def __str__(self):
        return self.num

    @staticmethod
    def _add_big_int(s1, s2):
        """
        s1 > 0   s2 > 0
        """
        carry = 0
        res = []
        for x, y in itertools.izip_longest(reversed(s1), reversed(s2), fillvalue='0'):
            r = int(x) + int(y) + carry
            carry = r / 10
            r %= 10
            res.append(r)
        if carry:
            res.append(carry)
        return ''.join(map(str, reversed(res)))

    @staticmethod
    def _substract_bit_int(s1, s2):
        """
        Make sure s1 > s2 > 0
        """
        carry = 0
        res = []
        for x, y in itertools.izip_longest(reversed(s1), reversed(s2), fillvalue='0'):
            x, y = int(x), int(y)
            y += carry
            if x < y:
                x += 10
                carry = 1
            else:
                carry = 0
            x -= y
            res.append(x)
        return ''.join(map(str, reversed(res))).lstrip('0') or '0'

    def __add__(self, other):
        x, y = self.num, other.num
        if not x.startswith('-') and not y.startswith('-'):
            return BigInt(self._add_big_int(x, y))
        if x.startswith('-') and y.startswith('-'):
            return BigInt('-' + self._add_big_int(x[1:], y[1:]))
        if x.startswith('-'):
            x = x[1:]
            if int(y) >= int(x):
                return BigInt(self._substract_bit_int(y, x))
            else:
                return BigInt('-' + self._substract_bit_int(x, y))
        else:
            y = y[1:]
            if int(x) >= int(y):
                return BigInt(self._substract_bit_int(x, y))
            else:
                return BigInt('-' + self._substract_bit_int(y, x))

    def __sub__(self, other):
        x, y = self.num, other.num
        if y.startswith('-'):
            y = y[1:]
        else:
            y = '-' + y
        return self + BigInt(y)


print BigInt('123') + BigInt('123')
print BigInt('999') + BigInt('1')
print BigInt('1000') + BigInt('-123')
print BigInt('123') + BigInt('-1000')
print BigInt('123') - BigInt('123')
print BigInt('0') - BigInt('123')
