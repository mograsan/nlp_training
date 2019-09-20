s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(".", "")
list = s.split()
dict = {}
for i in range(len(list)):
    tmp_string = list[i]
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        dict[i] = tmp_string[0]
    else:
        dict[i] = tmp_string[0:2:1]
print(dict)
