# AHPA #13 - The Blizzard Problem
#
# Print out the lists: one item per line.
#
# In the Candy Cravers list, print
# the Heath item’s location.
#
# In the Classic Creations list,
# print the Royal Rocky Road item.
#
# Add a new Classic Creation: "red
# licorice".
#
# Print new list.
#
# Remove the Heath Blizzard from
# Candy Cravers.
#
# Print new list.
# Combine the lists and print on
# one line
#
# Print a count of the total number
# of treats provided
#
# Student Name: Evagelos Petropoulos
#
candyCravers = [
    "Reese’s Peanut ButterCup", "Butterfinger", "Oreo", "Heath", "M&M’s"
]

classicCreations = [
    "Banana Split", "Salted Caramel Truffle",
    "M&M’s Peanut Butter Monster Cookie", "Georgia Mud Fudge",
    "Double Fudge Cookie Dough", "Chocolate Xtreme",
    "Peanut Butter Cookie Dough Smash", "Chocolate Chip Cookie Dough",
    "Royal Rocky Road", "Chocolate Covered Strawberry",
    "Choco Covered Strawberry", "Royal Rocky Road", "Turtle Pecan Cluster",
    "Mint Oreo", "Royal New York Cheesecake", "Royal Oreo"
]
#prints out list
for item in candyCravers:
    print('{0}'.format(item))
#prints out list
for item in classicCreations:
    print('{0}'.format(item))

#prints Heath's item's location
heath_location = candyCravers.index('Heath')
print('Heath\'s location in the list is: {0}'.format(heath_location))

#prints the Royal Rocky Road item
print(classicCreations[11])

#adds a new Classic Creation: "red licorice" and print new list
classicCreations.append('red licorice')
print(classicCreations)

#removes the Heath Blizzard from Candy Cravers and prints new list
candyCravers.remove('Heath')
print(candyCravers)

#combine the lists and print on one line
new_list = candyCravers + classicCreations
print(new_list)

#prints total number of treats provided
print(len(new_list), 'treats in total.')