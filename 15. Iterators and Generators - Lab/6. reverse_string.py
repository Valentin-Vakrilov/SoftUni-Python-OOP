def reverse_text(string):
    reversed_string = reversed(string)

    for ch in reversed_string:
        yield ch


for char in reverse_text("step"):
    print(char, end='')
