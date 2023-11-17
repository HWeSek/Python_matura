with open('./sygnaly.txt') as file:
    words = file.readlines()
    file.close()
    output = []

for word in words:
    word = word.strip()
    is_valid=True
    for i in range(0,len(word)-1):
        if abs(ord(word[i]) - ord(word[i+1])) > 10:
            is_valid=False
    if is_valid:
        output.append(word)
print(len(output))

with open('./wynik.txt','a') as outfile:
    for word in output:
        outfile.write(word+'\n')
    outfile.close()