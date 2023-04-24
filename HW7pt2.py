#--------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.7 Part 2 
#     Due date: 03/23/2023
#
# Purpose:
#       trace input strings using a parsing table to determine if accepted or rejected
#--------------------------------------------------------------------------------------
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
  stack.append('S') # push S

  print(f"\ncurrent stack: {stack}")
  current = stack.pop() # pop S
  
  # parse thru input word
  while i < len(word):
    # state S
    if current == 'S':
      # case: [row S, col a]
      if input_word[i] == 'a':
        stack.append(list(parsing_table[0][0])[1]) # push a
        stack.append(list(parsing_table[0][0])[0]) # push W
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print("Potential Missing Arg.: 'a' \n")
        return False  # reject the word since it fell in one of the blank boxes in row S

    # state W
    elif current == 'W':
      # case: [row W, col =]
      if input_word[i] == '=':
        stack.append(list(parsing_table[1][8])[1]) # push =
        stack.append(list(parsing_table[1][8])[0]) # push E
        
        print(f"current stack: {stack}")
        current = stack.pop()
      
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '=' \n")
        return False # reject the word since it fell in one of the blank boxes in row W
    
    # state E
    elif current == 'E':
      # case: [row E, col a]
      if input_word[i] == 'a':
        stack.append(list(parsing_table[2][0])[1]) # push Q
        stack.append(list(parsing_table[2][0])[0]) # push T
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row E, col (]
      elif input_word[i] == '(':
        stack.append(list(parsing_table[2][3])[1]) # push Q
        stack.append(list(parsing_table[2][3])[0]) # push T
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '(' or 'a' \n")
        return False # reject the word since it fell in one of the blank boxes in row E

    # state Q
    elif current == 'Q':
      # case: [row Q, col +]
      if input_word[i] == '+':
        stack.append(list(parsing_table[3][1])[2]) # push Q
        stack.append(list(parsing_table[3][1])[1]) # push T
        stack.append(list(parsing_table[3][1])[0]) # push +
        
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row Q, col )]
      elif input_word[i] == ')':
        stack.append(list(parsing_table[3][4])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row Q, col $]
      elif input_word[i] == '$':
        stack.append(list(parsing_table[3][5])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row Q, col -]
      elif input_word[i] == '-':
        stack.append(list(parsing_table[3][6])[2]) # push Q
        stack.append(list(parsing_table[3][6])[1]) # push T
        stack.append(list(parsing_table[3][6])[0]) # push -
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', ')', or '-' \n")
        return False # reject the word since it fell in one of the blank boxes in row Q

    # state T
    elif current == 'T':
      # case: [row T, col a]
      if input_word[i] == 'a':
        stack.append(list(parsing_table[4][0])[1]) # push Q
        stack.append(list(parsing_table[4][0])[0]) # push T
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row T, col (]
      elif input_word[i] == '(':
        stack.append(list(parsing_table[4][3])[1]) # push Q
        stack.append(list(parsing_table[4][3])[0]) # push T
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '(' or 'a' \n")
        return False # reject the word since it fell in one of the blank boxes in row T

    # state R
    elif current == 'R':
      # case: [row R, col +]
      if input_word[i] == '+':
        stack.append(list(parsing_table[5][1])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row R, col *]
      elif input_word[i] == '*':
        stack.append(list(parsing_table[5][2])[2]) # push R
        stack.append(list(parsing_table[5][2])[1]) # push F
        stack.append(list(parsing_table[5][2])[0]) # push *
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row R, col )]
      elif input_word[i] == ')':
        stack.append(list(parsing_table[5][4])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row R, col $]
      elif input_word[i] == '$':
        stack.append(list(parsing_table[5][5])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row R, col -]
      elif input_word[i] == '-':
        stack.append(list(parsing_table[5][6])[0]) # push lambda
        
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row R, col /]
      elif input_word[i] == '/':
        stack.append(list(parsing_table[5][7])[2]) # push R
        stack.append(list(parsing_table[5][7])[1]) # push F
        stack.append(list(parsing_table[5][7])[0]) # push /
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '(', ''+', '-', '*', '/', or ')'")
        return False # reject the word since it fell in one of the blank boxes in row R

    # state F
    elif current == 'F':

      # case: [row F, col a]
      if input_word[i] == 'a':
        stack.append(list(parsing_table[6][0])[0]) # push a
        
        print(f"current stack: {stack}")
        current = stack.pop()
      
      # case: [row F, col ()]
      elif input_word[i] == '(':
        stack.append(list(parsing_table[6][3])[2]) # push )
        stack.append(list(parsing_table[6][3])[1]) # push E
        stack.append(list(parsing_table[6][3])[0]) # push (
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '(' or 'a' \n")
        return False # reject the word since it fell in one of the blank boxes in row R
  
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
parsing_table = [[ ' ' for x in range(9)] for y in range (7)]

# add values from predictive parsing table into parsing_table

# row S
parsing_table[0][0] = 'aW'   # [row S, column a] = aW

# row W
parsing_table[1][8] = '=E'   # [row W, column =] = =E

# row E
parsing_table[2][0] = 'TQ'   # [row E, column a] = TQ
parsing_table[2][3] = 'TQ'   # [row E, column (] = TQ

# row Q
parsing_table[3][1] = '+TQ' # [row Q, column +] = +TQ
parsing_table[3][4] = 'l'     # [row Q, column )] = lambda
parsing_table[3][5] = 'l'     # [row Q, column $] = lambda
parsing_table[3][6] = '-TQ' # [row Q, column -] = -TQ

# row T
parsing_table[4][0] = 'FR'   # [row T, column a] = FR
parsing_table[4][3] = 'FR'   # [row T, column (] = FR

# row R
parsing_table[5][1] = 'l'     # [row R, column +] = lambda
parsing_table[5][2] = '*FR' # [row R, column *] = *FR 
parsing_table[5][4] = 'l'     # [row R, column )] = lambda
parsing_table[5][5] = 'l'     # [row R, column $] = lambda
parsing_table[5][6] = 'l'     # [row R, column -] = lambda
parsing_table[5][7] = '/FR'   # [row R, column /] = /FR

# row F
parsing_table[6][0] = 'a'     # [row F, column a] = a
parsing_table[6][3] = '(E)' # [row F, column (] = (E)


# get input from user for the word to be checked
word = input("enter your word: ")

# print if it was accepted or rejected by the CFG
if check_grammar(parsing_table, word) is True:
  print(f"{word} is accepted by the CFG")
else:
  print(f"\n{word} is rejected by the CFG")