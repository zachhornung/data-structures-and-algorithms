from multi_bracket_validation.multi_bracket_validation import find_brackets

def test_import():
  assert find_brackets
  
def test_good_strings():
  string1 = '(hello) {world} [baby] goats'
  string2 = '((((())))){{{{{}}}}}[[[[[]]]]]'
  assert (find_brackets(string1) == True) and (find_brackets(string2) == True)
  
def test_bad_strings():
  string1 = '(hello) {world [baby] goats'
  string2 = '(((((((((((((((((((((((((((((((((((((((((((('
  assert (find_brackets(string1) == False) and (find_brackets(string2) == False)
  
def test_no_brackets():
  string = 'hello world'
  assert find_brackets(string) == True
  
def test_mismatched_brackets():
  string = '(((}}}'
  assert find_brackets(string) == False