elements = [88, 75, 16, 65, 29, 89, 84, 11, 97, 3, 74, 12, 74, 6, 67, 12, 72, 93, 50, 69]

def quickSort(elements):
    if len(elements) <2:
        return elements
    pivot = elements[-1]
    smaller = []
    larger = []

    for i in range(0,len(elements)-1):
        if elements[i] <= pivot:
            smaller.append(elements[i])
        else:
            larger.append(elements[i])

    return quickSort(smaller) + [pivot] + quickSort(larger)

print(quickSort(elements))