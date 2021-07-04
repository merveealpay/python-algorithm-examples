# 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    fibonacci_list = [1, 1]

    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])

    return fibonacci_list


print(fibonacci(5))
