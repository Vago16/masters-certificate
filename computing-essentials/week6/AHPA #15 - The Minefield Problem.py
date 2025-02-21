#
# AHPA #15 - The Minefield Problem
#


# Initialize variables
rows = 20
columns = 20
mineField = []
numHumans = 0


# Create the minefield

row = ". . . . . . . . . . . . + . . . . . . ."
mineField.append(row.split(" "))
row = ". . . . . . . . . . . . + . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + H + + . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . . + . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . . . H + + + . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . . . . . . + . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . . . . . . + . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . . + + H + + . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . + . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . H . . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . + . . . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . + . . . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . + . . . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . + . . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . + . . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + . . . . . . . . . ."
mineField.append(row.split())
row = ". . . . . . . . . + . . . . . . . . . ."
mineField.append(row.split())


#
# Function Name: printMap
#
# Description: Prints out the map of the mine field showing where you 
#              have already been.
#
# Inputs: None
#
# Outputs: None
#

def printMap():
  for i in mineField:
    print(i)
  print("")
  print("")
                               
#
# Count the number of humans in the mindfield -- can we pick all of them
# up?
#
for row in mineField:
    numHumans = numHumans + row.count('H')      #count num of times "H" occurs in the list


print("There are {0} humans to be picked up.".format(numHumans))

#
# Start off making your way through the minefield, pick up humans as you
# find them
#
for row in mineField:
    if 'H' in row:      #check if 'H' is in the list
      n = row.index('H')        #get the index at which H occurs
      row[n] = '*'      #show the location has been traversed safely
      printMap()        #print map as per instructions
      while '+' in row:     # to make sure if theres multiple instances of '+' in the list
        m = row.index('+')
        row[m] = '*'
    elif '+' in row:        #check if '+' is in the list
       m = row.index('+')
       row[m] = '*'
       if 'H' in row:       
        n = row.index('H')
        row[n] = '*'
        printMap()
        while '+' in row:
         m = row.index('+')
         row[m] = '*'

printMap()      #final print of map to show output is as expected

   
#
# Find entry point into minefield
#

#
# Mark entry into the minefield
#

#
# Work your way through the minefield
#