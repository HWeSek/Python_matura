with open('./sygnaly.txt') as file:
    words = file.readlines()
    file.close()
i = 1
output = ''
for word in words:
    if i % 40 == 0:
        output+=word[9]
    i+=1

with open('./wynik.txt','w') as outfile:
    outfile.write(output+'\n')
    outfile.close()