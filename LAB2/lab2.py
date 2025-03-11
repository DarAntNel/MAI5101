def factorial(number):
    if number == 1:
        return number
    elif number < 1:
        return "undefined"
    return number * factorial(number-1)


def fibonacci(number, number_sequence = [0,1]):
    last_number = len(number_sequence) - 1

    if number == 0:
        return 0
    if number == 1:
        return number_sequence[0]
    if number == 2:
        return number_sequence[1]

    if len(number_sequence) == number:
        return number_sequence[number-1]

    new_number = number_sequence[last_number] + number_sequence[last_number - 1]
    number_sequence.append(new_number)

    return fibonacci(number, number_sequence)


