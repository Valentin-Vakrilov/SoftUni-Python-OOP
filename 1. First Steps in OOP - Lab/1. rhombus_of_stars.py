def print_stars(n, line):
    print((" " * (n - line)) + "* " * line)


size = int(input())

for row in range(size+1):
    print_stars(size, row)

for row in range(size - 1, 0, -1):
    print_stars(size, row)
