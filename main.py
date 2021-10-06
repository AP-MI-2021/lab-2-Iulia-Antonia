def rest_modulo16(x: int):
    """
    Calculeaza restul modulo 16
    :param x: un numar int de cel mult 4 cifre binare
    :return: restul corespunzator

    """
    p2 = 1  # puterea lui 2 corespunzatoare pozitiei
    nr = 0
    while x:
        nr = (x % 10) * p2 + nr
        p2 = p2 * 2
        x = x // 10
    return nr


def get_base_16_from_2(n):
    """
    Transforma un numar n scris in baza 2, in baza 16.
    :param n: numarul in baza 2 pe care il avem de convertit
    :return: nrb16 - numarul convertit in baza 16
    """
    nrb16 = ""
    m = int(n)
    while m:
        x = m % 10000
        nr = rest_modulo16(x)
        if nr == 10:
            cif = 'A'
        elif nr == 11:
            cif = 'B'
        elif nr == 12:
            cif = 'C'
        elif nr == 13:
            cif = 'D'
        elif nr == 14:
            cif = 'E'
        elif nr == 15:
            cif = 'F'
        else:
            cif = str(nr)
        nrb16 = cif + nrb16
        m = m // 10000
    return nrb16


def test_get_base_16_from_2():
    assert get_base_16_from_2(10) == '2'
    assert get_base_16_from_2(10101010) == 'AA'
    assert get_base_16_from_2(11111) == '1F'
    assert get_base_16_from_2(100111) == '27'
    assert get_base_16_from_2(100011111) == '11F'
    assert get_base_16_from_2(111100111100) == 'F3C'
    assert get_base_16_from_2(10010011) == '93'
    assert get_base_16_from_2(110000110000) == 'C30'


def produs(n):
    """
    Calculeaza n!
    :return: rezultatul produsului
    """
    p = 1
    i = 1
    while i <= n:
        p = p * i
        i = i + 1
    return p


def get_n_choose_k(n: int, k: int):
    """
    Calculeaza combinari de n luate cate k
    - input : n numarul de elemente ale multimii ( numar natural )
              k un numar natural <=n
    - output : rezultatul aplicarii formulei de la combinari de n luate cate k
    """
    return produs(n) // (produs(k) * produs(n - k))


def test_get_n_choose_k():
    assert get_n_choose_k(2, 1) == 2
    assert get_n_choose_k(6, 3) == 20
    assert get_n_choose_k(10, 1) == 10
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(7, 4) == 35
    assert get_n_choose_k(9, 7) == 36
    assert get_n_choose_k(20, 0) == 1
    assert get_n_choose_k(15, 10) == 3003


def get_leap_years(start: int, end: int):
    """
    Afisarea tuturor anilor bisecti  dintre doi ani dati de la tastatura (inclusiv anii dati)
    :param start: primul an (trebuie sa fie mi mic decat cel de-al doilea)
    :param end: al doilea an
    :return: lista anilor bisecti
    """
    leap_years_lst = []
    i = start
    while i <= end:
        if i % 4 == 0:
            leap_years_lst.append(i)
        i = i + 1
    return leap_years_lst


def test_get_leap_years():
    assert get_leap_years(2000, 2002) == [2000]
    assert get_leap_years(2000, 2006) == [2000, 2004]
    assert get_leap_years(1009, 1020) == [1012, 1016, 1020]
    assert get_leap_years(2002, 2021) == [2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(503, 533) == [504, 508, 512, 516, 520, 524, 528, 532]
    assert get_leap_years(1, 32) == [4, 8, 12, 16, 20, 24, 28, 32]


def main():
    while True:
        print('1.Conversia unui numar n din baza 2 in baza 16')
        print('2.Combinari de n luate cate k')
        print('3.Afisarea tuturor anilor bisecti dintre doi ani dati')
        print('4.Exit')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            n = input('Dati numarul in baza 2: ')
            print(f'Numarul {n} din baza 2, convertit in baza 16 este ', get_base_16_from_2(n))
        elif optiune == '2':
            n = int(input('Dati numarul n: '))
            k = int(input('Dati numarul k: '))
            print(get_n_choose_k(n, k))
        elif optiune == '3':
            start = int(input('Dati anul de start: '))
            end = int(input('Dati anul de end: '))
            print(get_leap_years(start, end))
        elif optiune == '4':
            break
        else:
            print('optiune invalida')


test_get_n_choose_k()
test_get_base_16_from_2()
test_get_leap_years()
main()
