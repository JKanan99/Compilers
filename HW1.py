#-----------------------------------------------------------------------------------------
#     Group Names: Angela DeLeo, Roman Saddi, Jennah Kanan
#     Assignment No.1
#     Due date: 02/02/2023
#
# Purpose: This program reads an expression in postfix form, evaluates the expression
#          and displays its value
#-----------------------------------------------------------------------------------------
# Comment all functions and class members.
# Functions: 
# - convert_to_infix() : converts postfix into infix
# - solveInfix() : solves infix expression

def convert_to_infix(postfix_exp):
  """convert postfix expression into infix expression"""
  # initialize empty list to hold infix expression
  infix_exp = []

  # parse thru postfix expression
  for operand in postfix_exp:

    # break as soon as we see the $ in the expression
    if operand == '$':
      break

    # check if current index is a operand
    elif operand.isalpha():
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


def solveInfix():
  """converts the infix into a string and solves it using the given values"""
  # convert the list into a string
  infixString = convert_to_infix(expression)

  # replace the variables in the expression with their respective values
  pluggedString1 = infixString.replace("a", "5")
  pluggedString2 = pluggedString1.replace("b", "7")
  pluggedString3 = pluggedString2.replace("c", "2")
  pluggedString4 = pluggedString3.replace("d", "4")

  # solve the infix equation and print it
  answer = eval(pluggedString4)
  print("\t Value = ", answer)
  

# check to see if the $ is included in user input
while True:
  expression = input("Enter a postfix expression with a $ at the end: ")
  dollarSign = "$"
  # dollar sign is found, so we can solve the expression
  if dollarSign in expression:
      solveInfix()
  # dollar sign is not found, so ask user
  else:
    print("please include $ at end of expression.")
  # ask user if they want to continue
  if input("CONTINUE(y/n)? ") != "y":
    break
