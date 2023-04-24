#-----------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.8
#     Due date: 04/11/2023
# Purpose:
#     trace input strings using an LR parsing table to determine if accepted or rejected
#-----------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions:
#       check_grammar checks the grammar of an inputted word using a parsing table
#       entry_Rn is used for rule checking when an entry falls in Rn


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

  stack.append('0') # push 0

  print(f"\ncurrent stack: {stack}")
  current = stack.pop() # pop 0

  def entry_Rn(n):
    """ When the entry is Rn do the following steps at specified rule # n """
    
    if n == '1':
      # rule 1: E -> E + T 
      # 2 * |E + T| = 2 * 3 = 6 
      # pop 6 times
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      
      popped = stack.pop()
    
      # push popped, E, and entry at [popped, E]
      stack.append(popped)
      stack.append('E')
      stack.append(LR_parsing_table[int(popped)][8])

    elif n == '2':
      # rule 2: E -> E - T 
      # 2 * |E - T| = 2 * 3 = 6 
      # pop 6 times
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      
      popped = stack.pop()
    
      # push popped, E, and entry at [popped, E]
      stack.append(popped)
      stack.append('E')
      stack.append(LR_parsing_table[int(popped)][8])
      
    elif n == '3':
      # rule 3: E -> T 
      # 2 * |T| = 2 * 1 = 2 
      # pop 2 times
      stack.pop()
      stack.pop()
      popped = stack.pop()
    
      # push popped, E, and entry at [popped, E]
      stack.append(popped)
      stack.append('E')
      stack.append(LR_parsing_table[int(popped)][8])

    elif n == '4':
      # rule 4: T -> T * F 
      # 2 * |T * F| = 2 * 3 = 6 
      # pop 6 times
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      
      popped = stack.pop()
    
      # push popped, T, and entry at [popped, T]
      stack.append(popped)
      stack.append('T')
      stack.append(LR_parsing_table[int(popped)][9])

    elif n == '5':
      # rule 5: T -> T / F 
      # 2 * |T / F| = 2 * 3 = 6 
      # pop 6 times
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      
      popped = stack.pop()
    
      # push popped, T, and entry at [popped, T]
      stack.append(popped)
      stack.append('T')
      stack.append(LR_parsing_table[int(popped)][9])

    elif n == '6':
      # rule 6: T -> F 
      # 2 * |F| = 2 * 1 = 2 
      # pop 2 times
      stack.pop()
      stack.pop()
  
      popped = stack.pop()
  
      # push popped, T, and entry at [popped, T]
      stack.append(popped)
      stack.append('T')
      stack.append(LR_parsing_table[int(popped)][9])

    elif n == '7':
      # rule 7: F -> ( E )
      # 2 * |( E )| = 2 * 3 = 6
      # pop 6 times
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()
      stack.pop()

      # pop next item to continue parsing
      popped = stack.pop()

      # push popped, F, and entry at [popped, F]
      stack.append(popped)
      stack.append('F')
      stack.append(LR_parsing_table[int(popped)][10])
      
    elif n == '8':
      # rule 8: F -> i
      # 2 * |i| = 2 * 1 = 2
      # pop 2 times
      stack.pop()
      stack.pop()

      # pop next item to continue parsing
      popped = stack.pop()

      # push popped, F, and entry at [popped, F]
      stack.append(popped)
      stack.append('F')
      stack.append(LR_parsing_table[int(popped)][10])

  
  # parse thru input word
  while i < len(word):
      
    # state 0  
    if current == '0':
      # case: [row 0, col i] = S5
      if input_word[i] == 'i':
        # push 0, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[0][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 0, col (] = S4
      elif input_word[i] == '(':
        # push 0, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[0][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 0

    # state 1
    elif current == '1':
      # case: [row 1, col +] = S6
      if input_word[i] == '+':
        # push 1, +, 6
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[1][1])[1])

        print(f"current stack: {stack}")
        current = stack.pop()   
        i += 1
        
      # case: [row 1, col -] = S7
      elif input_word[i] == '-':
        # push 1, -, 7
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[1][2])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 1, col $] = ACC
      elif input_word[i] == '$':
        return True

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+' or '-' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 1

    # state 2
    elif current == '2':
      # case: [row 2, col +] = R3
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('3')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 2, col -] = R3
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('3')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 2, col *] = S8
      elif input_word[i] == '*':
        # push 2, *, 8
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[2][3])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 2, col /] = S9
      elif input_word[i] == '/':
        # push 2, /, 9
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[2][4])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 2, col )] = R3
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('3')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 2, col $] = R3
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('3')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 2

    # state 3
    elif current == '3':
      # case: [row 3, col +] = R6
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 3, col -] = R6
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
    
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 3, col *] = R6
      elif input_word[i] == '*':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 3, col /] = R6
      elif input_word[i] == '/':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 3, col )] = R6
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 3, col $] = R6
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('6')
        print(f"current stack: {stack}")
        current = stack.pop()
        

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 3

    # state 4
    elif current == '4':
      # case: [row 4, col i] = S5
      if input_word[i] == 'i':
        # push 4, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[4][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 4, col (] = S4
      elif input_word[i] == '(':
        # push 4, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[4][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 4

    # state 5
    elif current == '5':
      # case: [row 5, col +] = R8
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 5, col -] = R8
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 5, col *] = R8
      elif input_word[i] == '*':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 5, col /] = R8
      elif input_word[i] == '/':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 5, col )] = R8
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 5, col $] = R8
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('8')
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 5

    # state 6
    elif current == '6':
      # case: [row 6, col i] = S5
      if input_word[i] == 'i':
        # push 6, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[6][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 6, col (] = S4
      elif input_word[i] == '(':
        # push 6, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[6][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 6

    # state 7
    elif current == '7':
      # case: [row 7, col i] = S5
      if input_word[i] == 'i':
        # push 7, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[7][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 7, col (] = S4
      elif input_word[i] == '(':
        # push 7, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[7][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 7

    # state 8
    elif current == '8':
      # case: [row 8, col i] = S5
      if input_word[i] == 'i':
        # push 8, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[8][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 8, col (] = S4
      elif input_word[i] == '(':
        # push 8, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[8][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 8

    # state 9
    elif current == '9':
      # case: [row 9, col i] = S5
      if input_word[i] == 'i':
        # push 9, i, 5
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[9][0])[1])
    
        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      # case: [row 9, col (] = S4
      elif input_word[i] == '(':
        # push 9, (, 4
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[9][5])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      else:
        print(f"Potential Missing Arg. after position {i} of {word}: 'i' or '(' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 9

    # state 10
    elif current == '10':
      # case: [row 10, col +] = S6
      if input_word[i] == '+':
        # push 10, +, 6
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[10][1])[1])

        print(f"current stack: {stack}")
        current = stack.pop()   
        i += 1
        
      # case: [row 10, col -] = S7
      elif input_word[i] == '-':
        # push 10, -, 7
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[10][2])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 10, col )] = S15
      elif input_word[i] == ')':
        # push 10, ), 15
        stack.append(current)
        stack.append(input_word[i])
        stack.append('15')

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 10

    # state 11
    elif current == '11':
      # case: [row 11, col +] = R1
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('1')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 11, col -] = R1
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('1')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 11, col *] = S8
      elif input_word[i] == '*':
        # push 11, *, 8
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[11][3])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 11, col /] = S9
      elif input_word[i] == '/':
        # push 11, /, 9
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[11][4])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 11, col )] = R1
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('1')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 11, col $] = R1
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('1')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 11

    # state 12
    elif current == '12':
      # case: [row 12, col +] = R2
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('2')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 12, col -] = R2
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('2')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 12, col *] = S8
      elif input_word[i] == '*':
        # push 12, *, 8
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[12][3])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 12, col /] = S9
      elif input_word[i] == '/':
        # push 11, /, 9
        stack.append(current)
        stack.append(input_word[i])
        stack.append(list(LR_parsing_table[12][4])[1])

        print(f"current stack: {stack}")
        current = stack.pop()
        i += 1
        
      # case: [row 12, col )] = R2
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('2')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 12, col $] = R2
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('2')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 12

    # state 13
    elif current == '13':
      # case: [row 13, col +] = R4
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 13, col -] = R4
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 13, col *] = R4
      elif input_word[i] == '*':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 13, col /] = R4
      elif input_word[i] == '/':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 13, col )] = R4
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 13, col $] = R4
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('4')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 13

    # state 14
    elif current == '14':
      # case: [row 14, col +] = R5
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 14, col -] = R5
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 14, col *] = R5
      elif input_word[i] == '*':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 14, col /] = R5
      elif input_word[i] == '/':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 14, col )] = R5
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 14, col $] = R5
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('5')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 14

    # state 15
    elif current == '15':
      # case: [row 15, col +] = R7
      if input_word[i] == '+':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')

        print(f"current stack: {stack}")
        current = stack.pop()

      # case: [row 15, col -] = R7
      elif input_word[i] == '-':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 15, col *] = R7
      elif input_word[i] == '*':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')

        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 15, col /] = R7
      elif input_word[i] == '/':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 15, col )] = R7
      elif input_word[i] == ')':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')
        
        print(f"current stack: {stack}")
        current = stack.pop()
        
      # case: [row 15, col $] = R7
      elif input_word[i] == '$':
        # push current back into stack
        stack.append(current)
        entry_Rn('7')
        
        print(f"current stack: {stack}")
        current = stack.pop()

      else:
        print(f"Potential Missing Arg. after position {i} of {word}: '+', '-', '*', '/' or ')' \n")
        return False  # reject the word since it fell in one of the blank boxes in row 15



