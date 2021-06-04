def find_brackets(string):
  left_paren_counter = 0
  right_paren_counter = 0
  left_curly_counter = 0
  right_curly_counter = 0
  left_square_counter = 0
  right_square_counter = 0
  for char in string:
    if char == '(':
      left_paren_counter += 1
    if char == ')':
      right_paren_counter += 1
    if char == '{':
      left_curly_counter += 1
    if char == '}':
      right_curly_counter += 1
    if char == '[':
      left_square_counter += 1
    if char == ']':
      right_square_counter += 1
  if (left_paren_counter == right_paren_counter) and (left_curly_counter == right_curly_counter) and (left_square_counter == right_square_counter):
    return True
  return False