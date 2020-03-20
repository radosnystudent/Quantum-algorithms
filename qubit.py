from gates import gate_list
from math import sqrt
from random import randint

class Qubit:

    def __init__(self, alfa : complex, beta : complex):
        self.__alfa = alfa
        self.__beta = beta
        self.__gates = gate_list

    def useGate(self, choice : str, fi = None):
        if choice.startswith('R'):
            result = self.__gates[choice](self.__alfa, self.__beta, fi)
        else:
            result = self.__gates[choice](self.__alfa, self.__beta)
        self.__alfa = result.item(0)
        self.__beta = result.item(1)
        
    def measure(self):
        moduleAlfa = abs(self.__alfa)**2
        moduleBeta = abs(self.__beta)**2
        p_alfa = round(moduleAlfa/(moduleAlfa+moduleBeta),2) * 100
        if randint(0, 100) <= p_alfa:
            self.__alfa /= abs(self.__alfa)
            self.__beta = 0
        else:
            self.__beta /= abs(self.__beta)
            self.__alfa = 0

    def __str__(self):
        return f'Aktualny stan qubita\n{complex(round(self.__alfa.real,2), round(self.__alfa.imag,2))}|0> + {complex(round(self.__beta.real,2),round(self.__beta.imag,2))}|1>'


def chooseGate():
    while True:
        choice = input('Wybierz bramke wpisujac: X, Y, Z, S, St, T, Tt, H, M, Rx, Ry lub Rz\n> ')
        if len(choice) == 1:
            choice = choice.upper()
        elif len(choice) == 2:
            choice = choice[0].upper() + choice[1].lower()
        if choice in [key for key in gate_list.keys()]:
            return choice
        else:
            print('Nie ma takiej bramki.')
    return None

def main():
    print('Podaj dwie liczby zespolone:')
    complexNumbers = list()

    for i in range(2):
        print(f'{i + 1} liczba:')
        real = float(input('Real:\n> '))
        imag = float(input('Imaginary:\n> '))
        complexNumbers.append(complex(real, imag))
    
    Q = Qubit(complexNumbers[0], complexNumbers[1])

    choice = -1

    while True:
        while choice not in range(4):
            choice = int(input('1. Wyswietl stan\n2. Pomiar\n3. Bramka\n0. Exit\n> '))
        if choice == 1:
            print(Q)
        elif choice == 2:
            Q.measure()
        elif choice == 3:
            gate = chooseGate()
            if gate:
                if gate.startswith('R'):
                    Q.useGate(gate, float(input('Podaj wartosc kata Fi:\n> ')))
                else:
                    Q.useGate(gate)
        if choice == 0:
            break
        choice = -1

if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