# initialize LR_parsing_table to contain blank spaces for all entries
LR_parsing_table = [[ ' ' for x in range(11)] for y in range (16)]

# row 0
LR_parsing_table[0][0] = 'S5'   # [row 0, column i] = S5
LR_parsing_table[0][5] = 'S4'   # [row 0, column (] = S4
LR_parsing_table[0][8] = '1'    # [row 0, column E] = 1
LR_parsing_table[0][9] = '2'    # [row 0, column T] = 2
LR_parsing_table[0][10] = '3'   # [row 0, column F] = 3

# row 1
LR_parsing_table[1][1] = 'S6'   # [row 1, column +] = S6
LR_parsing_table[1][2] = 'S7'   # [row 1, column -] = S7
LR_parsing_table[1][7] = 'ACC'  # [row 1, column $] = ACC

# row 2
LR_parsing_table[2][1] = 'R3'   # [row 2, column +] = R3
LR_parsing_table[2][2] = 'R3'   # [row 2, column -] = R3
LR_parsing_table[2][3] = 'S8'   # [row 2, column *] = S8
LR_parsing_table[2][4] = 'S9'   # [row 2, column /] = S9
LR_parsing_table[2][6] = 'R3'   # [row 2, column )] = R3
LR_parsing_table[2][7] = 'R3'   # [row 2, column $] = R3

