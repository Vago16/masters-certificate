# Module 1 Topic 1 Assignment
# Procedural Programming
# Evagelos Petropoulos
# U75564437

#This program uses procedural programming to track three types of vaccines in a population represented by 15 individuals


#number of individuals
NUM_INDIVIDUALS = 15

#initialize the vaccines(0 is a no for the particular vaccine and 1 is a yes)
vac_a = [0] * NUM_INDIVIDUALS
vac_b = [0] * NUM_INDIVIDUALS
vac_c = [0] * NUM_INDIVIDUALS


def print_menu():
    #displays the program's menu of options
    print()
    print('Press i to input data for each individual')
    print('Press r to report vaccination data for an individual')
    print('Press v to report vaccination totals for each vaccine type')
    print('Press q to quit')
    print()

def input_data():
    #inputs data for each vaccine(0 is a no for the particular vaccine and 1 is a yes)
    for i in range(NUM_INDIVIDUALS):
        print('Enter in the vaccination data for individual {0} (0 for no, 1 for yes):'.format(i + 1))
        while True:     #keep looping until there is a valid integer input
            try:
                vac_a[i] = int(input('  Does the individual have vac_a? '))
                if vac_a[i] != 0 and vac_a[i] != 1:     #in case the user inputs an integer that is not 0 or 1, repeats question for input
                    print(' Please enter in 0 for no or 1 for yes.')
                    vac_a[i] = int(input('  Does the individual have vac_a? '))

                vac_b[i] = int(input('  Does the individual have vac_b? '))
                if vac_b[i] != 0 and vac_a[i] != 1:
                    print(' Please enter in 0 for no or 1 for yes.')
                    vac_b[i] = int(input('  Does the individual have vac_a? '))

                vac_c[i] = int(input('  Does the individual have vac_c? '))
                if vac_c[i] != 0 and vac_a[i] != 1:
                    print(' Please enter in 0 for no or 1 for yes.')
                    vac_c[i] = int(input('  Does the individual have vac_a? '))

                break

            except ValueError:      #if not an integer, raise a ValueError
                print(' Please enter in 0 for no or 1 for yes.')

def report_data():
    #reports vaccine data for the individual that is input by the user
    while True:
        try:
            individual_num = int(input('    Enter the number of the individual(1-15): '))
            if 1 <= individual_num <= 15:
                i = individual_num - 1
                print(' Individual {0} vaccination data'.format(individual_num))

                if vac_a[i]:        #if vac_a[i] == 1(True)
                    print('     vac_a: Yes')
                else:
                    print('     vac_a: No')

                if vac_b[i]:
                    print('     vac_b: Yes')
                else:
                    print('     vac_b: No')

                if vac_c[i]:
                    print('     vac_c: Yes')
                else:
                    print('     vac_c: No')
            
            else:
                print(' Please enter in a number between 1-15')

            break

        except ValueError:
            print(' Please enter in a number between 1-15')

def report_total():
    #report vaccination totals for each vaccination type
    #initialize totals of each vaccine
    total_vac_a = sum(vac_a)
    total_vac_b = sum(vac_b)      
    total_vac_c = sum(vac_c)

    print(' Vaccine totals:')
    print('     vac_a: {0}'.format(total_vac_a))
    print('     vac_b: {0}'.format(total_vac_b))
    print('     vac_c: {0}'.format(total_vac_c))

#main part of program, where all the functions are called
while True:
    
    print_menu()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # just use first letter of input in case more than one is input
    print()

    if action == 'i':
        input_data()

    elif action == 'r':    
        report_data()

    elif action == 'v': 
        report_total()

    #quit the program
    elif action == 'q':
        break

    #invalid input
    else:
        print('* Not a valid option, select from one of the choices available *')

print('Done')
