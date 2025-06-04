def temp():
    n = int(input())
    s = input()
    house = []
    count = 0
    arr = [''] * n
    
    for i, j in enumerate(s):
        if j == 'H':
            arr[i] = 'H'
            count += 1
            if i == n - 1:
                house.append(count)
        else:
            arr[i] = 'B'
            if count > 0:
                house.append(count)
                count = 0

    if len(house) == 0 or max(house) == 1:
        print('YES')
        print(''.join(arr))
    else:
        print('NO')

# Call the function
temp()

