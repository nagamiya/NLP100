'''
Implement a function cipher that converts a given string with the specification:

Every alphabetical letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
Keep other letters unchanged
Use this function to cipher and decipher an English message.
'''

def clipher(text):
    clipher_text = []
    for t in text:
        if str.islower(t):
            clipher_text.append(chr(219 - ord(t)))
        else:
            clipher_text.append(t)
    return "".join(clipher)


text = list(input())
encode = clipher(text)
print(encode)
decode = clipher(encode)
print(decode)
