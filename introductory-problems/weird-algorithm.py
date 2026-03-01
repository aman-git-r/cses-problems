n = int(input())
result = []
while n != 1:
    result.append(n)
    n = n // 2 if n % 2 == 0 else 3 * n + 1
print(*result)
