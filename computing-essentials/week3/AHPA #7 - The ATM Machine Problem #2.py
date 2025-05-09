# AHPA #7 - The ATM Machine Problem #2

# Create software that will provide 
# an ATM user with the proper
# change for any dollar amount.

# Create two separate solutions: 
# one that uses a While loop and 
# one that uses a For loop.

# Example: run the code for $1917,
# $550, and $23.
#
# Student Name: Evagelos Petropoulos
#
cash_withdrawn = int(input('How much money(while loop) do you wish to withdraw from the ATM? '))
#initialize variable for change
change_for_hundred_bills = 0
change_for_ten_bills = 0
change_for_one_bills = 0

#While loop
while (cash_withdrawn >= 1):
    if (cash_withdrawn >= 100):
        change_for_hundred_bills = cash_withdrawn // 100
        cash_withdrawn = cash_withdrawn % 100
    elif (cash_withdrawn >= 10):
        change_for_ten_bills = cash_withdrawn // 10
        cash_withdrawn = cash_withdrawn % 10
    elif (cash_withdrawn >= 1):
        change_for_one_bills = cash_withdrawn
        cash_withdrawn = cash_withdrawn - cash_withdrawn



print('Here is your change: {0} hundred dollar bills, {1} ten dollar bills,  {2} one dollar bills'
      .format(change_for_hundred_bills, change_for_ten_bills,change_for_one_bills))

#For loop
cash_withdrawn_for = int(input('How much money(for loop) do you wish to withdraw from the ATM? '))

print('Here is your change: ', end = '')

#the +1 is to be inclusivw of the last val of cash_withdrawn_for
for i in range(cash_withdrawn_for + 1):
    if (cash_withdrawn_for >= 100):
        print(cash_withdrawn_for // 100, 'hundred dollar bills', end=' ')
        cash_withdrawn_for = cash_withdrawn_for % 100
    elif (cash_withdrawn_for >= 10):
        print(cash_withdrawn_for // 10, 'ten dollar bills', end=' ')
        cash_withdrawn_for = cash_withdrawn_for % 10
    elif(cash_withdrawn_for >= 1):
        print(cash_withdrawn_for, 'one dollar bills')
        cash_withdrawn_for = cash_withdrawn_for - cash_withdrawn_for



#previous try for the for loop that did not work, took me like 3-4 hours of brainstorming trying different methods to come up with current solution
'''cash_for_loop = int(input('How much money(for loop) do you wish to withdraw from the ATM? '))
sum = 0
change_for_hundred_bills_for = 0
change_for_ten_bills_for = 0
change_for_one_bills_for = 0

if cash_withdrawn < 0:
    print('Enter positive Amount.')
else:
    for cash in range(0, cash_for_loop + 1):
        sum += 1
        if (sum >= 100):
            change_for_hundred_bills_for = sum // 100
            sum = sum % 100
        elif (sum >= 10):
            change_for_ten_bills_for = sum // 10
            sum = sum % 10
        elif (sum >= 1):
            change_for_one_bills_for = sum
            sum = sum - sum
    print('{0} hundred dollar bills, '.format(change_for_hundred_bills_for, end=''))
    print('{0} ten dollar bills, '.format(change_for_ten_bills_for, end=''))
    print('{0} one dollar bills'.format(change_for_one_bills_for, end=''))'''




