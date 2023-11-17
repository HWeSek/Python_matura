liczba = input('Podaj liczbe do zamiany: ')

def MultiConversion(number, input_system, output_system):
    work_number=[]
    output_list=[]
    wynik=0
    i=0
    if input_system==2:
        for digit in number:
            if digit == '1' or digit == '0':
                work_number.append(digit)
            else:
                print('Tylko 1 i 0 w systemie dwójkowym!')
                break
    if input_system==10:
        while number != 0:
            rest = input(number) % output_system
            output_list.append(rest)
            number // output_system
        print(output_list)

    work_number.reverse()
    for digit in work_number:
        wynik = wynik + int(digit)*input_system**i
        i+=1

MultiConversion(liczba, 10, 2)