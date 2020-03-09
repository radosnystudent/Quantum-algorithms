import numpy as np
from math import sqrt, sin, cos

""""
np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) # X
np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex) # Y
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex) # Z
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,1)]], dtype=complex) # S
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,-1)]], dtype=complex) # St
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,1)*np.pi/4)]], dtype=complex) # T
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,-1)*np.pi/4)]], dtype=complex) # Tt
np.matrix([[complex(0.5,0.5), complex(0.5,-0.5)], [complex(0.5,-0.5), complex(0.5,0.5)]], dtype=complex) # M
np.matrix([[complex(1/sqrt(2),0), complex(1/sqrt(2),0)], [complex(1/sqrt(2),0), complex(-1/sqrt(2),0)]], dtype=complex) # H
def Rx(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) 

def Ry(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex)

def Rz(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex)
"""

class Qubit:

    def __init__(self, alfa : complex, beta : complex):
        self.alfa = alfa
        self.beta = beta

    def X_gate(self):
        result = np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) #np.array([[self.alfa, self.beta]], dtype=complex).transpose()
        self.alfa = result.item(0)
        self.beta = result.item(1)
        print(f'{self.alfa} {self.beta}')

    def S_gate(self):
        result = np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,1)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]])
        self.alfa = result.item(0)
        self.beta = result.item(1)
        print(f'{self.alfa} {self.beta}')

    def T_gate(self):
        result = np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,1)*np.pi/4)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]])
        self.alfa = result.item(0)
        self.beta = result.item(1)
        print(f'{self.alfa} {self.beta}')

    def Rx_gate(self, fi : any):
        def Rx(fi : any):
            return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex)

        result = Rx(fi) * np.matrix([[self.alfa], [self.beta]])
        self.alfa = result.item(0)
        self.beta = result.item(1)
        print(f'{self.alfa} {self.beta}')

if __name__ == '__main__':
    q = Qubit(complex(5,2), complex(3,0))
    q.Rx_gate(np.pi)