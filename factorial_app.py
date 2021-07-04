# 1! = 1
# 2! = 1*2
# 3! = 1*2*3

def factorial(n):
    """

    :param n: faktoriyeli bulunacak sayi
    :return: sonuc
    """
    result = 1
    for k in range(2, n + 1):
        result *= k

    return result


print(factorial(3))
