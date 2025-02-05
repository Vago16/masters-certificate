#Create a program that computes the average of a set of salary values.

#In our sample program, we will use 
# any negative value as the sentinel.
#Any negative number can end the loop, but we prompt for a sentinel of –1 
# so that the user need not ponder which negative number to enter.

#initializing variables
salary = 0
total = 0
count = 0

while (salary >= 0):
    salary = int(input('Please enter salary(-1 to stop): '))    #-1 is the sentinel val; less than 0 so stops loop
    if (salary > 0):
        total += salary     #adding together salaries
        count += 1          #incrementing every time a salary is input

print(f'Average salary = {total / count}')



