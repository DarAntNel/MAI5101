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

    if number == 1 or number == 2 or len(number_sequence) == number:
        return number_sequence[number-1]

    new_number = number_sequence[last_number] + number_sequence[last_number - 1]
    number_sequence.append(new_number)

    return fibonacci(number, number_sequence)


def binary_search(arr, target, array_start, array_end):
    if array_end >= array_start:

        array_middle = array_start + (array_end - array_start) // 2

        if arr[array_middle] == target:
            return array_middle
        elif arr[array_middle] > target:
            return binary_search(arr, target, array_start, array_middle - 1)
        else:
            return binary_search(arr, target, array_middle + 1, array_end)

    else:
        return -1


def  merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])



