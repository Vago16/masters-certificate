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

#2.Print the zip code key and associated value(number of infections) 
# after updating with this_weeks_infections_dict keys if they exist
print('Updated infection data:')
print('Zip Code # Infections')
#if the key is in this_weeks_infections_dict, then add the value to the value associated with the same key in infection_by_zip
if '32003' in this_weeks_infections_dict:
     print(int('32003\t', '    ',(int(this_weeks_infections_dict['32003']) + int(infection_by_zip_dict['32003']))))
else:
     print('32003\t', '    ',infection_by_zip_dict['32003'])

if '32026' in this_weeks_infections_dict:
     print('32026\t', '    ',(int(this_weeks_infections_dict['32026']) + int(infection_by_zip_dict['32026'])))
else:
     print('32026\t', '    ',infection_by_zip_dict['32026'])

if '32192' in this_weeks_infections_dict:
     print('32192\t', '    ',(int(this_weeks_infections_dict['32192']) + int(infection_by_zip_dict['32192'])))
else:
     print('32192\t', '    ',infection_by_zip_dict['32192'])

if '34997' in this_weeks_infections_dict:
     print('34997\t', '    ',(int(this_weeks_infections_dict['34997']) + int(infection_by_zip_dict['34997'])))
else:
     print('34997\t', '    ',infection_by_zip_dict['34997'])
