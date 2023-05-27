def first_two(str):
  if len(str) == 0:
    return ""
  elif len(str) < 2:
    return str
  return str[0:2]
    
