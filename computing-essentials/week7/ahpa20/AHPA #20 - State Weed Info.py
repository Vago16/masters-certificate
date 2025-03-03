# AHPA #20 - State Weed Info
#
# Open the state data file and create 3
# separate dictionaries: one for 
# population, one for 
# representatives, and one for  % of 
# U.S. population.
#
# Answer the following questions:
# What % of the U.S. lives in the 
#original 13 colonies?
# [New Hampshire, Massachusetts, 
# Connecticut, Rhode Island, New York, 
# New Jersey, Pennsylvania, Delaware, 
# Maryland, Virginia, North Carolina, 
# South Carolina, Georgia]
#
# If California fell into the ocean, 
# what % of our population would we 
# lose?
# 
# If President Biden needs to get a 
# bill passed and only California, 
# Texas, Florida, and New York support 
# it, will it pass in the House? 
# [There are 435 representatives]
#
# What percentage of representatives 
# come from Florida?
# 
# Four states have legalized marijuana 
# for recreational use (Washington , 
# Oregon , Colorado, and Alaska). How 
# many people can legally use weed?
#
#Evagelos Petropoulos
#
infile = open('AHPA #20 - State Data.txt', 'r')
lines = []
for line in infile:
    lines.append(line.strip())

#initialize dicionary
dict_states = {}
states = [' '.join(item.split()[:-2]) for item in lines]        #list comprehension to get list of states

#initialize index for the for loop
index = 0
for state in states:
    dict_states[state] = [int(item) for item in lines[index].split()[-2:]]      #list comprehension to get dictionary of key: states and value: populations and reps
    index += 1


#Question: What % of the U.S. lives in the original 13 colonies?
#original 13 states list
states = ['New Hampshire', 'Massachusetts', 'Connecticut', 'Rhode Island', 'New York', 'New Jersey', 'Pennsylvania', \
'Delaware', 'Maryland', 'Virginia', 'North Carolina', 'South Carolina', 'Georgia']

pop_13_states = 0   
#gets the population of the 13 colonies
for key in states:
    pop_13_states += dict_states[key][0]       #if iterable in states matches a key in the dictionary 

total_pop = 0   
#gets total population
for key in dict_states.keys():
    total_pop += dict_states[key][0]

pop_13_states = (pop_13_states*100)/total_pop
#prints out the percentage asked for
print('{0:.2f}{1} of the U.S. lives in the original 13 colonies.'.format(pop_13_states,'%'))

#Question: If California fell into the ocean, what % of our population would we lose?
#population of california
cal_pop = dict_states['California'][0]
pop_lost = (cal_pop*100)/total_pop
print('If California fell into the ocean, we would lose {0:.2f}{1} of our population.'.format(pop_lost,'%'))

#Question: If President Biden needs to get a bill passed and only California, Texas, Florida, and New York support it, will it pass in the House?
total_reps = 0
#gets total number of reps
for key in dict_states.keys():
    total_reps += dict_states[key][1]

state_rep = 0
#list of states that support the bill
states_bill = ['California', 'Texas', 'Florida', 'New York']
for key in states_bill:
    state_rep += dict_states[key][1]        #gets the reps from the states in the list, index position 1 is the second val in the dictionary

print('There are {0} reps in the states that support Biden and {1} in the House, so no, it will not pass.'.format(state_rep, total_reps))

# What percentage of representatives come from Florida?
reps_from_fl_percent = (dict_states['Florida'][1]*100)/435      #435 is total number of reps
print('{0:.2f}{1} of representatives come from Florida.'.format(reps_from_fl_percent, '%'))

# Four states have legalized marijuana for recreational use (Washington , Oregon , Colorado, and Alaska).
#Question: How many people can legally use weed?
states_that_can_smoke = ['Washington','Oregon', 'Colorado','Alaska']
pop_states_that_can_smoke = 0
for key in states_that_can_smoke:
    pop_states_that_can_smoke += dict_states[key][0]        #index 0 is population
print('{0:,} people can legally use weed.'.format(pop_states_that_can_smoke))