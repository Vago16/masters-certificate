# Module 2  Assignment
# Classes file
# Evagelos Petropoulos
# U75564437

class Individual:
    #object to be used by the class Group
    def __init__(self, id, name, last_name, address):
        #initialize Individual object with id, vaccination status(set to false(0) initially for all 3 vaccines)
        #symptom status(set to false(0) initially for all 3 symptoms), name, last_name, and address
        self.id = id
        self.vac_a = 0
        self.vac_b = 0
        self.vac_c = 0
        self.sympt_a = 0
        self.sympt_b = 0
        self.sympt_c = 0
        self.name = name
        self.last_name = last_name
        self.address = address


    def correct_input_vacc(self,vaccine_type):
        #makes sure the value input is valid for the method give_vaccine()
        while True:     #keep looping until there is a valid integer input
            try:
                prompt =('{0}? ').format(vaccine_type)
                value = int(input(prompt))
                if value in (0, 1):  # valid input
                    return value
                else:
                    print(' Please enter 0 for no or 1 for yes.')

            except ValueError:      #if not an integer, raise a ValueError
                print(' Please enter in 0 for no or 1 for yes.')
        
    def give_vaccine(self):
        #inputs data for each vaccine(0 is a no for the particular vaccine and 1 is a yes)
        print('Enter in the vaccination data for individual {0} (0 for no, 1 for yes): '.format(self.id + 1))
        self.vac_a = self.correct_input_vacc('vac_a')
        self.vac_b = self.correct_input_vacc('vac_b')
        self.vac_c = self.correct_input_vacc('vac_c')

    def correct_input_symptom(self, symptom_type):
        #makes sure the value input is valid for the method check_symptom()
        while True:     #keep looping until there is a valid integer input
            try:
                prompt =('{0}? ').format(symptom_type)
                value = int(input(prompt))
                if value in (0, 1):  # valid input
                    return value
                else:
                    print(' Please enter 0 for no or 1 for yes.')

            except ValueError:      #if not an integer, raise a ValueError
                print(' Please enter in 0 for no or 1 for yes.')

    def check_symptom(self):
        #inputs data for each symptom(0 is a no for the particular symptom and 1 is a yes)
        print('Enter in the symptom data for individual {0} (0 for no, 1 for yes): '.format(self.id + 1))
        self.sympt_a = self.correct_input_symptom('sympt_a')
        self.sympt_b = self.correct_input_symptom('sympt_b')
        self.sympt_c = self.correct_input_symptom('sympt_c')

    def report_individual_vacc(self):
        #returns what vaccines an individual does and does not have
        print(' Individual {0} vaccination data'.format(self.id + 1))

        if self.vac_a:        #if self.vac_a == 1(True)
            print('     vac_a: Yes')
        else:
            print('     vac_a: No')

        if self.vac_b:
            print('     vac_b: Yes')
        else:
            print('     vac_b: No')

        if self.vac_c:
            print('     vac_c: Yes')
        else:
            print('     vac_c: No')

    def report_individual_symptoms(self):
        #returns what symptoms an individual does and does not have
        print(' Individual {0} symptom data'.format(self.id + 1))

        if self.sympt_a:        #if self.sympt_a == 1(True)
            print('     sympt_a: Yes')
        else:
            print('     sympt_a: No')

        if self.sympt_b:        
            print('     sympt_b: Yes')
        else:
            print('     sympt_b: No')

        if self.sympt_c:        
            print('     sympt_c: Yes')
        else:
            print('     sympt_c: No')

