# AHPA #12 - The Party

# You need to create a Python
# program to keep track of who's
# coming, what they are bringing,
# and how many people you will be
# able to serve.
#
# Create a program that uses a list
# to keep track of all of the
# required information.
#
# Here's the data that you will
# load into your list: Frank,
# pizza, 10, Mary, wings, 8, Bob,
# cookies, 15, Lisa, dip, 20, Mark,
# brownies, 12, Ann, burgers, 7,
# Henry, mints, 30, Ruth, hotdogs,
# 22
#
# After entering the data, answer
# the following questions:
#
# How many people will be bringing
# food?
# What foods will be there?
# How many people can be fed if
# Ruth cancels?
#
# Student Name: Evagelos Petropoulos
#
# Create party list

# How many people will be bringing food?

#What food will be there?

#How many people can be fed if Ruth cancels?

party_list = [['Frank', 'pizza', 10 ], ['Mary', 'wings', 8], ['Bob', 'cookies', 15], ['Lisa', 'dip', 20],
               ['Mark', 'brownies', 12], ['Ann', 'burgers', 7], ['Henry', 'mints', 30], ['Ruth', 'hotdogs', 22]]   
frank_list = party_list[0]
mary_list = party_list[1]
bob_list = party_list[2]
lisa_list = party_list[3]
mark_list = party_list[4]
ann_list = party_list[5]
henry_list = party_list[6]
ruth_list = party_list[7]

people_bringing_food = len(party_list)
print('There are {0} people bringing food.'.format(people_bringing_food))     #Number of people bringing food

print('The food being brought includes: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}.'.format(
    frank_list[1], mary_list[1], bob_list[1], lisa_list[1], mark_list[1], ann_list[1], henry_list[1], ruth_list[1]
))      #food being brought to the party

#variable for how many people are fed, adds values of third indexes together except for ruth
amount_fed = frank_list[2] + mary_list[2] + bob_list[2] + lisa_list[2] + mark_list[2] + ann_list[2] + henry_list[2]
print('{0} people can be fed if Ruth cancels.'.format(amount_fed))      #amount of people that can be fed



