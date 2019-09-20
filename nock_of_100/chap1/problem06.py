def char_n_gram(n, sentence):
    words = list(sentence)
    tmp = ""
    res = []
    cnt = 0
    for i in range(len(words)):
        cnt = cnt + 1
        tmp += words[i]
        if cnt == n or i == len(words) - 1:
            res.append(tmp)
            tmp = ""
            cnt = 0
    return res

s1 = "paraparaparadise"
s2 = "paragraph"
x = char_n_gram(2, s1)
y = char_n_gram(2, s2)
print(x)
print(y)
wa = list(set(x) | set(y))
seki = list(set(x) & set(y))
sa = list(set(x) - set(y))
print(wa)
print(seki)
print(sa)
print("se" in x)
print("se" in y)
