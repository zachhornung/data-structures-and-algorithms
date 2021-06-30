def left_join(dictionary1, dictionary2, **kwargs):
  if 'right_join' in kwargs:
    dictionary1, dictionary2 = dictionary2, dictionary1
  k2dict = {key:(True if key in dictionary2.keys() else False) for key in dictionary2.keys()}
  return [[key, dictionary1[key], dictionary2[key]] if k2dict[key] else [key, dictionary1[key], None] for key in dictionary1]