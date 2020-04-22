"""
Split the sentence “Now I need a drink, alcoholic of course,
after the heavy lectures involving quantum mechanics.” into words,
and create a list whose element presents the number of alphabetical letters in the corresponding word.
"""

import re

origin_text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# 正規表現で区切る　-> splitの結果で空文字列が入っているので注意
new_text = re.split(r'[ ,.]', origin_text)
print(new_text)

for text in new_text:
    if text != "" :
        print(f"{len(text)} ", end="")

print()