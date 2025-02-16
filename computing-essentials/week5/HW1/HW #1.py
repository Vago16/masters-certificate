#
# COP 5008 Homework #1 - Mpox Diagnostics
#
# Evagelos Petropoulos
#
# Open data file

# Ask Questions

# Display result of questionaire
infile = open("HW #1 Data.txt", "r")
data = infile.readline()
print(data)

for line in infile:
  print(line)