# AHPA #17 - Ronda
#
# The coach has the results of all 
# of her past fights (opponent, 
# method, round, total time).
#
# Now he wants to know the top 
# three fastest matches that Ronda 
# has won and how she won them.
#
# You need to create a Python 
# program to read in her data, 
# clean it, and find these answers.
#
# Student Name: Evagelos Petropoulos
#

infile = open('AHPA #17 - Rousey Data.txt', 'r')
#initialize empty list
data = []

#function to convert total time to seconds
def convert_to_seconds(time_str):
    minutes, seconds = time_str.split(":")
    return int(minutes) * 60 + float(seconds)


for line in infile:
    line = line.strip()     
    if line:        #if line is not empty
        opponent, method, num_of_rounds, time = line.split(',')     #splits values based on commas
        time_in_seconds = convert_to_seconds(time)
        data.append((opponent, method, num_of_rounds, time_in_seconds))

sorted_fights = sorted(data)
top_three_fights = sorted_fights[0:2]

for fight in sorted_fights:
    print('Ronda fought {0} with {1} in {2} seconds.'.format(opponent, method, time_in_seconds))

infile.close()
print(data)

