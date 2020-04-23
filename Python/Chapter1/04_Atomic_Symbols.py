'''
Split the sentence 
“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can.” 
into words, and extract the first letter from the 1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words 
and the first two letters from the other words. 
Create an associative array (dictionary object or mapping object) 
that maps from the extracted string to the position (offset in the sentence) of the corresponding word.

'''
import re

indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
origin_text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# splitの時に""が入るのは内包表記を使うと一度に書ける
new_text = [t for t in re.split(r'[ ,.]', origin_text) if t != ""]
cut_text = {}

# インデックスが欲しい時はenumerate使った方が綺麗（らしい）
for index, text in enumerate(new_text):
    if index + 1 in indexes:
        cut_text[index + 1] = text[:1:]
    else:
        cut_text[index + 1] = text[:2:]

print(cut_text)