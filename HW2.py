#-----------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.2
#     Due date: 02/09/2023
#
# Purpose: Write a program to find the value of a postfix expression. Variables are one or more 
#          characters each. We might have some integer numbers as part of the expression.
#-----------------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions: 
# - convert_to_infix() : converts postfix into infix
# - variable_input() : subsitutes user input variables into expression



def convert_to_infix(postfix_exp):
  """convert postfix expression into infix expression"""

  # split the postfix expression to separate variables, integers, and operators
  postfix_list = postfix_exp.split()
  
  # initialize empty list to hold infix expression
  infix_exp = []

  # parse thru postfix expression
  for operand in postfix_list:
    
    # break as soon as we see the $ in the expression
    if operand == '$':
      break

    # check if current index is a operand
    elif operand.isalpha():
      infix_exp.insert(0, operand)

    elif operand.isdigit():
      infix_exp.insert(0, operand)

    # current index is operator, so we form groupings
    else:

      # part after previous operand
      group1 = infix_exp[0]
      infix_exp.pop(0)
      # print(f'\n group 1: {group1}')

      # part before previous operand
      group2 = infix_exp[0]
      infix_exp.pop(0)
      # print(f'\n group 2: {group2}')

      # group together with parantheses separating each piece of the expression
      infix_exp.insert(0, '(' + group2 + operand + group1 + ')')
      # print(f' current infix_exp: {infix_exp}')

  return infix_exp[0]


def variable_input(expression):
  """extract variables from given expression and give values"""
  
  # split the string into a list of smaller strings 
  split = expression.split()
  split_length = len(split)
  
  # for each smaller string in the list, 
  # check if its an alpha (word), if it is, replace it with the user input
  for x in range(split_length):
    if split[x].isalpha() == True:
       i = str()
       y = input("\t\tEnter the value of " + split[x] + ": ") 
       split[x] = y
  
  #put the list back together into one string ( post fix expression )
  final_string = str()
  for elem in split: #or whatever return result 
    final_string += str(elem) + " "

  return final_string


# check to see if the $ is included in user input
while True:
  expression = input("\nEnter a postfix expression with a $ at the end: \n\t")
  dollarSign = "$"
  
  # dollar sign is found, so we can solve the expression
  if dollarSign in expression:

      # call variable_input to give values to variables
      post_fix = variable_input(expression)

      # convert postfix expression to infix
      infix = convert_to_infix(post_fix)
    
      ans = eval(infix)
      print(f"\t\t  Expression's value is {ans}")
    
      # evaluate infix expression

      
  # dollar sign is not found, so ask user
  else:
    print("please include $ at end of expression.")
  
    # ask user if they want to continue
  if input("\t\tCONTINUE(y/n)? ") != "y":
    break

print()