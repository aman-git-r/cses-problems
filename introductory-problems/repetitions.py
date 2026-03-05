chars = input()
n = len(chars)

max_leng = 0
current = None
leng = 0

for i in range(n):
    if chars[i] == current:
        leng += 1
    else:
        leng = 1
        current = chars[i]
    max_leng = max(max_leng, leng)

print(max_leng)
