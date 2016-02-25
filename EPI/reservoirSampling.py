import sys
import random

N = int(sys.argv[1])
sample = []

def reservoir_sampling(stream):
    for i, line in enumerate(input):
        if i < N:
            sample.append(line)
        elif i >= N and random.random() < N / float(i + 1):
            replace = random.randint(0, len(sample) - 1)
            sample[replace] = line

    for line in sample:
        sys.stdout.write(line)

def reservoir_sampling(input, k):
    samples = []
    for i in xrange(len(input)):
        if i < k:
            sample.append(input[i])
        elif i > k and random.random() < k / float(i + 1):
            replace = random.randint(len(sample) - 1)
            sample[replace] = input[i]

def random_subset( iterator, K ):
    result = []
    N = 0

    for item in iterator:
        N += 1
        if len( result ) < K:
            result.append( item )
        else:
            s = int(random.random() * N)
            if s < K:
                result[ s ] = item

    return result

def random_select(iterator):
    N = 0
    ans = 0
    for item in iterator:
        N += 1
        if random.random() < 1.0 / N:
            ans = item
    return ans
