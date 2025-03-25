from timeit import default_timer as timer
import sys

# TO DO: define your arrange function here...




#---- Main Program ----#        
# TO DO: start timer here...



# DONE: Parse the command line arguments 


if len(sys.argv) != 2:
    raise ValueError('Please provide one file name.')
inputFileName = sys.argv[1]

print("\nThe file that will be used for input is: " + inputFileName)


# TO DO: Open file, read lines into a list, close file...



print("\n************************")
print("*** Modified Strings ***")
print("************************")

# TO DO: For each item in the list, call arrange() and
#        print the modified list returned by arrange()...




# TO DO: End timer...




# TO DO: print the running time...



