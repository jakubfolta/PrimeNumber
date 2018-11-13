def prime(number):
  if number == 2:
    return True
  if number < 2:
    return False
  for char in range(2, number - 1):
    if number % char == 0:
      return False
    return True

print(prime(6))
