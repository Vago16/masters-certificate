from abc import ABC, abstractmethod

class Person(ABC):
    #abstract base class to be inherited by Individual
    def __init__(self, id, name, last_name, address):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.address = address
    #decorater extending a method from ABC, to be used in Individual
    @abstractmethod
    def report(self):
        pass

class Individual(Person):
    # object to be used by the class Group
    def __init__(self, id, name, last_name, address):
        self.__id = id
        self.__vac_a = 0
        self.__vac_b = 0
        self.__vac_c = 0
        self.__sympt_a = 0
        self.__sympt_b = 0
        self.__sympt_c = 0
        self.__name = name
        self.__last_name = last_name
        self.__address = address

    #abstract base class method extended with the decorator
    def report(self):   
        print("Name: {0} {1}".format(self.name, self.last_name))

    # Getter and setter methods for attributes accessed outside or in Group

    def get_id(self):
        return self.__id

    def get_vac_a(self):
        return self.__vac_a

    def set_vac_a(self, val):
        self.__vac_a = val

    def get_vac_b(self):
        return self.__vac_b

    def set_vac_b(self, val):
        self.__vac_b = val

    def get_vac_c(self):
        return self.__vac_c

    def set_vac_c(self, val):
        self.__vac_c = val

    def get_sympt_a(self):
        return self.__sympt_a

    def set_sympt_a(self, val):
        self.__sympt_a = val

    def get_sympt_b(self):
        return self.__sympt_b

    def set_sympt_b(self, val):
        self.__sympt_b = val

    def get_sympt_c(self):
        return self.__sympt_c

    def set_sympt_c(self, val):
        self.__sympt_c = val

    def get_name(self):
        return self.__name

    def set_name(self, val):
        self.__name = val

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, val):
        self.__last_name = val

    def get_address(self):
        return self.__address

    def set_address(self, val):
        self.__address = val

    # Methods with adjusted attribute access
    def correct_input_vacc(self, vaccine_type):
        while True:
            try:
                prompt = '{0}? '.format(vaccine_type)
                value = int(input(prompt))
                if value in (0, 1):
                    return value
                else:
                    print(' Please enter 0 for no or 1 for yes.')
            except ValueError:
                print(' Please enter in 0 for no or 1 for yes.')

    def give_vaccine(self):
        print('Enter in the vaccination data for individual {0} (0 for no, 1 for yes): '.format(self.__id + 1))
        self.__vac_a = self.correct_input_vacc('vac_a')
        self.__vac_b = self.correct_input_vacc('vac_b')
        self.__vac_c = self.correct_input_vacc('vac_c')

    def correct_input_symptom(self, symptom_type):
        while True:
            try:
                prompt = '{0}? '.format(symptom_type)
                value = int(input(prompt))
                if value in (0, 1):
                    return value
                else:
                    print(' Please enter 0 for no or 1 for yes.')
            except ValueError:
                print(' Please enter in 0 for no or 1 for yes.')

    def check_symptom(self):
        print('Enter in the symptom data for individual {0} (0 for no, 1 for yes): '.format(self.__id + 1))
        self.__sympt_a = self.correct_input_symptom('sympt_a')
        self.__sympt_b = self.correct_input_symptom('sympt_b')
        self.__sympt_c = self.correct_input_symptom('sympt_c')

    def identifying_info(self):
        while True:
            person_name = input("   Enter First Name(20 character max): ")
            person_name = person_name.strip()
            if not person_name:
                print("Must input a name")
            elif len(person_name) > 20:
                print("Please enter 20 characters max")
            else:
                self.__name = person_name
                break

        while True:
            person_last_name = input("   Enter Last Name(20 character max): ")
            person_last_name = person_last_name.strip()
            if not person_last_name:
                print("Must input a name")
            elif len(person_last_name) > 20:
                print("Please enter 20 characters max")
            else:
                self.__last_name = person_last_name
                break

        while True:
            person_address = input("   Enter Address(40 character max): ")
            person_address = person_address.rstrip()
            if not person_address:
                print("Must input an address")
            elif len(person_address) > 40:
                print("Please enter 40 characters max")
            else:
                self.__address = person_address
                break

    def report_individual_vacc(self):
        lines = ['\nIndividual {0} vaccination data\n'.format(self.__id + 1),
                 ' First Name: {0}'.format(self.__name),
                 ' Last Name: {0}'.format(self.__last_name),
                 ' Address: {0}'.format(self.__address)]

        lines.append('     Johnson: Yes' if self.__vac_a else '     Johnson: No')
        lines.append('     Moderna: Yes' if self.__vac_b else '     Moderna: No')
        lines.append('     Pfizer: Yes' if self.__vac_c else '     Pfizer: No')

        return '\n'.join(lines)

    def report_individual_symptoms(self):
        print(' Individual {0} symptom data'.format(self.__id + 1))
        print('     Coughing: Yes' if self.__sympt_a else '     Coughing: No')
        print('     Fever: Yes' if self.__sympt_b else '     Fever: No')
        print('     Nausea: Yes' if self.__sympt_c else '     Nausea: No')

    def reset(self):
        self.__vac_a = 0
        self.__vac_b = 0
        self.__vac_c = 0
        self.__sympt_a = 0
        self.__sympt_b = 0
        self.__sympt_c = 0


