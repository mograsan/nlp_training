def word_n_gram(n, sentence):
    words = sentence.split()
    tmp = ""
    res = []
    cnt = 0
    for i in range(len(words)):
        cnt = cnt + 1
        tmp += words[i]
        if cnt == n or i == len(words) - 1:
            res.append(tmp)
            tmp = " "
            cnt = 0
    return res


def char_n_gram(n, sentence):
    words = list(sentence)
    words = [s for s in words if s != " "]
    tmp = " "
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

s = "I am an NLPer"
wng = word_n_gram(2, s)
print(wng)

cng = char_n_gram(2, s)
print(cng)
