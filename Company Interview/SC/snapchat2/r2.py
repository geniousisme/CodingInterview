import heapq


def merge(files):
    heap = []
    # Initialization
    for f in files:
        try:
            line = f.next()
            string, count = line.split(',')
            count = int(count)
        except StopIteration:
            continue
        heapq.heappush(heap, (string, count, f))

    max_string, max_count = '', 0
    last_string, last_count = None, 0
    # Merge
    while heap:
        if heap[0][0] != last_string:
            # Find new String. Update result
            if last_count > max_count:
                max_string, max_count = last_string, last_count
            string, count, f = heapq.heappop(heap)
            last_string, last_count = string, count
        else:
            string, count, f = heapq.heappop(heap)
            last_count += count
        try:
            line = f.next()
            string, count = line.split(',')
            count = int(count)
            heapq.heappush(heap, (string, count, f))
        except StopIteration:
            continue

    if last_count > max_count:
        max_string, max_count = last_string, last_count

    return max_string, max_count


def generate_file(l):
    for i in l:
        yield i


f1 = generate_file(['a,200', 'b,9', 'c,100'])
f2 = generate_file(['a,3', 'c,90'])
f3 = generate_file([])
print merge([f1, f2, f3])