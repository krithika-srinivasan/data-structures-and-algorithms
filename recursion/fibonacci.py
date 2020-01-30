def fibonacci(n):
    if n <= 1:
        return(n, 0)
    a, b = fibonacci(n - 1)
    return (a+b, a)

num = int(input('Number for fibonacci sum '))
print(fibonacci(num))