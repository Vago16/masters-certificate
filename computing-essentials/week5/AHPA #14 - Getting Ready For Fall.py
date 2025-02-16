# AHPA #14 - Getting Ready For Fall
#
# ACG 2021 Princ Financial Accounting
# AMH 2010 Pilot American History I
# ARC 2180 Intro Digital Architecture
# ASL 4202 Pilot American Sign Language
# ARC 2180 Pilot Intro Digital Architecture
#
# Use the data to create a list
#
# Insert "Fall 2026" at the start 
# of each of the class listings
# 
# Place "Room: TBD" at the end of 
# each class listing
# 
# If any of the courses have 
# "Pilot" in their title, that is 
# to be removed
# 
# If there are any duplicates, then 
# they are to be removed
# 
# A copy of your list is to be 
# created
# 
# The final list of student catalog 
# data is then to be printed out
# 
# Student Name: Evagelos Petropoulos
#
fall_list = ['ACG 2021 Princ Financial Accounting','AMH 2010 Pilot American History I','ARC 2180 Intro Digital Architecture',
             'ASL 4202 Pilot American Sign Language','ARC 2180 Pilot Intro Digital Architecture']

def class_list():
    new_list = []       #holds new elements being created
    fresh_list = []
    dupe_list = []      #list to hold duplicate values
    for i in fall_list:
        if i not in fresh_list:
            fresh_list.append(i)        #class list with no duplicate values
        else:
            dupe_list.append(i)         #any duplicate values go here
    print('This is the class list without any duplicates: {0}.'.format(fresh_list))
    print('Here are the duplicate classes: {0}.'.format(dupe_list))
            
    for fall_class in fall_list:
        
        fall_class = "Fall 2026 " + fall_class + ' Room: TBD'       #new elements with requested information
        new_list.append(fall_class)
        if 'Pilot' in fall_class:       #removes element if 'Pilot' is found in the element
            fall_class = new_list.pop()

    return('Here is the final class list: {0}'.format(new_list)) 

print(class_list())




