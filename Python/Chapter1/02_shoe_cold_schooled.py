# "shoe"と"cold"を一文字ずつ順番に合わせた文字列を出力
text1 = "shoe"
text2 = "cold"

""" 
    ・"間に挟みたい文字列とか".join([リスト])
    ・ループでオブジェクト複数使いたいときはzipを使う
    ・なんでstr(char1 + char2)を入れるとforのところのエラーが消えたのかわかってない
    →
"""
ans = "".join([str(char1 + char2) for char1, char2 in zip(text1, text2)])
print(ans)