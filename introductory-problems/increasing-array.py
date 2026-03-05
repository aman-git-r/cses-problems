n = int(input())
nums = list(map(int, input().split()))

moves = 0
for i in range(n):
    if i != 0 and nums[i] < nums[i - 1]:
        moves += nums[i - 1] - nums[i]
        nums[i] = nums[i - 1]
print(moves)


