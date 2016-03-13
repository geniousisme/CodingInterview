def add1(x, y): # iterative
    # carry = sum = 1
    while x:
        sum   = x ^ y;
        carry = x & y;
        x     = carry << 1;
        y     = sum;
    return y

def add(x, y): # recursive
    if y == 0:
        return x
    sum = x ^ y
    carry = (x & y) << 1
    return add(sum, carry)

if __name__ == "__main__":
    print add(3, 4)
    print add(2, 99)
    print add(2, 9)
    print add(100, -100)


