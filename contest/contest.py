f = open("file.txt", "r")

aa = "aeiou"
a = ' abcdefghijklmnopqrstuvwxyz'

text = ""
for i in f:
    total = 0
    for j in i:
        if j in aa:
            total += 1
    text += a[total]

print(text)
