# AHPA #2 - Days Alive
#
# Write a Python program that will 
# have a variable set to a person's 
# age. It will then print out the 
# following statement:
# Hello, you have been alive for <x> days.
#
# Assume every year has 365 days. 
# No leap years.
#
# Remember to submit your work when 
# done
#
# Student Name: Evagelos Petropoulos
#
#enter in years in input, and input is changed to a float type
age_in_years = float(input('How many years have you been alive: '))

#years is converted to days
age_in_days = age_in_years * 365

#decided to incorporate a simple if else statement in case the user inputs a non-negative number
if (age_in_days >= 0):          #only prints string statement if value of age_in_days is greater than/equal to zero
    print('Hello, you have been alive for', f'{age_in_days:.1f}', 'days.')
else:                           #tells user to try again with an input that is greater than/equal to zero
    print('Please enter a non-negative number.')

