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
