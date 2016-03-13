# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_palindrome(string):
    start = 0; end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        else:
            start += 1; end -= 1
    return True

def palindrome_idx(string):
    start = 0; end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            if is_palindrome(string[:start] + string[start + 1:]):
                return start
            else:
                return end
        else:
            start += 1; end -= 1
    return -1

if __name__ == "__main__":
    case_num = int(raw_input())
    for i in xrange(case_num):
        print palindrome_idx(raw_input())