class Group:
    #class that has 15 Individual objects and uses them to track vaccine status
    def __init__(self, num_individuals = 5):    
        ######CHANGE BACK TO 15#####
        self.individuals = []       #initialize list for Individual objects, with placeholders for name, last_name, and address
        for i in range(num_individuals):
            self.individuals.append(Individual(i, 'Name{0}'.format(i), 'Last_Name{0}'.format(i), 'Address{0}'.format(i)))

    def print_menu(self):
        #displays the program's menu of options for the group
        print()
        print('Press i to input data for each individual')
        print('Press r to report vaccination data for an individual')
        print('Press v to report vaccination totals for each vaccine type')
        print('Press s to report symptom totals for each vaccine type')
        print('Press t to reset to 0 vaccination and clear all symptom data for every patient')
        print('Press q to quit')
        print()

    def input_group_data(self):
        #inputs vaccine data for every Individual object in Group
        for individual in self.individuals:
            individual.give_vaccine()
            individual.check_symptom()

    def report_from_group_vacc(self):
        #returns vaccine data for a selected Individual object
        while True:
            try:
                individual_num = int(input('    Enter the number of the individual(1-15): '))
                if 1 <= individual_num <= len(self.individuals):
                    self.individuals[individual_num - 1].report_individual_vacc()
                    break
                else:
                    print(' Please enter in a number between 1-15')

            except ValueError:
                print(' Please enter in a number between 1-15')
    
    def report_total_vacc(self):
        #report vaccination totals for each vaccination type
        #initialize totals of each vaccine
        total_vac_a = 0
        total_vac_b = 0
        total_vac_c = 0

        for i in self.individuals:
            total_vac_a += i.vac_a
            total_vac_b += i.vac_b      
            total_vac_c += i.vac_c

        print(' Vaccine totals:')
        print('     vac_a: {0}'.format(total_vac_a))
        print('     vac_b: {0}'.format(total_vac_b))
        print('     vac_c: {0}'.format(total_vac_c))

    def report_symptoms_per_vacc(self):
        #report symptom data for each vaccination type
        #initialize symptom data for each vaccine
        total_vac_a_sympt_a = 0
        total_vac_a_sympt_b = 0
        total_vac_a_sympt_c = 0

        total_vac_b_sympt_a = 0
        total_vac_b_sympt_b = 0
        total_vac_b_sympt_c = 0

        total_vac_c_sympt_a = 0
        total_vac_c_sympt_b = 0
        total_vac_c_sympt_c = 0

        for i in self.individuals:
            if i.vac_a:     #if individual has vac_a
                if i.sympt_a:
                    total_vac_a_sympt_a += i.sympt_a
                if i.sympt_b:
                    total_vac_a_sympt_b += i.sympt_b
                if i.sympt_c:
                    total_vac_a_sympt_c += i.sympt_c

            if i.vac_b:     
                if i.sympt_a:
                    total_vac_b_sympt_a += i.sympt_a
                if i.sympt_b:
                    total_vac_b_sympt_b += i.sympt_b
                if i.sympt_c:
                    total_vac_b_sympt_c += i.sympt_c

            if i.vac_c:     
                if i.sympt_a:
                    total_vac_c_sympt_a += i.sympt_a
                if i.sympt_b:
                    total_vac_c_sympt_b += i.sympt_b
                if i.sympt_c:
                    total_vac_c_sympt_c += i.sympt_c

        print(' Symptom totals per vaccine:')
        print('     **vac_a**')
        print('         sympt_a: {0}'.format(total_vac_a_sympt_a))
        print('         sympt_b: {0}'.format(total_vac_a_sympt_b))
        print('         sympt_c: {0}'.format(total_vac_a_sympt_c))

        print('     **vac_b**')
        print('         sympt_a: {0}'.format(total_vac_b_sympt_a))
        print('         sympt_b: {0}'.format(total_vac_b_sympt_b))
        print('         sympt_c: {0}'.format(total_vac_b_sympt_c))

        print('     **vac_a**')
        print('         sympt_a: {0}'.format(total_vac_c_sympt_a))
        print('         sympt_b: {0}'.format(total_vac_c_sympt_b))
        print('         sympt_c: {0}'.format(total_vac_c_sympt_c))
                        

    def reset(self):
        pass

    def start(self):
        #start program menu with actions to be performed
        while True:
    
            self.print_menu()

            action = input('What do you want to do? ')
            action = action.lower()
            action = action[0]  # just use first letter of input in case more than one is input
            print()

            if action == 'i':
                self.input_group_data()

            elif action == 'r':    
                self.report_from_group_vacc()

            elif action == 'v': 
                self.report_total_vacc()

            elif action == 's': 
                self.report_symptoms_per_vacc()

            elif action == 't': 
                self.reset()

            #quit the program
            elif action == 'q':
                break

            #invalid input
            else:
                print('* Not a valid option, select from one of the choices available *')