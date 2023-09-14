def get_primes(integers):
    for number in integers:
        if number <= 1:
            continue

        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
