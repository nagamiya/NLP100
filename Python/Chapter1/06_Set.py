'''
Let the sets of letter bi-grams from the words “paraparaparadise” and “paragraph” $X$ and $Y$, respectively.
 Obtain the union, intersection, difference of the two sets. In addition,
  check whether the bigram “se” is included in the sets $X$ and $Y$
'''

import re

def n_gram(text, n):
    ans = []
    for idx in range(len(text) - n + 1):
        ans.append(text[idx:idx+n])
    return ans
    


# 元のテキスト
text1 = "paraparaparadise"
text2 = "paragraph"

# 文字bigram
x = set(tuple(n_gram(text1, 2)))
print(type(x))
y = set(tuple(n_gram(text2, 2)))
print(type(y))

print(f"x >> {x}")
print(f"y >> {y}")
print(f"２つの和集合 >> { x | y}")
print(f"２つの積集合 >> { x & y}")
print(f"２つの差集合 >> { x - y}")

print(f"xにseが含まれるか >> { 'se' in x }")
print(f"yにseが含まれるか >> { 'se' in y }")