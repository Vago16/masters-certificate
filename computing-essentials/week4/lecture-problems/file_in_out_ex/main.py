'''
Read the values from the input text file numbers.txt and write them to a new output file
formatted.txt.  Also calculate and print to the output file their total and average values.
'''

#open numbers.txt for reading
infile = open('numbers.txt', 'r')
#open formatted.txt for writing
outfile = open('formatted.txt', 'w')

#initialize variables
total = 0
numNumbers = 0      #how many numbers there are, used for calculating average
number = infile.readline()

while (number != ''):       #execute until end of file
    number = number.strip()     #gets rid of newline characters
    number = float(number)      #change number type from string to float
    print('{0:15.2f}'.format(number), file = outfile)       #print number values in formatted.txt
    total += number
    numNumbers += 1
    number = infile.readline()

print('-' * 15, file = outfile)
print('Total  : {0:6.2f}'.format(total), file = outfile)
print('Average  : {0:6.2f}'.format(total/numNumbers), file = outfile)


#closes both the read and write input and output respectively so that everything runs smooth
infile.close()
outfile.close()