from LAB2.lab2 import factorial
from LAB2.lab2 import fibonacci
from LAB2.lab2 import binary_search
from LAB2.lab2 import merge_sort







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = factorial(80)
    print(x)

    b = fibonacci(2)
    print(b)

    arr = [2, 3, 4, 10, 40]
    target = 10
    print(binary_search(arr, target, 0, len(arr) - 1))

    arr = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# 1. What is the time complexity of your Fibonacci function?
# 2. How does recursion compare to iteration in these cases?
