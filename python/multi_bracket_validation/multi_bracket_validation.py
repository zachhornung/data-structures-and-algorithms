import re
# def find_brackets(string):
#   open_brackets = ['(', '{', '[']
#   close_brackets = [')', '}', ']']
#   compliments = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
#   opening_stack = []

#   for i, char in enumerate(string):
#     if (i < len(string)-1) and (char in open_brackets):
#       if (string[i+1] in close_brackets) and not(compliments[string[i+1]] == char):
#         return False

#     if char in open_brackets:
#       opening_stack.append(char)

#     if char in close_brackets:
#       if compliments[opening_stack[-1]] == char:
#         opening_stack.pop()

#   if not opening_stack:
#     return True
#   return False

def find_brackets(string):
  brackets = ['(', ')', '{', '}', '[', ']']
  matches = ['()', '{}', '[]']
  string = ''.join([char for char in string if char in brackets])
  while any(match in string for match in matches):
    string = string.replace('()', '').replace('{}', '').replace('[]', '')
  if string:
    return False
  return True

# def findClosing(c):
#     if c == '(':
#         return ')'
#     elif c == '{':
#         return '}'
#     elif c == '[':
#         return ']'
#     return -1
 
# # function to check if parenthesis
# # are balanced.
# def check(expr, n):
 
#     # Base cases
#     if n == 0:
#         return True
#     if n == 1:
#         return False
#     if expr[0] == ')' or \
#        expr[0] == '}' or expr[0] == ']':
#         return False
 
#     # Search for closing bracket for first
#     # opening bracket.
#     closing = findClosing(expr[0])
 
#     # count is used to handle cases like
#     # "((()))". We basically need to
#     # consider matching closing bracket.
#     i = -1
#     count = 0
#     for i in range(1, n):
#         if expr[i] == expr[0]:
#             count += 1
#         if expr[i] == closing:
#             if count == 0:
#                 break
#             count -= 1
 
#     # If we did not find a closing
#     # bracket
#     if i == n:
#         return False
 
#     # If closing bracket was next
#     # to open
#     if i == 1:
#         return check(expr[2:], n - 2)
 
#     # If closing bracket was somewhere
#     # in middle.
#     return check(expr[1:], i - 1) and \
#            check(expr[i + 1:], n - i - 1)
 
# # Driver Code

# expr = "[(])"
# n = len(expr)
 
# if check(expr, n):
#     print("Balanced")
# else:
#     print("Not Balanced")


