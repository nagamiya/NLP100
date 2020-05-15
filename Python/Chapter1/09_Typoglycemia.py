'''
Write a program with the specification:

Receive a word sequence separated by space
For each word in the sequence:
If the word is no longer than four letters, keep the word unchanged
Otherwise,
Keep the first and last letters unchanged
Shuffle other letters in other positions (in the middle of the word)
Observe the result by giving a sentence, e.g., “I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”
'''

import random

def random_sort(text):
    task = list(text)
    head = task[0]
    body = task[1:-1]
    tail = task[-1]
    return head + "".join(random.sample(body, len(body))) + tail


text = input()
if (len(text) > 4):
    print(random_sort(text))
else:
    print(text)