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
infile2 = open('input.txt', 'r')        #second one for the second part to prevent issues
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

print('Number of characters: {0}'.format(num_chars))        #print number of characters

'''char = infile2.read()
print(char)'''


#WRITE to new file the first paragraph

#initialize variables
line = infile2.readline()
index = 0

for line in infile2:
    if (index <= 1):
        print(line, file = outfile)     #write to output
        index += 1      
    else: break     #only want the first line which is the first paragraph
        

infile.close()
infile2.close()
outfile.close()

