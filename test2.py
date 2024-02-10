class ArrayOperations:
    def shiftLeft(source, k):
        for i in range(k, len(source)):
            source[i - k] = source[i]
            source[i] = 0
        print(source)

    def rotateLeft(source, k):
        k = k % len(source)
        source[:] = source[k:] + source[:k]
        print(source)

    def remove(source, size, idx):
        if idx < 0 or idx >= size:
            print("Invalid index")
            return
        for i in range(idx, size - 1):
            source[i] = source[i + 1]
        source[size - 1] = 0
        print(source)

    def removeAll(source, size, element):
        i = 0
        while i < size:
            if source[i] == element:
                for j in range(i, size - 1):
                    source[j] = source[j + 1]
                source[size - 1] = 0
                size -= 1
            else:
                i += 1
        print(source)

# Example usage:

source1 = [10, 20, 30, 40, 50, 60]
ArrayOperations.shiftLeft(source1, 3)

source2 = [10, 20, 30, 40, 50, 60]
ArrayOperations.rotateLeft(source2, 3)

source3 = [10, 20, 30, 40, 50, 0, 0]
ArrayOperations.remove(source3, 5, 2)

source4 = [10, 2, 30, 2, 50, 2, 2, 0, 0]
ArrayOperations.removeAll(source4, 7, 2)
