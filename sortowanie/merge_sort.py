elements = [88, 75, 16, 65, 29, 89, 84, 11, 97, 3, 74, 12, 74, 6, 67, 12, 72, 93, 50, 69]

def mergeSorting(elements):
    if len(elements) < 2:
        return elements
    i = j = k = 0
    middle = len(elements) // 2
    left, right = elements[:middle], elements[middle:]
    mergeSorting(left)
    mergeSorting(right)

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            elements[k] = left[i]
            i+=1
        else:
            elements[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        elements[k] = left[i]
        i+=1
        k+=1
    while j < len(right):
        elements[k] = right[j]
        j+=1
        k+=1
    return elements

print(mergeSorting(elements))