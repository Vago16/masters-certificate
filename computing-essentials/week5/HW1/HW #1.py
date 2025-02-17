#
# COP 5008 Homework #1 - Mpox Diagnostics
#
# Evagelos Petropoulos
#
# Open data file

# Ask Questions

# Display result of questionaire
infile = open("HW #1 Data.txt", "r")

data = infile.readline().strip()    #reads first patient's name

#list of the questions asked to tidy up the while loop for readability
questions = ['Have you been having headaches?', 'Have you been having severe headaches?', 'Have you had a fever?',
             'Do you have swollen lymph nodes?', 'Do you feel exhausted?', 'Do you have a backache?',
             'Are you experiencing chills?', 'Do you have a rash?', 'Do you have a rash in / on your genitals?',
             'Do you have muscle pains?']

while data != '':   #loops over the text file till the end of the text file
  print('Patient Name:', data)    #prints patient name

  #initiliaze score for questions to 0
  score = 0

  print(questions[0], end = ' ')   #end makes it so the printed 'Yes' or 'No' is on the same line
  if infile.readline().strip().lower() == 'yes':    #not case dependent
    print('Yes')
    score += 1
    print(questions[1], end = ' ')   #this question is dependent on the previous one
    if infile.readline().strip().lower() == 'yes':
      score += 2
      print('Yes')
    else: print('No')
  else: print('No')


  print(questions[2], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 3
    print('Yes')
  else: print('No')
  
  print(questions[3], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 3
    print('Yes')
  else: print('No')
  
  print(questions[4], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 2
    print('Yes')
  else: print('No')
  
  print(questions[5], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 2
    print('Yes')
  else: print('No')
  
  print(questions[6], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 3
    print('Yes')
  else: print('No')

  print(questions[7], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 3
    print('Yes')
    print(questions[8], end = ' ')    #this question is dependent on the previous one
    if infile.readline().strip().lower() == 'yes':
      score += 4
      print('Yes')
    else: print('No')
  else: print('No')

  print(questions[9], end = ' ')
  if infile.readline().strip().lower() == 'yes':
    score += 2
    print('Yes')
  else: print('No')
  
  print(score)
  if score >= 15:   #15 is the value that determines whether or not the patient likely has mpox
    print("You may have mpox, please see a doctor.")
  else:
    print('You probably do not have mpox.')

  print('\n')   # new line for readability
  infile.readline()   #reads blank line between patients and answers

  data = infile.readline().strip()    ##reads next patient's name

  
#closes text to make sure everything works properly
infile.close()