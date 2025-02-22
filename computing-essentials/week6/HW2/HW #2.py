#
# COP 5008 – Homework #2: Almost A Problem
#
# Evagelos Petropoulos
#
infile = open("HW #2 - Data.txt", "r")
data = []


for line in infile:
    row = line.strip().split()       #splits the lists by commas
    data.append(row)    #appends each line as a new list
print(data)


males_with_mpox = 0
females_with_mpox = 0
total_mpox = 0      #sum of men and women who have mpox
total_females = 0
total_males = 0
total = len(data)   #total number of people
#loop for getting numbers of males and females
for i in data:
    if 'F' in i:
        total_females += 1
    if 'M' in i:
        total_males += 1

#to calculate percentage of men and women who mpox, must first get the numbers of who has it by gender
for i in data:
    mpox = i[13]        #mpox confirmation is the last element, 0 being false and 1 being true
    if mpox == '1':
        if 'F' in i:
            females_with_mpox += 1
        if 'M' in i:
            males_with_mpox += 1 

#gets percentage by dividing those with mpox by the total number of the gender, and multiplies by 100
def calc_mpox_by_gender():
    female_percent = (females_with_mpox / total_females) * 100      
    male_percent = (males_with_mpox / total_males) * 100
    return('\tOf the people who have Mpox, {0:.2f}{2} of them are males.\n\tOf the people who have Mpox, {1:.2f}{2} of them are females'.format(male_percent, female_percent, '%'))

print('1. What is the percentage of men vs. women who have mpox?')
print(calc_mpox_by_gender())
print()     #blank line for readability

#gets the value for how many people are above 65
seniors = 0
for i in data:
    senior_females_with_mpox = 0        #initialize vars
    senior_males_with_mpox = 0
    mpox = i[13]        #mpox confirmation is the last element, 0 being false and 1 being true
    if (int(i[1]) > 65):
        seniors += 1
        if mpox == '1':
            if 'F' in i:
                senior_females_with_mpox += 1
            if 'M' in i:
                senior_males_with_mpox += 1
print('2. Question #2:')
print('\ta. How many people over age 65 have mpox?')
print('\t\t There are {0} people over 65 that have mpox.'.format(seniors))
print('\tb. How many men over 65 have mpox?')
print('\t\t There are {0} men over 65 that have mpox.'.format(senior_males_with_mpox))
print('\tc. How many women over 65 have mpox?')
print('\t\t There are {0} women over 65 that have mpox.'.format(senior_females_with_mpox))
print()






       


                  


'''if 'F' in i:
        females_with_mpox += 1
        print(females_with_mpox, 'females',)
    if 'M' in i:
        males_with_mpox += 1 
        print(males_with_mpox, 'males')           #gender is the first element in each list
       #mpox confirmation is the last element, 0 being false and 1 being true'''


'''if mpox == 1:
        total_mpox += 1
        if gender == 'M':
            males_with_mpox += 1
        if gender == 'F':
            females_with_mpox += 1'''



#closes text to make sure everything works properly
infile.close()