# row 3
LR_parsing_table[3][1] = 'R6'   # [row 3, column +] = R6
LR_parsing_table[3][2] = 'R6'   # [row 3, column -] = R6
LR_parsing_table[3][3] = 'R6'   # [row 3, column *] = R6
LR_parsing_table[3][4] = 'R6'   # [row 3, column /] = R6
LR_parsing_table[3][6] = 'R6'   # [row 3, column )] = R6
LR_parsing_table[3][7] = 'R6'   # [row 3, column $] = R6

# row 4
LR_parsing_table[4][0] = 'S5'   # [row 4, column i] = S5
LR_parsing_table[4][5] = 'S4'   # [row 4, column (] = S4
LR_parsing_table[4][8] = '10'   # [row 4, column E] = 10
LR_parsing_table[4][9] = '2'    # [row 4, column T] = 2
LR_parsing_table[4][10] = '3'   # [row 4, column F] = 3

# row 5
LR_parsing_table[5][1] = 'R8'   # [row 5, column +] = R8
LR_parsing_table[5][2] = 'R8'   # [row 5, column -] = R8
LR_parsing_table[5][3] = 'R8'   # [row 5, column *] = R8
LR_parsing_table[5][4] = 'R8'   # [row 5, column /] = R8
LR_parsing_table[5][6] = 'R8'   # [row 5, column )] = R8
LR_parsing_table[5][7] = 'R8'   # [row 5, column $] = R8

