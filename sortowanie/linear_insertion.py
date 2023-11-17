elements = [88, 75, 16, 65, 29, 89, 84, 11, 97, 3, 74, 12, 74, 6, 67, 12, 72, 93, 50, 69]

def insertionSort(elements):
    for i in range(1, len(elements)):
        number = elements[i]

        while i > 0 and elements[i-1] > number:
            elements[i] = elements[i-1]
            i -= 1
        elements[i] = number
    return elements

print(elements)
print(insertionSort(elements))