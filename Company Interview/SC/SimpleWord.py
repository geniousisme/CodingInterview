def simpleWords(words):
    word_dict = {}
    for word in words:
        word_dict[word] = 1
    res = []
    for i, word in enumerate(words):
        word_dict[word] = 0
        if not is_compound_word(word, word_dict):
            res.append(word)
        word_dict[word] = 1
    return res
    
def is_compound_word(word, word_dict):
    if not word:
        return False
    dp = [True]
    for i in xrange(1, len(word) + 1):
        dp.append(False)
        for j in xrange(i):
            if word_dict.get(word[j:i]) == 1 and dp[j]:
                dp[i] = True
                break
    return dp[-1]

if __name__ == "__main__":
    test1 = ['chat', 'ever', 'snapchat', 'snap', 'salesperson', 'per', 'person', 'sales', 'son', 'whatsoever', 'what', 'so']
    print simpleWords(test1)
    test2 = ['aaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'aaaaa']
    print simpleWords(test2)




