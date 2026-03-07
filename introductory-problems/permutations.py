def beautiful(n: int):
    if n == 1:
        print(1)
        return
    if n == 2 or n == 3:
        print("NO SOLUTION")
        return

    arr_even = []
    arr_odd = []
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            arr_even.append(i)
        else:
            arr_odd.append(i)
    result = arr_even + arr_odd 
    print(*result, end="")

beautiful(int(input()))
