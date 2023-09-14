def read_next(*args):
    for item in args:
        for element in item:
            yield element


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
