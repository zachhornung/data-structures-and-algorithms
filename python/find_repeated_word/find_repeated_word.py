

def find_repeated_words(string):
  words = {}
  first_match = ''
  word = ''
  for char in string:
    if word.lower() in words:
      words[word] += 1
      return word
    if char == ' ':
      words[word.lower()] = 1
      word = ''
      continue
    if char.isalpha():
      word += char
  
  return first_match