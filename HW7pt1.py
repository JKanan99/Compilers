#-----------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.7 Part 1
#     Due date: 03/23/2023
# Purpose:
#     trace input strings using a parsing table to determine if accepted or rejected
#-----------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions:
#       check_grammar checks the grammar of an inputted word using a parsing table

def check_grammar(parsing_table, word):
 """ checks the grammar of a word using a parsing_table """
 input_word = list(word) # convert word into list of chars for parsing

 # check to make sure $ is at the end of the string first
 if input_word[len(word) - 1] != '$':
   print(f"\nMissing '$' after position {len(word)} of {word}")
   return False

 # declare stack and counter i
 stack = [] # initialize an empty stack
 i = 0 # initialize counter to go thru the entire word
  # begin the stack
 stack.append('$') # push $
 stack.append('E') # push E

 print(f"\ncurrent stack: {stack}")
 current = stack.pop() # pop E
 
 # parse thru input word
 while i < len(word):
   # state E
   if current == 'E':
     # case: [row E, col i]
     if input_word[i] == 'i':
       stack.append(list(parsing_table[0][0])[1]) # push Q
       stack.append(list(parsing_table[0][0])[0]) # push T
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     elif input_word[i] == '(':
       stack.append(list(parsing_table[0][5])[1]) # push Q
       stack.append(list(parsing_table[0][5])[0]) # push T

      
       print(f"current stack: {stack}")
       current = stack.pop()
      

     else:
       print("Potential Missing Arg.: 'i' or '(' \n")
       return False  # reject the word since it fell in one of the blank boxes in row S

   # state Q
   elif current == 'Q':
     # case: [row Q, col +]
     if input_word[i] == '+':
       stack.append(list(parsing_table[1][1])[2]) # push Q
       stack.append(list(parsing_table[1][1])[1]) # push T
       stack.append(list(parsing_table[1][1])[0]) # push +
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row Q, col -]
     elif input_word[i] == '-':
       stack.append(list(parsing_table[1][2])[2]) # push Q
       stack.append(list(parsing_table[1][2])[1]) # push T
       stack.append(list(parsing_table[1][2])[0]) # push -
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row Q, col )]
     elif input_word[i] == ')':
       stack.append(list(parsing_table[1][6])[0]) # push lamda
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row Q, col $]
     elif input_word[i] == '$':
       stack.append(list(parsing_table[1][7])[0]) # push lamda
      
       print(f"current stack: {stack}")
       current = stack.pop()
    
     else:
       print(f"Potential Missing Arg. after position {i} of {word}: '+', '-' ')' or '$' \n")
       return False # reject the word since it fell in one of the blank boxes in row W
  
   # state T
   elif current == 'T':
     # case: [row T, col i]
     if input_word[i] == 'i':
       stack.append(list(parsing_table[2][0])[1]) # push R
       stack.append(list(parsing_table[2][0])[0]) # push F
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row T, col (]
     elif input_word[i] == '(':
       stack.append(list(parsing_table[2][5])[1]) # push R
       stack.append(list(parsing_table[2][5])[0]) # push F
      
       print(f"current stack: {stack}")
       current = stack.pop()

     else:
       print(f"Potential Missing Arg. after position {i} of {word}: '(' or 'i' \n")
       return False # reject the word since it fell in one of the blank boxes in row E

   # state R
   elif current == 'R':
     # case: [row R, col +]
     if input_word[i] == '+':
       stack.append(list(parsing_table[3][1])[0]) # push lamda
      
       print(f"current stack: {stack}")
       current = stack.pop()

     # case: [row R, col -]
     elif input_word[i] == '-':
       stack.append(list(parsing_table[3][2])[0]) # push lambda
      
       print(f"current stack: {stack}")
       current = stack.pop()

     # case: [row R, col *]
     elif input_word[i] == '*':
       stack.append(list(parsing_table[3][3])[2]) # push R
       stack.append(list(parsing_table[3][3])[1]) # push F
       stack.append(list(parsing_table[3][3])[0]) # push *
      
       print(f"current stack: {stack}")
       current = stack.pop()

     # case: [row R, col /]
     elif input_word[i] == '/':
       stack.append(list(parsing_table[3][4])[2]) # push R
       stack.append(list(parsing_table[3][4])[1]) # push F
       stack.append(list(parsing_table[3][4])[0]) # push /
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row R, col )]
     elif input_word[i] == ')':
       stack.append(list(parsing_table[3][6])[0]) # push lamda
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row R, col $]
     elif input_word[i] == '$':
       stack.append(list(parsing_table[3][7])[0]) # push lamda
      
       print(f"current stack: {stack}")
       current = stack.pop()
    
      
     else:
       print(f"Potential Missing Arg. after position {i} of {word}: '$', '*', '/', '+', ')', or '-' \n")
       return False # reject the word since it fell in one of the blank boxes in row Q

   # state F
   elif current == 'F':
     # case: [row F, col a]
     if input_word[i] == 'i':
       stack.append(list(parsing_table[4][0])[0]) # push i

       print(f"current stack: {stack}")
       current = stack.pop()
      
     # case: [row F, col (]
     elif input_word[i] == '(':
       stack.append(list(parsing_table[4][5])[2]) # push )
       stack.append(list(parsing_table[4][5])[1]) # push E
       stack.append(list(parsing_table[4][5])[0]) # push (
      
       print(f"current stack: {stack}")
       current = stack.pop()
      
     else:
       print(f"Potential Missing Arg. after position {i} of {word}: '(' or 'i' \n")
       return False # reject the word since it fell in one of the blank boxes in row T

# if the current item that was popped matches the current char in the word
   elif current == word[i]:
     print(f"\nmatched {word[i]}")
    
     print(f"current stack: {stack}")
    
     i += 1
     current = stack.pop()

   # if the current item that was popped is lambda, pop again
   elif current == 'l':
     print(f"current stack: {stack}")
     current = stack.pop()

   # once the stack is empty, we know our word is accepted
   if stack == []:
     print(f"current stack: {stack}\n")
     return True

# initialize parsing_table to contain blank spaces for all entries
parsing_table = [[ ' ' for x in range(9)] for y in range (5)]

# add values from predictive parsing table into parsing_table

# row E
parsing_table[0][0] = 'TQ'   # [row E, column i] = TQ *same idea for the rest*
parsing_table[0][5] = 'TQ'

# row Q
parsing_table[1][1] = '+TQ'
parsing_table[1][2] = '-TQ'
parsing_table[1][6] = 'l'
parsing_table[1][7] = 'l'

# row T
parsing_table[2][0] = 'FR' 
parsing_table[2][5] = 'FR'  

# row R
parsing_table[3][1] = 'l'
parsing_table[3][2] = 'l' 
parsing_table[3][3] = '*FR'  
parsing_table[3][4] = '/FR'
parsing_table[3][6] = 'l'
parsing_table[3][7] = 'l'

# row F
parsing_table[4][0] = 'i'  
parsing_table[4][5] = '(E)' 

# get input from user for the word to be checked
word = input("enter your word: ")

# print if it was accepted or rejected by the CFG
if check_grammar(parsing_table, word) is True:
 print(f"{word} is accepted by the CFG")
else:
 print(f"\n{word} is rejected by the CFG")