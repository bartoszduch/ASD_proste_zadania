#Część 1

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, x):
        new_node = Node(x)
        self.children.append(new_node)

    def print_tree(self, prefix=''):
        print(f"{prefix}{self.value}")
        if self.children:
            prefix += '-' * (len(prefix) + 1)
            for child in self.children[:-1]:
                child.print_tree(prefix + '-')
            self.children[-1].print_tree(prefix)


root = Node(1.5)
root.insert(1.3)
root.insert(-1.6)

child = Node(3.5)
child.insert(3.7)
root.insert(child)

child = Node(4.5)
child.insert(4.0)
child.insert(-4.99)
root.insert(child)

child = Node(7.5)
child.insert(7.3)

grandchild = Node(7.7)
grandchild.insert(7.6)
child.insert(grandchild)

child.insert(-7.8)
child.insert(-7.9)
root.insert(child)

root.insert(9.5)
root.insert(9.3)

root.print_tree()

#Część 2,
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, x):
        if abs(self.value - x.value) <= 0.5:
            self.children.append(x)
        else:
            for child in self.children:
                child.insert(x)

    def minimum(self):
        if not self.children:
            return self.value
        else:
            min_value = self.value
            for child in self.children:
                min_value = min(min_value, child.minimum())
            return min_value

    def maximum(self):
        if not self.children:
            return self.value
        else:
            max_value = self.value
            for child in self.children:
                max_value = max(max_value, child.maximum())
            return max_value

    def search(self, x):
        if self.value == x.value:
            return True
        else:
            for child in self.children:
                if child.search(x):
                    return True
            return False

    def print_tree(self, prefix=''):
        print(f"{prefix}{self.value}")
        if self.children:
            prefix += '-' * (len(prefix) + 1)
            for child in self.children[:-1]:
                child.print_tree(prefix + '-')
            self.children[-1].print_tree(prefix)


root = Node(1.5)
root.insert(Node(1.3))
root.insert(Node(-1.6))

child = Node(3.5)
child.insert(Node(3.7))
root.insert(child)

child = Node(4.5)
child.insert(Node(4.0))
child.insert(Node(-4.99))
root.insert(child)

child = Node(7.5)
child.insert(Node(7.3))

grandchild = Node(7.7)
grandchild.insert(Node(7.6))
child.insert(grandchild)

child.insert(Node(-7.8))
child.insert(Node(-7.9))
root.insert(child)

root.insert(Node(9.5))
root.insert(Node(9.3))

root.print_tree()

x = Node(2.0)
root.insert(x)
print(f"Inserted {x.value}:")
root.print_tree()

print("Minimum:", root.minimum())
print("Maximum:", root.maximum())

y = Node(7.6)
print(f"Search {y.value}: {root.search(y)}")

z = Node(5.0)
print(f"Search {z.value}: {root.search(z)}")

#Część 3

import random
import time


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def insert(self, x):
        if abs(self.value - x.value) <= 0.5:
            self.children.append(x)
        else:
            for child in self.children:
                child.insert(x)

    def minimum(self):
        if not self.children:
            return self.value
        else:
            min_value = self.value
            for child in self.children:
                min_value = min(min_value, child.minimum())
            return min_value

    def maximum(self):
        if not self.children:
            return self.value
        else:
            max_value = self.value
            for child in self.children:
                max_value = max(max_value, child.maximum())
            return max_value

    def search(self, x):
        if self.value == x.value:
            return True
        else:
            for child in self.children:
                if child.search(x):
                    return True
            return False

    def print_tree(self, prefix=''):
        print(f"{prefix}{self.value}")
        if self.children:
            prefix += '-' * (len(prefix) + 1)
            for child in self.children[:-1]:
                child.print_tree(prefix + '-')
            self.children[-1].print_tree(prefix)


# Funkcja do generowania losowych danych
def generate_random_data(size):
    data = []
    for _ in range(size):
        value = random.uniform(0.5, float('inf'))
        data.append(Node(value))
    return data


# Funkcja do mierzenia czasu wykonania operacji
def measure_operation_time(structure_size):
    data = generate_random_data(structure_size)
    root = data[0]
    for node in data[1:]:
        root.insert(node)

    start_time = time.time()

    # Wykonanie operacji
    root.minimum()
    root.maximum()
    root.search(Node(random.uniform(0.5, float('inf'))))

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time


# Rozmiary struktury do przetestowania
structure_sizes = [25, 50, 100, 500, 1000]

# Mierzenie czasu wykonania operacji dla r�nych rozmiar�w struktury
for i in structure_sizes:
    execution_time = measure_operation_time(i)
    print(f"Structure Size: {i}, Execution Time: {execution_time} seconds")
