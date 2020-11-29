from math import pi, pow


def pole_prostokata(*a):
    return a[0] * a[1]


def pole_kwadratu(*a):
    return pow(a[0], 2)


def pole_trapezu(*a):
    return (a[0] + a[1]) * a[2] / 2


def pole_kola(*r: float):
    if r[0] > 0:
        return round(pi * pow(r[0], 2), 2)
    else:
        return "Blad"


def kontynuacja(isTrue):
    kontynuowac = input("Czy kontynuwac (y/n):")
    if kontynuowac == 'y':
        isTrue = True
    else:
        isTrue = False
    return isTrue


def input_data(a):
    zmienna = float(input(a))
    if zmienna < 0:
        print("Zmiennna poza zakresu dozwolonych liczb")
    else:
        return zmienna


def oblicz_pola2():
    try:
        metody = {'kwadrat': pole_kwadratu, 'prostokat': pole_prostokata, 'trapez': pole_trapezu, 'kolo': pole_kola}
        isTrue = True
        while (isTrue == True):
            wybor = input('Podaj wybor (kwadrat, prostokat, trapez, kolo): ')
            if (wybor == 'kwadrat'):
                print(metody.get(wybor)(input_data("Podaj a: ")))
                isTrue = kontynuacja(isTrue)
            elif (wybor == 'prostokat'):
                print(metody.get(wybor)(input_data("Podaj a: "), input_data("Podaj b: ")))
                isTrue = kontynuacja(isTrue)
            elif (wybor == 'trapez'):
                print(metody.get(wybor)(input_data("Podaj a: "), input_data("Podaj b: "), input_data("Podaj h: ")))
                isTrue = kontynuacja(isTrue)
            elif (wybor == 'kolo'):
                print(metody.get(wybor)(input_data("Podaj r: ")))
                isTrue = kontynuacja(isTrue)
    except:
        print("Dana musi byc z zakresu")


def oblicz_pole():
    isTrue = True
    while (isTrue == True):
        print("1. Pole kwardatu")
        print("2. Pole prostokata")
        print("3. Pole trapezu")
        print("4. Pole koła")
        typ_zadania = input("Podaj typ zadania (1-4): ")

        if int(typ_zadania) == 1:
            a = input("Podaj wielkosc a: ")
            print(pole_kwadratu(float(a)))
            isTrue = kontynuacja(isTrue)
        elif int(typ_zadania) == 2:
            a = input("Podaj wielkosc a")
            b = input("Podaj wielkosc b")
            print(pole_prostokata(float(a), float(b)))
            isTrue = kontynuacja(isTrue)
        elif int(typ_zadania) == 3:
            a = input("Podaj wielkosc a")
            b = input("Podaj wielkosc b")
            h = input("Podaj wielkosc h")
            print(pole_trapezu(float(a), float(b), float(h)))
            isTrue = kontynuacja(isTrue)
        elif int(typ_zadania) == 4:
            r = input("Podaj promien: ")
            print(round(pi * pow(r, 2), 2))
            isTrue = kontynuacja(isTrue)


def card_hide(credit_card: str):
    return "************" + credit_card[12:16]


def unique_sort(table):
    table = list(dict.fromkeys(table))
    table.sort()
    return table


def abcmath(a, b, c):
    if (a * b) % c == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    oblicz_pola2()
