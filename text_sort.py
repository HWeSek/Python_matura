words = ['apple', 'banana','watermelon', 'pineapple', 'pear']

# sortedWords = sorted(words)
# print(sortedWords)

def lexicographicBubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
lexicographicBubbleSort(words)
print(words)