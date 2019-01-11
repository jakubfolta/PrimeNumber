def prime(number):
  if number == 2:
    return True
  if number < 2:
    return False
  for digit in range(2, number - 1):
    if number % digit == 0:
      return False
      break
  else:
    return True

print(prime(19))


def checkIfNumberIsPrime(number):
  if number == 2:
    return True
  if number < 2:
    return False
  for x in range(2, number - 1):
    if number % x == 0:
      print(str(number) + ' is not a prime number.')
      return False
      break
  else:
      print(str(number) + ' is a prime number!')
      return True
        
print(checkIfNumberIsPrime(12))
