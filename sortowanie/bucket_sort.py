import math
elementy = [88, 75, 16, 65, 29, 89, 84, 11, 97, 3, 74, 12, 74, 6, 67, 12, 72, 93, 50, 69]
# el 0 - od 0 do 9
#el 1 - od 10-19
#el 2 - od 20-29
def bucketSort(elements):
    sorted=[]
    maximum = max(elements)
    buckets = [ [] for i in range(math.floor(maximum/10)+1)]
    for element in elements:
        buckets[math.floor(element/10)].append(element)
    for bucket in buckets:
        bucket.sort()
        for element in bucket:
            sorted.append(element)
    return sorted

print(bucketSort(elementy))