a = int(input('Enter num: '))
b = 286
sum = 0

if (a % 2 == 1):
    for num in range(a + 1, b + 1, 2):
        sum = sum + num
        if (sum > 100):
            break
else:
    for num in range(a, b + 1, 2):
        sum = sum + num
        if (sum > 100):
            break
    print("Sum is", sum)