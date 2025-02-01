# AHPA #8 - Titration Time!
# 
# You are a Chemistry major who has to create 
# a program for first time Chem lab users.
#
# The Erlenmeyer flask contains a nitric acid 
# solution.
#
# When the student presses a button, a 0.5 ml 
# NaOH solution can be added to a buret, which 
# is set up over the Erlenmeyer flask.
# 
# An indicator is added to the solution being 
# titrated. The indicator is a substance that 
# changes to blue when the reaction is 
# complete (endpoint).	 You determine the 
# amount of mixture that will cause this 
# reaction to occur.
# 
# Create a titration simulator that will allow 
# a student to add up to 18 ml of titrant. 
# 
# Notify the student when the mixture turns 
# blue.
#
# Student Name: Evagelos Petropoulos

curr_amount = 0
add_amount = 0.5
button_press = 0

end_amount = int(input('How many mls (max 18) should the mixture require to turn blue? '))

while (curr_amount < end_amount):
    button_press += 1   #increment to show how many times button has been presses
    curr_amount += add_amount
#    print(curr_amount, add_amount) used in testing to make sure values were adding up correctly
    if (curr_amount > 18):
        print('Solution did not turn blue before 18 mls was added.')
        break
    if (curr_amount == end_amount):
        print('Suolution turned blue.')

print(f'Button was pressed {button_press} times.')