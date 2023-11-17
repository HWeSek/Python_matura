with open('./sygnaly.txt') as file:
    words = file.readlines()
    file.close()
the_biggest_number = 0
for word in words:
    word_set = set(word.strip())
    if len(word_set) > the_biggest_number:
        the_biggest_number=len(word_set)
        the_biggest_word = word.strip()
output = the_biggest_word + ' ' + str(the_biggest_number)

with open('./wynik.txt','a') as outfile:
    outfile.write(output+'\n')
    outfile.close()