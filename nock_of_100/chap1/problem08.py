def cipher(sentence):
    res = ""
    for c in sentence:
        if c.islower():
            res += chr(219 - ord(c))
        else:
            res += c
    return res

sentence = "UmplDzrhfprNrmtvm"
print(cipher(sentence))