class Group:
    def __init__(self, num_individuals=1):
        self.individuals = []
        for i in range(num_individuals):
            self.individuals.append(Individual(i, 'Name{0}'.format(i), 'Last_Name{0}'.format(i), 'Address{0}'.format(i)))

    def get_individual(self, index):
        #get the index of an individual object from the Group
        if 0 <= index < len(self.individuals):
            return self.individuals[index]
        else:
            return None
        
    def get_individuals(self):
        return self.individuals

    def add_individual(self, individual):
        self.individuals.append(individual)

    def print_menu(self):
        print()
        print('Press i to input data for each individual')
        print('Press r to report vaccination data for an individual')
        print('Press v to report vaccination totals for each vaccine type')
        print('Press s to report symptom totals for each vaccine type')
        print('Press t to reset to 0 vaccination and clear all symptom data for every patient')
        print('Press q to quit')
        print()

    def input_group_data(self):
        for individual in self.individuals:
            individual.give_vaccine()
            individual.check_symptom()
            individual.identifying_info()

    def report_from_group_vacc(self, individual_num):
        if 1 <= individual_num <= len(self.individuals):
            return self.individuals[individual_num - 1].report_individual_vacc()
        else:
            return 'Please enter a number of an individual that exists'

    def report_total_vacc(self):
        total_vac_a = 0
        total_vac_b = 0
        total_vac_c = 0

        for i in self.individuals:
            total_vac_a += i.get_vac_a()
            total_vac_b += i.get_vac_b()
            total_vac_c += i.get_vac_c()

        results = [' Vaccine totals:',
                   '     Johnson: {0}'.format(total_vac_a),
                   '     Moderna: {0}'.format(total_vac_b),
                   '     Pfizer: {0}'.format(total_vac_c)]
        return results

    def report_symptoms_per_vacc(self):
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
            if i.get_vac_a():
                if i.get_sympt_a():
                    total_vac_a_sympt_a += i.get_sympt_a()
                if i.get_sympt_b():
                    total_vac_a_sympt_b += i.get_sympt_b()
                if i.get_sympt_c():
                    total_vac_a_sympt_c += i.get_sympt_c()

            if i.get_vac_b():
                if i.get_sympt_a():
                    total_vac_b_sympt_a += i.get_sympt_a()
                if i.get_sympt_b():
                    total_vac_b_sympt_b += i.get_sympt_b()
                if i.get_sympt_c():
                    total_vac_b_sympt_c += i.get_sympt_c()

            if i.get_vac_c():
                if i.get_sympt_a():
                    total_vac_c_sympt_a += i.get_sympt_a()
                if i.get_sympt_b():
                    total_vac_c_sympt_b += i.get_sympt_b()
                if i.get_sympt_c():
                    total_vac_c_sympt_c += i.get_sympt_c()

        results = [' Symptom totals per vaccine:',
                   '     **Johnson**',
                   '         Coughing: {0}'.format(total_vac_a_sympt_a),
                   '         Fever: {0}'.format(total_vac_a_sympt_b),
                   '         Nausea: {0}'.format(total_vac_a_sympt_c),

                   '     **Moderna**',
                   '         Coughing: {0}'.format(total_vac_b_sympt_a),
                   '         Fever: {0}'.format(total_vac_b_sympt_b),
                   '         Nausea: {0}'.format(total_vac_b_sympt_c),

                   '     **Pfizer**',
                   '         Coughing: {0}'.format(total_vac_c_sympt_a),
                   '         Fever: {0}'.format(total_vac_c_sympt_b),
                   '         Nausea: {0}'.format(total_vac_c_sympt_c)]
        return results

    def reset(self):
        for i in self.individuals:
            i.reset()
        print(" All vaccinations and symptom data have been reset")

    def start(self):
        while True:
            self.print_menu()

            action = input('What do you want to do? ')
            action = action.lower()
            action = action[0]

            print()

            if action == 'i':
                self.input_group_data()

            elif action == 'r':
                # The original code called report_from_group_vacc() without argument
                # This needs an argument, or else you must handle it here
                try:
                    individual_num = int(input('Enter individual number to report: '))
                    print(self.report_from_group_vacc(individual_num))
                except ValueError:
                    print('Please enter a valid number')

            elif action == 'v':
                for line in self.report_total_vacc():
                    print(line)

            elif action == 's':
                for line in self.report_symptoms_per_vacc():
                    print(line)

            elif action == 't':
                self.reset()

            elif action == 'q':
                break

            else:
                print('* Not a valid option, select from one of the choices available *')
