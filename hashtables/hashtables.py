# implementation of hash function wth out collision handling or any other implementation
# Taken an array of size 100

class HashTable:
    def __init__(self):
        self.Max = 100
        self.array = [None for i in range(self.Max)]

    def get_hashfunction(self, key):
        counter = 0
        for char in key:
            counter += ord(char)
        return counter % self.Max

    def add_element(self, key, value):
        counter = self.get_hashfunction(key)
        self.array[counter] = value

    def get_fromkey(self, key):
        counter = self.get_hashfunction(key)
        return self.array[counter]


t = HashTable()
t.add_element('varshith', '250')
t.add_element('Ramesh', '100')
t.add_element('mark', '256')
print(t.array)
print(t.get_fromkey('varshith'))
print(t.get_fromkey('Ramesh'))
print(t.get_fromkey('mark'))
