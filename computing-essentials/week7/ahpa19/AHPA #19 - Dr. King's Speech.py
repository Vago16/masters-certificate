# AHPA #19 - Dr. King's Speech
#
# Using sets I want you to calculate how 
# many unique words there are in Dr. 
# King’s “I Have A Dream” speech.
#
# Using sets I want you to calculate how 
# many unique words there are in Dr. 
# King’s “Letter From the Birmingham 
# City Jail” text.
#
# Next, I’d like to know how many of 
# the words in the “I have a dream 
# speech” were also used in the “Letter 
# From the Birmingham City Jail” text 
# (count).
#
# Now tell me what words that were used 
# in the “I have a dream” speech were 
# NOT used in the “Letter From the 
# Birmingham City Jail” text (list).
#
#Student Name: Evagelos Petropoulos
#
infile_dream_speech = open('AHPA #19 - MLK Speech.txt', 'r')
infile_jail_speech = open('AHPA #19 - Letter From The  Birmingham City Jail Speech.txt', 'r')

dream_speech_list = []  #empty lists 
jail_speech_list = []

#strips periods, commas, and newline characters while reading lines and splits elements when a space is detected
for line in infile_dream_speech:
    words = line.lower().replace('.', '').replace(',', '').replace('!', '').replace(':', '').split()
    dream_speech_list.extend(words)

for row in infile_jail_speech:
    words = row.lower().replace('.', '').replace(',', '').replace('!', '').replace(':', '').split()
    jail_speech_list.extend(words)

#converts lists to sets
dream_speech_set = set(dream_speech_list)
jail_speech_set = set(jail_speech_list)

#closes files
infile_dream_speech.close()
infile_jail_speech.close()

#1. Prints out how many unique words there are in Dr. King’s “I Have A Dream” speech
print('There are {0} unique words in Dr. King’s “I Have A Dream” speech.\n'.format(len(dream_speech_set)))

#2. Prints out how many unique words there are in Dr. King’s “Letter From the Birmingham City Jail” text.
print('There are {0} unique words in Dr. King’s “Letter From the Birmingham City Jail” text.\n'.format(len(jail_speech_set)))

#3. Prints out how many words in the “I have a dream speech” were also used in the “Letter From the Birmingham City Jail” text(count)
print('There are {} words in \"I have a dream\" speech that were also used in the \"Letter From the Birmingham County Jail\" text.\n'.format(len(dream_speech_set.intersection(jail_speech_set)))) 

#4. Prints out what words were used in “I have a dream speech” but were not used in the “Letter From the Birmingham City Jail” text(list)
difference_list = list(dream_speech_set.difference(jail_speech_set))        #gets the difference
print('These words only appeared in the \"I Have A Dream\" speech:\n', difference_list)