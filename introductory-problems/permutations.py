def beautiful(n: int):
    arr_even = []
    arr_odd = []
    if n == 1:
        print(1)
        return
    if n == 2 or n == 3:
        print("NO SOLUTION")
        return
    for i in range(1, n + 1):
        if i % 2 == 0:
            arr_even.append(i)
        else:
            arr_odd.append(i)
    if abs(arr_even[-1] - arr_odd[0]) > 1:
        arr_even.extend(arr_odd)
    else:
        print("NO SOLUTION")
        return 
    for item in arr_even:
        print(item, end=" ")

beautiful(int(input()))
