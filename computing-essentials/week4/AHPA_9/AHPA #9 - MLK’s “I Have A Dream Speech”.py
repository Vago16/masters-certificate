# AHPA #9 - MLK’s “I Have A Dream Speech”
#
# Print the total number of
# characters in the speech.
#
# Open another file for output.
#
# Write only the first paragraph of
# this speech to that file.
#
# Student Name: Evagelos Petropoulos
#

infile = open('input.txt', 'r')
outfile = open('output.txt', 'w')

#READ and print num of characters in speech
#initiliazed variables
num_chars = 0
index = 1

#while there are characters
while True:
    char = infile.read(1)       #read by character
    num_chars += 1      #increment number of characters
    if not char:        #if at end of text, end loop
        break

print(num_chars)        #print number of characters
    



#WRITE to new file the first paragraph

#initialize variables
'''line = infile.readline()

while(line != ''):
    print(line, file = outfile)
    if (line > 1):
        break'''

#print('Hello', file = outfile)

infile.close()
outfile.close()

