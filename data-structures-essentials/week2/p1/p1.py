from timeit import default_timer as timer
import sys

# TO DO: define your arrange function here...
def arrange(string, evens = '', odds = ''):
    """A recursive function that rearranges a sequence of digits so the even numbers always come before the odd numbers.
        Arguments:
                string (str): a string with numbers in it to be arranged
                evens (str): empty string for even numbers to be placed into
                odds (str): empty string for odd numbers to be placed into
          """
    #base case for when string is empty, puts the even numbers before odds
    if not string:  
        return evens + odds
    
    #gets first character from the string
    char = string[0]

    if char.isdigit():
        #checks if the integer of the character is an even or odd number to add to the respective variable
        if (int(char) % 2 == 0):
            evens += char
        else:
            odds += char

    #recursive call to continue the function
    return arrange(string[1:], evens, odds)

#---- Main Program ----#        
# TO DO: start timer here...
start = timer()

# DONE: Parse the command line arguments 

if len(sys.argv) != 2:
    raise ValueError('Please provide one file name.')
inputFileName = sys.argv[1]

print("\nThe file that will be used for input is: " + inputFileName)

# TO DO: Open file, read lines into a list, close file...
f = open("digits.txt","r")
myList = f.readlines()
f.close()

print("\n************************")
print("*** Modified Strings ***")
print("************************")

# TO DO: For each item in the list, call arrange() and
#        print the modified list returned by arrange()...
for i in myList:
    print(arrange(i.strip()))


# TO DO: End timer...
end = timer()

# TO DO: print the running time...
print("\n************************")
print("*** Running Time ***")
print("************************")
print("Total Time of Program:", (end - start) * 1000, "milliseconds")

