def staircase(stair_num):
    for level in xrange(1, stair_num + 1):
        print " " * (stair_num - level) + "#" * level

if __name__ == '__main__':
    number = input()
    staircase(number)
