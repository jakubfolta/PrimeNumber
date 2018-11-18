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
