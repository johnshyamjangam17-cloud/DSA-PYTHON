
SIZE = 10

# Separate Chaining
class SeparateChaining:
    def __init__(self):
        self.table = [[] for i in range(SIZE)]

    def insert(self, key):
        index = key % SIZE
        self.table[index].append(key)

    def display(self):
        print("Separate Chaining:")
        for i in range(SIZE):
            print(i, ":", self.table[i])


# Linear Probing
class LinearProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            new_index = (index + i) % SIZE

            if self.table[new_index] is None:
                self.table[new_index] = key
                return

        print("Hash Table is Full")

    def display(self):
        print("Linear Probing:")
        print(self.table)


# Quadratic Probing
class QuadraticProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            new_index = (index + i * i) % SIZE

            if self.table[new_index] is None:
                self.table[new_index] = key
                return

        print("Hash Table is Full")

    def display(self):
        print("Quadratic Probing:")
        print(self.table)


# Main Program
values = [23, 43, 13, 27, 37]

sc = SeparateChaining()
lp = LinearProbing()
qp = QuadraticProbing()

for key in values:
    sc.insert(key)
    lp.insert(key)
    qp.insert(key)

sc.display()
lp.display()
qp.display()