# row 6
LR_parsing_table[6][0] = 'S5'   # [row 6, column i] = S5
LR_parsing_table[6][5] = 'S4'   # [row 6, column (] = S4
LR_parsing_table[6][9] = '11'   # [row 6, column T] = 11
LR_parsing_table[6][10] = '3'   # [row 6, column F] = 3

# row 7
LR_parsing_table[7][0] = 'S5'   # [row 7, column i] = S5
LR_parsing_table[7][5] = 'S4'   # [row 7, column (] = S4
LR_parsing_table[7][9] = '12'   # [row 7, column T] = 12
LR_parsing_table[7][10] = '3'   # [row 7, column F] = 3

# row 8
LR_parsing_table[8][0] = 'S5'   # [row 8, column i] = S5
LR_parsing_table[8][5] = 'S4'   # [row 8, column (] = S4
LR_parsing_table[8][10] = '13'  # [row 8, column F] = 13

# row 9
LR_parsing_table[9][0] = 'S5'   # [row 9, column i] = S5
LR_parsing_table[9][5] = 'S4'   # [row 9, column (] = S4
LR_parsing_table[9][10] = '14'  # [row 9, column F] = 14

# row 10
LR_parsing_table[10][1] = 'S6'  # [row 10, column +] = S6
LR_parsing_table[10][2] = 'S7'  # [row 10, column -] = S7
LR_parsing_table[10][6] = 'S15' # [row 10, column )] = S15

# row 11
LR_parsing_table[11][1] = 'R1'  # [row 11, column +] = R1
LR_parsing_table[11][2] = 'R1'  # [row 11, column -] = R1
LR_parsing_table[11][3] = 'S8'  # [row 11, column *] = S8
LR_parsing_table[11][4] = 'S9'  # [row 11, column /] = S9
LR_parsing_table[11][6] = 'R1'  # [row 11, column )] = R1
LR_parsing_table[11][7] = 'R1'  # [row 11, column $] = R1

# row 12
LR_parsing_table[12][1] = 'R2'  # [row 12, column +] = R2
LR_parsing_table[12][2] = 'R2'  # [row 12, column -] = R2
LR_parsing_table[12][3] = 'S8'  # [row 12, column *] = S8
LR_parsing_table[12][4] = 'S9'  # [row 12, column /] = S9
LR_parsing_table[12][6] = 'R2'  # [row 12, column )] = R2
LR_parsing_table[12][7] = 'R2'  # [row 12, column $] = R2

# row 13
LR_parsing_table[13][1] = 'R4'  # [row 13, column +] = R4
LR_parsing_table[13][2] = 'R4'  # [row 13, column -] = R4
LR_parsing_table[13][3] = 'R4'  # [row 13, column *] = R4
LR_parsing_table[13][4] = 'R4'  # [row 13, column /] = R4
LR_parsing_table[13][6] = 'R4'  # [row 13, column )] = R4
LR_parsing_table[13][7] = 'R4'  # [row 13, column $] = R4

# row 14
LR_parsing_table[14][1] = 'R5'  # [row 14, column +] = R5
LR_parsing_table[14][2] = 'R5'  # [row 14, column -] = R5
LR_parsing_table[14][3] = 'R5'  # [row 14, column *] = R5
LR_parsing_table[14][4] = 'R5'  # [row 14, column /] = R5
LR_parsing_table[14][6] = 'R5'  # [row 14, column )] = R5
LR_parsing_table[14][7] = 'R5'  # [row 14, column $] = R5

# row 15
LR_parsing_table[15][1] = 'R7'  # [row 13, column +] = R7
LR_parsing_table[15][2] = 'R7'  # [row 13, column -] = R7
LR_parsing_table[15][3] = 'R7'  # [row 13, column *] = R7
LR_parsing_table[15][4] = 'R7'  # [row 13, column /] = R7
LR_parsing_table[15][6] = 'R7'  # [row 13, column )] = R7
LR_parsing_table[15][7] = 'R7'  # [row 13, column $] = R7

# get input from user for the word to be checked
word = input("enter your word: ")

# print if it was accepted or rejected by the CFG
if check_grammar(LR_parsing_table, word) is True:
  print(f"\n{word} is accepted by the CFG")
else:
  print(f"\n{word} is rejected by the CFG")
  