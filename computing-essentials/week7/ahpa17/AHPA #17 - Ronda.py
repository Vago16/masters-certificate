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
data = []

for line in infile:
    row = line.strip().split(',')     #splits the lists by commas
    data.append(row) 

infile.close()
print(data)

#separate out times and make them uniform
times = []
pos = 0 
while pos < len(data):
    if (data[pos][3][1] == ':'):
        new_time = data[pos][3][0] + '.' + data[pos][3][2:]
        pos += 1
    else:
        new_time = data[pos][3]
        pos += 1
    times.append(new_time)

i = 0
for time in times:
    print(time + ' ' + str(i))
    i += 1
    
print(sorted(times))

#add times back in to data list
index = 0
for fight in data:
    fight.pop(3)
    fight.append(times[index])
    index +=1
