def anagramIter(slowo1, slowo2):
    litery = {}
    if len(slowo1) != len(slowo2):
        print("Slowa nie są anagramami")
        return False
    elif slowo1 == slowo2:
        print("Slowa podane nie są różne")
        return False
    else:
        for litera in slowo1:
            litery[litera] = 0
        for litera in slowo2:
            litery[litera] = 0
        for litera in slowo1:
            litery[litera] +=1
        for litera in slowo2:
            litery[litera] +=1

        for ilosc in litery.values():
            if ilosc%2 == 0:
                wynik = True
            else:
                wynik = False
                break
        if wynik:
            print('Slowa sa anagramami')
            return True
        else:
            print("Slowa nie są anagramami")
            return False

anagramIter('yipyip', 'piypiy')
