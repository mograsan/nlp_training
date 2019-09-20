import random
sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
lst = sentence.split()
res = ""
for w in lst:
    print(w)
    if len(w) > 4:
        first = w[0]
        last = w[len(w)-1]
        tmp = list(w)
        tmp.pop(0)
        tmp.pop(len(tmp)-1)
        random.shuffle(tmp)
        after_word = ""
        after_word = first + "".join(tmp) + last
        res += " " + after_word
    else:
        res += " " + w

print(res)
