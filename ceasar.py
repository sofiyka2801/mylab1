alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
step = 1
text = input("текст:").strip()
res=''
for c in text:
    res += alpha[(alpha.index(c) +step)%len(alpha)]
print("результат:'" + res + "'")