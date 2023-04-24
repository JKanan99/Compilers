#-----------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.3 Part 2
#     Due date: 02/16/2023
#
# Purpose:
#       given CFG: 
#                  S -> aS | bB |cC
#                  B -> bB |aC |cD | lambda
#                  C -> aS | bD | cD | lambda
#                  D -> bD | aB | cC
#       
#       determine whether an input string is accepted or rejected by the CFG.
#-----------------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions: check_grammar checks the grammar of a word, given table and word


## --- check_grammar function

def check_grammar(word, table):
  """checks the grammar of a given word using a given transition table"""

  # convert word to list of chars to parse thru
  word = list(word) 
  
  # initialize state, column, and index to 0
  state = 0
  col = 0
  i = 0

  # parse thru each character in the word
  while i < len(word):

    # switch (w[i])
    match w[i]:
      # case a, we are at column 0
      case "a":
        col = 0
      # case b, we are at column 1
      case "b":
        col = 1
      # case c, we are at column 2
      case "c":
        col = 2
      # case $, we are at the end of the word and ready to decide if it is accepted or not
      case "$":
        # if we are at one of the proper end states (1 or 2) we can accept the word
        if state == 1 or state == 2:
          print(f"{w} is accepted by the CFG.")
        # otherwise, the word is rejected
        else:
          print(f"{w} is rejected by the CFG.")
          
    state = table[state][col] # update current state
    i+=1 # go to the next character


## --- driver code

# transition table for given CFG
table = [
         [0,1,2], # state 0
         [2,1,3], # state 1
         [0,3,3], # state 2
         [1,3,2],  # state 3
         [4,4,4]  # state 4
        ] 

# receive input from user and make it lowercase
w = input("enter a word with $ at the end: ").lower()

# call function using inputted word and transition table
check_grammar(w, table)
