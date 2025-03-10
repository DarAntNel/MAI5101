def factorial(number):
    if number == 1:
        return number
    elif number < 1:
        return "undefined"
    return number * factorial(number-1)

