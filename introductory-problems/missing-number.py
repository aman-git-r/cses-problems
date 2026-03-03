n = int(input())
nums = list(map(int, input().split()))
arr = [0] * (n + 1)
for num in nums:
    arr[num] = 1
for i in range(1, (n + 1)):
    if arr[i] == 0:
        print(i)
        break
