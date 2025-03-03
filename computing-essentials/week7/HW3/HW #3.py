#
# COP 5008 - Homework #3: Finding The Source
#
# Evagelos Petropoulos
#
#initialize empty dictionaries
infection_by_zip_dict = {}
this_weeks_infections_dict = {}

#try-except statement for opening infile_infection_by_zip and mapping keys and values to a dictionary 
try:        
    infile_infection_by_zip = open('InfectionByZip.txt', 'r')
    #strips periods, commas, and newline characters while reading lines and splits elements when a space is detected
    for line in infile_infection_by_zip:
        line = line.strip()
        if line:        #if line is true
            key, value = line.split()       #splits key and values apart when space is detected
            infection_by_zip_dict[key] = value
    infile_infection_by_zip.close()     #closes files
except FileNotFoundError:
    print("Error: File \'InfectionByZip.txt\' not found.")
except ValueError:
         print(f"Error: Invalid format found in file.")

#try-except statement for opening infile_this_weeks_infections and mapping keys and values to a dictionary 
try:        
    infile_this_weeks_infections = open('ThisWeeksInfections.txt', 'r')
    for line in infile_this_weeks_infections:
        line = line.strip()
        if line:       
            key, value = line.split()      
            this_weeks_infections_dict[key] = value
    infile_this_weeks_infections.close()     
except FileNotFoundError:
    print("Error: File \'ThisWeeksInfections.txt\' not found.")
except ValueError:
         print(f"Error: Invalid format found in file.")

         
#1.Print the zip code key and associated value(number of infections)
print('Zip Code # Infections')
print('32003\t', '    ',infection_by_zip_dict['32003'])
print('32026\t', '    ',infection_by_zip_dict['32026'])
print('32192\t', '    ',infection_by_zip_dict['32192'])
print('34997\t', '    ',infection_by_zip_dict['34997'])

print(this_weeks_infections_dict)
print()     #blank line for readability