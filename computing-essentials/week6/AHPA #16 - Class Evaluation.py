# AHPA #16 - Class Evaluation

# Given the class data, perform the following actions:
# Determine the highest score on
# the final exam
#
# Using list functions, calculate
# the average score on the final
# exam
#
# Use a linear search to determine
# if any student got a score > 92
#
# Print out the test scores
# followed by commas – except the
# last one
#
# Determine how many students got a
# 77 on the final exam
#
# The students who got 77 dropped
# the class, print out the scores
# with the 77 scores removed
#
# Student Name: Evagelos Petropoulos
#
#Final Scores: 72,85,91,67,77,85,80,95,83,77​

fin_scores = [72, 85, 91, 67, 77, 85, 80, 95, 83, 77]

avg_score = sum(fin_scores) / len(fin_scores)       #divides sum of list by length to get average
print('The average score is', avg_score)

#linear search for students who got above a 92
limit = 92
pos = 0
found = False

while pos < len(fin_scores) and not found:      #while position is less than the length of the list and found is false
    if fin_scores[pos] > limit:
        found = True        #if greater than limit, found is now truw
    else: pos = pos + 1
    if found:       #if found is true, print this statement
        print('Student', pos, 'got above a 92.')

#print out all test scores, followed by commas, except the last one
for i in range(len(fin_scores)):
    if (i == len(fin_scores) - 1):      #if last element, just print elements
        print(fin_scores[i])
    else:
        print('{0},'.format(fin_scores[i]), end = '')       #for all elements except last, print element separators

#this loop counts how many times 77 appears in the list
counter = 0
val = 77
for ele in fin_scores:
    if (ele == val):
        counter = counter + 1

print('The score 77 appears {0} times.'.format(counter))

#this loop removes all instances of the element 77 from the list
index = 0

while index < len(fin_scores):
    score = fin_scores[index]       #value at a certain position
    if (score == val):      # val is  77
        fin_scores.pop(index)       #remove if it equals val
    else: index = index + 1     #increment otherwise

print('This is the list of scores with all instances of 77 removed:,', fin_scores)
    
