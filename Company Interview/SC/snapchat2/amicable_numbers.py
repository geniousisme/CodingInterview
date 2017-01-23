def sum_of_dividers(n):
    return sum(i for i in xrange(1,n/2+1) if n%i == 0)


def amicable_numbers(n):
    res = []

    for i in xrange(1, n+1):
        s1 = sum_of_dividers(i)
        if s1 > i:
            if sum_of_dividers(s1) == i:
                res.append((i, s1))
    return res


def amicable_numbers2(n):
    dp = [1] * (n+1)
    for d in xrange(2, n/2+1):
        for i in xrange(d+d, n+1, d):
            dp[i] += d
    res = []
    for i in xrange(1, n+1):
        s1 = dp[i]
        if i < s1 <= n:
            if dp[s1] == i:
                res.append((i, s1))
    return res


print amicable_numbers(4000)
print amicable_numbers2(4000)