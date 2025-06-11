
# =========== Stack Memory ==================

def add(a, b):
    result = a + b  # 'result' is a local variable stored on the stack
    return result

def main():
    num1 = 100
    num2 = 200
    total = add(num1, num2)
    print(f"Sum:{total}\n")

if __name__ == '__main__':
    print("Stack Memory")
    main()

# ============ Heap Memory ======================

class Person:
    def __init__(self, name):
        # 'name' is stored in heap memory
        self.name = name

# Object allocated in heap
print("Heap Memory")
p1 = Person("Alice")
p2 = Person("Bob")
print(p1.name, p2.name)
