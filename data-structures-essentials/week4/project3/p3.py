from timeit import default_timer as timer
import sys

#
# Music Streaming Application
#

# This class is used to store one node in the linked list.
# A node has a song's title and three pointers to other nodes.
class Song:
    def __init__(self, title):
        self.title = title
        self.nextInOrigOrder = None # pointer to next song on list when initial list is created
        self.prevInPlaylist  = None # pointer to previous song in the user's playlist
        self.nextInPlaylist  = None # pointer to next song in the user's playlist

    # methods used to set the pointers
    def setNextInOrigOrder (self, node):
        self.nextInOrigOrder = node

    def setPrevInPlaylist (self, node):
        self.prevInPlaylist = node

    def setNextInPlaylist (self, node):
        self.nextInPlaylist = node

    # returns the song title of the node    
    def getSongTitle(self):
        return(self.title)

    # returns the next node (in the original order)
    def getNextInOrigOrder(self):
        return(self.nextInOrigOrder)

    # returns the previous node (in the playlist order)
    def getPrevInPlaylist(self):
        return(self.prevInPlaylist)

    # returns the next node (in the playlist order)
    def getNextInPlaylist(self):
       return(self.nextInPlaylist)



# Main Program
# Initializing pointers that will be used to create and traverse the linked list
headNodeOrig = None
headNodePlaylist = None
tailNodePlaylist = None
currentNode = None

# TO DO: write your code below this line.
#start timer
start = timer()

#takes the name of the python file and text input files as command line arguments, must be in order of 
#p3.py songs.txt playlist.txt commands.txt in the command line
if len(sys.argv) != 4:
    raise ValueError('Please provide three file names.')

inputSongs = sys.argv[1]
inputPlaylist = sys.argv[2]
inputCommands = sys.argv[3]

print("\nThe file that has all the songs is:", inputSongs)
print("\nThe file that has the user's playlist is:", inputPlaylist)
print("\nThe file that has the user's commands is:", inputCommands)
print()

#####SONG INPUT########
#open text file for songs
f = open(inputSongs,"r")

songTitle = f.readline().rstrip()

while songTitle != '':
    new_node = Song(songTitle)       #creates new node

    #print(songTitle)   #makes sure songs are being correctly read and mapped to list, uncomment to check
    
    if headNodeOrig is None:
        headNodeOrig = new_node     #head node is now created for songs
    else:
        currentNode.setNextInOrigOrder(new_node)
    
    currentNode = new_node  #traverse to the next node
    songTitle = f.readline().rstrip()

f.close()

#######PLAYLIST INPUT##########
#open text file for playlist
g = open(inputPlaylist, "r")

playlist_title = g.readline().rstrip()

while playlist_title != '':
    search_node = headNodeOrig  #starts the search at the head
    found_node = None   #initializes variable for the value that is to be searched for

    while search_node is not None:
        if search_node.getSongTitle() == playlist_title:
            found_node = search_node
            break
        search_node = search_node.getNextInOrigOrder()

    #print(search_node.getSongTitle())   #make sure correct order is happening, uncomment to check

    if found_node is not None:
        if headNodePlaylist is None:
            headNodePlaylist = found_node   #rearranges so head node now has playlist song
        else:
            #update head pointers
            currentNode.setNextInPlaylist(found_node)
            found_node.setPrevInPlaylist(currentNode)

        currentNode = found_node    #location now at the current node
        tailNodePlaylist = found_node   #update tail pointers


    playlist_title = g.readline().rstrip()

g.close()

########COMMAND INPUT########
#open text file for commands
h = open(inputCommands, "r")

input_commands = h.readline().rstrip()

print("***********************")
print("** Playlist Commands **")
print("***********************")

#list of variables that encompass input commands 
while input_commands != '':
    
    if input_commands == "Beginning":
        currentNode = headNodePlaylist     #set position to head of playlist
        print("Beginning")

    elif input_commands == "End":
        currentNode = tailNodePlaylist        #set position to tail of the playlist
        print("End")

    elif input_commands == "Play":
        if currentNode:
            print("Now Playing: ", currentNode.getSongTitle())       #displays current Song title node
        else:
            print("Please select a song.")

    elif input_commands == "Previous":
        print("Previous")
        if currentNode and currentNode.getPrevInPlaylist():    #if at current node and there is not None value returned for the previous node
            currentNode = currentNode.getPrevInPlaylist()     #moves currentNode to previous Song node in playlist

    elif input_commands == "Next":
        print("Next")
        if currentNode and currentNode.getNextInPlaylist():     #if at current node and there is not None value returned  for the next node
            currentNode = currentNode.getNextInPlaylist()     #moves currentNode to next Song node in playlist

    input_commands = h.readline().rstrip()

h.close()

#end timer
end = timer()

#print program runtime
print()
print("************************")
print("***** Running Time *****")
print("************************")
print("Total Time of Program:", (end - start) * 1000, "milliseconds")
