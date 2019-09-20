sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(",", "")
sentence = sentence.replace(".", "")
non_space = sentence.split()
res = []
for i in range(len(non_space)):
    res.append(len(non_space[i]))

print(res)
