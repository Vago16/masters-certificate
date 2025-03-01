# AHPA #19 - Dr. King's Speech
#
# Using sets I want you to calculate how 
# many unique words there are in Dr. 
# King’s “I Have A Dream” speech.
#
# Using sets I want you to calculate how 
# many unique words there are in Dr. 
# King’s “Letter From the Birmingham 
# City Jail” text.
#
# Next, I’d like to know how many of 
# the words in the “I have a dream 
# speech” were also used in the “Letter 
# From the Birmingham City Jail” text 
# (count).
#
# Now tell me what words that were used 
# in the “I have a dream” speech were 
# NOT used in the “Letter From the 
# Birmingham City Jail” text (list).
#

lowerLine = line.lower()
strippedLine = lowerLine.strip(".,\n")
listLine = strippedLine.split()
speechList.extend(listLine)