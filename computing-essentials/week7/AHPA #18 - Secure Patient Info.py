# AHPA #18 - Secure Patient Info
#
# Write a program that asks a user to
# enter the password in order to access 
# the data.
#
# If the password is entered 
# incorrectly 3 times in a row, raise a 
# ValueError exception and inform the 
# user that they are now locked out.
#
# If the password is correctly entered, 
# open the data file, parse the 
# records, and on separate lines print 
# the patient’s name (First, Middle, 
# Last) and their SS# with NO blank 
# lines between each line.
#
# Student Name: Evagelos Petropoulos
#
attempt = 0
print('You have 3 tries to input your password.')

#function for when the password is input correctly; 'opens the data file'
def open_file():
    first_name = input('What is your first name? ')
    middle_name = input('What is your midle name? ')
    last_name = input('What is your last name? ')
    social_security = input('What is your social security number? ')
    print('Here is your record: ' + first_name, middle_name, last_name, social_security)

#while the number of password attempts is less than 3, ask the user to input password
while attempt < 3:
    passcode = input('Password? ')
    if passcode == 'password':      # if input correctly, run function and exit loop
        print('Opening Data')
        open_file()
        break
    else:       #if input incorrectly, increment attempt and tell the user how many tries they have left
        attempt += 1
        print('Incorrect password,{0} attempts remaining.'.format((3 - attempt)))

#if attempt equals 3, raises an error with a message
if attempt == 3:
    raise ValueError('You are now locked out.')