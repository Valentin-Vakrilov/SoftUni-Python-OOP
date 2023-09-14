class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration

        self.counter += 1

        return self.count - self.counter


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
