def checkIfPrime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  for x in range (2, num -1):
    if num % x == 0:
      return False
  return True

print (checkIfPrime(21))
