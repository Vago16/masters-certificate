# Module 1 Topic 3 Assignment
# Modeling Physical Objects with OOP Assignment
# Evagelos Petropoulos
# U75564437

class Individual:
    def _init_(self, id):
        #nitialize Individual object with id, name, vaccination status(set to false initially for all 3 vaccines)
        self.id = id
        self.vac_a = 0
        self.vac_b = 0
        self.vac_c = 0

    def correct_input(self,vaccine_type):
        #makes sure the value input is valid
        while True:     #keep looping until there is a valid integer input
            try:
                value = int(input('{0}? ').format(vaccine_type))
                if value != 0 and value != 1:     #in case the user inputs an integer that is not 0 or 1, repeats question for input
                    print(' Please enter in 0 for no or 1 for yes.')
                    value = int(input('  Does the individual have vac_a? '))
                break

            except ValueError:      #if not an integer, raise a ValueError
                print(' Please enter in 0 for no or 1 for yes.')
        
    def give_vaccine(self):
        #inputs data for each vaccine(0 is a no for the particular vaccine and 1 is a yes)
        print('Enter in the vaccination data for individual {0} (0 for no, 1 for yes): '.format(self.id + 1))
        