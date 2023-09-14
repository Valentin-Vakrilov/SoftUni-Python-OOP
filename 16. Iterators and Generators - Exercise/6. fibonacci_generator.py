def fibonacci():
    first_number, second_number = 0, 1

    while True:
        yield first_number

        first_number, second_number = second_number, first_number + second_number


generator = fibonacci()
for i in range(1):
    print(next(generator))
