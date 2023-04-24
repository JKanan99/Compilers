#-----------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.3 Part 1
#     Due date: 02/16/2023
#
# Purpose: 
#-----------------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions:

import string

#extract data from sample file and read it into one big string
sampleFile = open("hw3Sample.txt", "r")
sampleString = sampleFile.read()
sampleFile.close()


#create the heading of the table
heading = [["token", "number", "identifier", "reserved word"]]
for row in heading:
  print('| {:10} | {:^4} | {:>4} | {:<3} |'.format(*row))

  
#turn string into list and iterate through words
for w in sampleString.split("\n"):
  #iterate through words in list letter by letter
  number = True
  identifier = True
  reserved = False
  
  for element in range(0, len(w)):

    #Check first character in w ; if number, w is not an identifier
    if(w[0].isnumeric()):
      identifier = False

    #Iterate through each character in w ; not a number if letter or underscore exists
    if(w[element].isalpha() == True) or (w[element] == "_"):
      number = False

    #Iterate through each character in w ; not an identifier if dash or space exists
    if(w[element] == "-") or (w[element] == " "):
      identifier = False

    #Check for reserved characters
    if("While" in w or "for" in w or "switch" in w or "do" in w or "return" in w):
      reserved = True

  #print out the table information
  table = [[w, ("no", "yes")[number], ("no", "yes")[identifier], ("no", "yes")[reserved]]]
  for row in table:
    print('| {:10} | {:^6} | {:>10} | {:<13} |'.format(*row))

print("...........")
  

