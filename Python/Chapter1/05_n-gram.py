'''
Implement a function that obtains n-grams from a given sequence
object(e.g., string and list).
Use this function to obtain word bi-grams and letter-grams from
the sequence "I am an NLPer".
'''
import re


def n_gram(text, n):
    ans = []
    for idx in range(len(text) - n + 1):
        ans.append(text[idx:idx+n])
    return ans


text = "I am an NLPer"
# 文字bigram 
print(n_gram(text, 2))

# 単語bigram
print(n_gram(text.split(' '), 2))