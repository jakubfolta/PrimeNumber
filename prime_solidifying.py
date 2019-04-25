def check_if_prime(number):
    if number == 2:
        return True
    elif number < 2:
        return False
    for x in range(2, number - 1):
        if number % x == 0:
            return False
            break
    else:
        return True

print(check_if_prime(5))
