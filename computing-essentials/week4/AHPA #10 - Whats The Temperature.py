# AHPA #10 - What's The Temperature?

# Create a program that will allow a 
# user to tell what type of 
# temperature they will be entering 
# (F/C), then enter a temperature 
# that the facility can be set to, 
# and then convert that temperature 
# - to either Celsius or Fahrenheit.
#
# Student Name: Evagelos Petropoulos
#

#celsius to farenheit
#temp_of_F = temp_of_C * 1.8 + 32

#farenheit to celsius 
#temp_of_C = (temp_of_F - 32) / 1.8

def conversion():
    type_of_temp = input('What type of temperature are you entering, Farenheit or Celsius? Enter F or C. ')
    temperature = float(input('What degree is the temperature? '))
    if type_of_temp.upper() == 'F':
        temperature = (temperature - 32) / 1.8
        type_of_temp = 'Celsius'
    elif type_of_temp.upper() == 'C':
        temperature = (temperature * 1.8) + 32
        type_of_temp = 'Farenheit'
    
    print('Your converted temperature is {0:.2f} degrees {1}.'.format(temperature, type_of_temp))

conversion()