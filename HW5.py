#-----------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.5 
#     Due date: 03/02/2023
#
# Purpose:
#       
#-----------------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions: 

import string

#open and save the contents of h5.txt into compileString
compileFile = open("h5.txt", "r")
compileString = compileFile.read()
compileFile.close()

#split compileString into a list of words
compileList = compileString.split(" ")

#--------------------------------------------------------
#alter compileString
#STEP 1: remove comments within the format **comment**

#create a flag indicating when ** starts and ends
deleteFlag = False
#create a loop iterating through all words in compileList
for w in range(len(compileList)):
  #identify when an ending ** is connected to a \n
  if "\n" in compileList[w] and "**" in compileList[w] and deleteFlag == True:
    compileList[w] = "\n"
    deleteFlag = False
  #identify when a starting ** is connected to a \n
  elif "\n" in compileList[w] and "**" in compileList[w]:
    compileList[w] = "\n"
    deleteFlag = True
  #identify the second occurance of **
  elif deleteFlag == True and "**" in compileList[w]:
    compileList[w]= " "
    deleteFlag = False
  #identify the first occurance of **
  elif "**" in compileList[w]:
    deleteFlag = True
  #delete the word if deleteFlag is True
  if deleteFlag == True:
    compileList[w]= " "

#-------------------------------------------------
#STEP 2: remove any unnessesary new lines

#create a newLine flag to indicate a NL had been used already
newLineExists = True

for w in range(len(compileList)):
  nlCheck = compileList[w]
  #converge multiple uses of \n into a single \n
  if nlCheck.count("\n") > 1:
    compileList[w] = "\n"

  #Identify the unneeded newLine
  if newLineExists == True and "\n" not in compileList[w] and compileList[w] != " " and compileList[w] != "":
    newLineExists = False
  elif newLineExists == True  and compileList[w] == "\n":
    compileList[w] = " "
    newLineExists = False
  elif newLineExists == False and "\n" in compileList[w]:
    newLineExists = True
      

#-------------------------------------------------
#STEP 3: remove any unneccesary spaces

#create a counter for # of deletions to fix allignment
deleteCount = 0

#iterate through the list of words
for w in range(len(compileList)):
  #delete unneeded space if another space exists directly before it
  if compileList[w - deleteCount] == " " and compileList[w - deleteCount - 1] == " ":
    deleteCount = deleteCount + 1
    temp = compileList[w - deleteCount]
    compileList.remove(temp)


#-------------------------------------------------------
#join together compileList into the string compileString
  
compileString = " ".join(compileList)

#--------------------------------------------------------
#open newh5.txt and push the contents of compileString into it
outputFile = open("newh5.txt", "w")
outputFile.write(compileString)
outputFile.close()