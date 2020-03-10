import numpy as np
from gates import gate_list

class Qubit:

    def __init__(self, alfa : complex, beta : complex):
        self.alfa = alfa
        self.beta = beta


if __name__ == '__main__':
    q = Qubit(complex(5,2), complex(3,0))
    #print(gate_list[0](complex(1,0), complex(0,0)))

"""
np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) # X
np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex) # Y
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) # Z
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,1)]], dtype=complex) # S
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,-1)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) # St
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,1)*np.pi/4)]], dtype=complex) # T
np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,-1)*np.pi/4)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) # Tt
np.matrix([[complex(0.5,0.5), complex(0.5,-0.5)], [complex(0.5,-0.5), complex(0.5,0.5)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) # M
np.matrix([[complex(1/sqrt(2),0), complex(1/sqrt(2),0)], [complex(1/sqrt(2),0), complex(-1/sqrt(2),0)]], dtype=complex) * np.matrix([[self.alfa], [self.beta]]) # H
def Rx(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) 

def Ry(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex)

def Rz(fi : any) -> np.matrix:
    return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex)
"""