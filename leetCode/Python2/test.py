def reverse_words(sentence):
    words_in_sentence = sentence.split()
    print ' '.join(reversed(words_in_sentence))

def reverse_words_in_place(sentence):
    char_list = list(sentence)
    start = 0
    for i in xrange(len(char_list)):
        if char_list[i] == ' ':
            reverse(char_list, start, i - 1)
            start = i + 1
    reverse(char_list, start, len(char_list) - 1)
    reverse(char_list, 0, len(char_list) - 1)
    print ''.join(char_list)

def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end   -= 1

if __name__ == '__main__':
    reverse_words_in_place("alice likes cats")