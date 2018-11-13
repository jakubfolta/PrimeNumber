def is_prime(digit):
  if digit < 2:
    return False
  elif digit == 2:
    return True
  else:
    for number in range(2, digit):
      if digit % number == 0:
        return False
        break
    else:
        return True

print(is_prime(21))
