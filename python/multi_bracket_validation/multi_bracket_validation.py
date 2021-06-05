def find_brackets(string):
  string = ''.join([char for char in string if char in '(){}[]'])
  while any(x in string for x in ['()', '{}', '[]']):
    string = string.replace('()', '').replace('{}', '').replace('[]', '')
  return not string

