def in1to10(n, outside_mode):
  if outside_mode:
    if 1 <= n <= 10:
      return True
    else:
      return False
  else:
    return n in in range(1, 11)