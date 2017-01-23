from collections import Counter
from collections import defaultdict


def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)


def any_substr_anagram(s, p):
    """
    give a source string s and pattern string p, find if any substring of s
    is anagram of p.
    """
    if not p:
        return ''
    counter = Counter(p)
    k = len(counter)
    window = defaultdict(int)

    low, high = 0, 0
    while high < len(s):
        if s[high] not in counter:
            low = high = high + 1
            window = defaultdict(int)
            k = len(counter)
            continue

        window[s[high]] += 1
        if window[s[high]] == counter[s[high]]:
            k -= 1
            if k == 0:
                return s[low:high+1]
        elif window[s[high]] > counter[s[high]]:
            while low < high and s[low] != s[high]:
                if window[s[low]] == counter[s[low]]:
                    k -= 1
                window[s[low]] -= 1
                low += 1
            window[s[low]] -= 1
            low += 1
        high += 1
    return ''

print any_substr_anagram('acd', 'dc')
print any_substr_anagram('aaaaaaaaxtxbxyaaaaaaaaa', 'xbxxy')
print any_substr_anagram('aaaaaaaaxxbxyaaaaaaaaa', 'xbxxy')