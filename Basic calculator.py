def addition(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def subtraction(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiplication(*numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


def division(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result


def factorial(n):
    if n == 1 or n == 0:
        return f"Please enter a number other than 1 or 0. \n Your choice is: {n}!"
    else:
        result = 1
    for number in range(n, 1, -1):
        result *= number
    return result
