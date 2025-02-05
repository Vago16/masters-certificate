# AHPA #6 - The Challenge Of Being Kim Kardashian

# Create a Python program that will 
# ask the user what color pants Kim 
# will be wearing and what time it 
# is. The program will then tell 
# Kim what color shoes to wear and 
# where she should go.
#
# Student Name: Evagelos Petropoulos
#

#SHOES part

#added strip and lower method so if the user inputs space at beginning or end or has different capitalization than code it will still run
color_pants = input(str('What color are the pants that Kim has decided to wear? ')).strip().lower()
shoes = ''

#if else statement for shoes matching with pants
if (color_pants == 'white'): shoes = 'white stilettos'
elif (color_pants == 'black'): shoes = 'blue wedges'
elif (color_pants == 'green'): shoes = 'green Mary Jane shoes'
elif (color_pants == 'yellow'): shoes = 'orange pumps'
else: shoes = 'brown flats'

#DESTINATION part
time = int(input('What time is it? '))
destination = ''

#if a value greater than or equal to 12 is selected, Kim is said to go home and a statement is printed asking the user to select a different time
if (time < 1): destination = 'to the beach'
elif (time < 2): destination = 'to lunch at La Petite'
elif (time < 4): destination = 'to get her nails done at Tips R Us'
elif (time < 6): destination = 'to the Flat Tummy gym'
elif (time < 8): destination = 'home to get ready to go out'
elif (time < 9): destination = 'to Racks & Stacks BBQ'
elif (time < 11): destination = 'see a movie at The 24 Hour Multiplex'
elif (time < 12): destination = 'hit the club at \"The Backdoor\"'
else:           
    destination ='home'
    print('Please select a time before 12 am.')

print('Kim is wearing her {0} to go {1}.'.format(shoes,destination))