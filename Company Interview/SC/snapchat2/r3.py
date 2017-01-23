def print_line(cur_line, width):
    if len(cur_line) == 1:
        print cur_line[0]
        return
    total_spaces = width - sum(map(len, cur_line))
    intervals = len(cur_line) - 1

    res = ''
    base = total_spaces / intervals
    for i in xrange(total_spaces % intervals):
        res += cur_line[i] + ' ' * (base+1)
    for i in xrange(total_spaces % intervals, intervals):
        res += cur_line[i] + ' ' * base
    res += cur_line[-1]
    print res


def text_justification(input_str, width):
    print '=' * 50
    tokens = input_str.split()

    cur_line = []
    cur_length = 0

    for token in tokens:
        if cur_length + len(token) > width:
            print_line(cur_line, width)
            cur_line = []
            cur_length = 0

        cur_line.append(token)
        cur_length += (1 + len(token))

    print_line(cur_line, width)


text_justification('where', 19)
text_justification('where is', 5)
text_justification('where is', 8)
text_justification('where is it', 14)
text_justification('where is the way', 8)
text_justification('where is the way', 9)
text_justification('where is the way', 12)


