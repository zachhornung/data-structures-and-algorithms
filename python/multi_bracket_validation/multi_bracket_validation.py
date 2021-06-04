def find_brackets(string):
  open_brackets = ['(', '{', '[']
  close_brackets = [')', '}', ']']
  compliments = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
  opening_stack = []

  for i, char in enumerate(string):
    if (i < len(string)-1) and (char in open_brackets):
      if (string[i+1] in close_brackets) and not(compliments[string[i+1]] == char):
        return False

    if char in open_brackets:
      opening_stack.append(char)

    if char in close_brackets:
      if compliments[opening_stack[-1]] == char:
        opening_stack.pop()

  if not opening_stack:
    return True
  return False