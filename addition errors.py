m = int(input())
for _ in range(m):
    a = input()
    b = input()
    temp = 0
    value = 10
    for i in range(-1, (len(str(min(int(a), int(b)))) + 1) * -1, -1):
        if int(a[i]) + int(b[i]) >= 10:
            temp += value
        value *= 10
    print(temp)
