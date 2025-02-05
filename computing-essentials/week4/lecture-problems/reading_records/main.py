'''
Open and read def leppard.txt, identify each album based on what order it was released in, 
print the order it was released and the title of the album.
'''

infile = open('def leppard.txt')

index = 1
order = 1

for line in infile:
    if (index == 1):        #if at title of album, so only print title
        print('{0}:  {1}'.format(order, line.rstrip()))        #print title and remove newline character
        order += 1      # increment order for every line printed
    index += 1      #increment index for every line read
    if (index == 6):        #every 6 lines is a new album, so take index back to initial value
        index = 1