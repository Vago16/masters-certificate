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
seniors = 0     #initialize vars
senior_females_with_mpox = 0        #initialize vars
senior_males_with_mpox = 0
for i in data:
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

#function to count people under 18 with mpox
def count_juniors():
    juniors = 0
    for i in data:
        mpox = i[13]        #mpox confirmation is the last element, 0 being false and 1 being true
        if (int(i[1]) < 18):
            if mpox == '1':
                juniors += 1
    return(juniors)

print('3. How many people under the age of 18 have mpox?')
print('\tThere are {0} people under the age of 18 that have mpox.'.format(count_juniors()))
print()

#function to count overweight males with mpox
def count_overweight_males():
    overweight_males_with_mpox = 0      #initialize var
    for i in data:
        mpox = i[13]
        if 'M' in i:
            if (int(i[2]) >= 210):
                if mpox == '1':
                    overweight_males_with_mpox += 1
    return(overweight_males_with_mpox)

print('4. If the average weight of a man is 190 pounds, how many men who are overweight by at least 20 pounds have mpox?')
print('\tThere are {0} men that are overweight that have mpox.'.format(count_overweight_males()))
print()

#function to count overweight females with mpox
def count_overweight_females():
    overweight_females_with_mpox = 0
    for i in data:
        mpox = i[13]
        if 'F' in i:
            if (int(i[2]) >=  180):
                if mpox == '1':
                    overweight_females_with_mpox += 1
    return(overweight_females_with_mpox)

print('5. If the average weight of a woman is 160 pounds, how many women who are overweight by at least 20 pounds have mpox?')
print('\tThere are {0} women that are overweight that have mpox.'.format(count_overweight_females()))

       


#closes text to make sure everything works properly
infile.close()