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

infile = open('AHPA #9 - MLK Speech.txt', 'r')

num_chars = 0

while True:
    char = infile.read(1)
    num_chars += 1
    if not char:
        break

print(num_chars)
    

infile.close()