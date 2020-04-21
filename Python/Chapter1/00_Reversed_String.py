# “stressed”を逆にする
origin_text = "stressed"
# -1だから逆順、1だと通常順（？）、順番変わらんやつ
new_text = origin_text[::-1]
print("original text: %s\nnew text: %s" % (origin_text, new_text) )