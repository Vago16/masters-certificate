#enter in values or range
a = int(input('Enter num: '))
b = int(input('Enter num: '))
#initialize sum
sum = 0

#first check if odd
if (a % 2 == 1):
    for num in range(a + 1, b + 1, 2): #if so, make min val and even number, and add 1 to b to make upper range inclusive, with step of two to keep to evens
        sum = sum + num
        print(num, sum)
        if (sum > 100):  #stop loop if sum goes over 100
            break
else:
    for num in range(a, b + 1, 2): #else, proceed as even, and add 1 to b to make upper range inclusive, with step of two to keep to evens
        sum = sum + num
        print(num, sum)
        if (sum > 100):
            break
    print("Sum is", sum)