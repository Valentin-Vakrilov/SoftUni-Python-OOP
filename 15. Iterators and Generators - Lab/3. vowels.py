class vowels:
    VOWELS = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]

    def __init__(self, string):
        self.string = string
        self.vowels = [el for el in string if el in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels:
            raise StopIteration

        return self.vowels.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
