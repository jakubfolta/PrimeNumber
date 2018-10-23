def prim(num):
  if num == 2:
    return True
  if num < 2:
    return False
  for dig in range(2, num -1):
    if num % dig == 0:
      return False
    else:
      return True

print (prim(7))
