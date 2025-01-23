def fibonacci(num):
    previous = 0
    current = 1
    found = False
    while current <= num:
        aux = previous
        previous = current
        current += aux
        if current == num:
            found = True
    return found

print(fibonacci(34))
print(fibonacci(29))

print(fibonacci(21))

print(fibonacci(13))