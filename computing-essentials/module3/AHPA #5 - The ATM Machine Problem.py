# AHPA #5 - The ATM Machine Problem
#
# Create software that will provide 
# an ATM user with the proper change 
# for any dollar amount up to $200.

# Example: Run the code for $19, 
# $55, and $200.
#
# Student Name: Evagelos Petropoulos
#
#gets user input and changes string into an integer
cash_withdrawn = int(input('How much money(max is $200) do you wish to withdraw from the ATM? '))

#initialize variable for change
change_for_hundred_bills = 0
change_for_twenty_bills = 0
change_for_ten_bills = 0
change_for_five_bills = 0
change_for_one_bills = 0

if (cash_withdrawn > 200):          #value for cash_withdrawn cannot be over 200
    print('Please enter an amount less than $200.')
elif (cash_withdrawn == 200):
    change_for_hundred_bills = 2
elif (cash_withdrawn > 100):
    change_for_hundred_bills = 1
    change_for_ten_bills = (cash_withdrawn % 100) // 10     #get remainder and floor division to get change
    change_for_one_bills = cash_withdrawn % 10
elif (cash_withdrawn == 100):
    change_for_hundred_bills = 1
elif (0 < cash_withdrawn < 100):
    change_for_ten_bills = (cash_withdrawn % 100) // 10
    change_for_one_bills = cash_withdrawn % 10

#since ten and one dollar bills are factors of twenty and five bills respectfully
#we need to floor divide to get the values for them if they exist, and then change the value of the factors to reflect that

if (change_for_ten_bills >= 2):                            
    change_for_twenty_bills = change_for_ten_bills // 2     
    change_for_ten_bills = change_for_ten_bills - (change_for_twenty_bills * 2) 

if (change_for_one_bills >= 5):
    change_for_five_bills = 1
    change_for_one_bills = change_for_one_bills - (change_for_hundred_bills * 5)




print('Here is your change: {0} hundred dollar bills, {1} twenty dollar bills, {2} ten dollar bills, {3}  five dollar bills, {4} one dollar bills'
      .format(change_for_hundred_bills,change_for_twenty_bills,change_for_ten_bills,change_for_five_bills,change_for_one_bills))