import numpy as np
from math import sqrt, sin, cos


def X_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex) * np.matrix([[alfa], [beta]])

def Y_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex) * np.matrix([[alfa], [beta]])
    
def Z_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex) * np.matrix([[alfa], [beta]]) 
    
def S_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,1)]], dtype=complex) * np.matrix([[alfa], [beta]])
    
def St_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(0,-1)]], dtype=complex) * np.matrix([[alfa], [beta]]) 
    
def M_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(0.5,0.5), complex(0.5,-0.5)], [complex(0.5,-0.5), complex(0.5,0.5)]], dtype=complex) * np.matrix([[alfa], [beta]]) 
    
def H_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1/sqrt(2),0), complex(1/sqrt(2),0)], [complex(1/sqrt(2),0), complex(-1/sqrt(2),0)]], dtype=complex) * np.matrix([[alfa], [beta]])

def T_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,1)*np.pi/4)]], dtype=complex) * np.matrix([[alfa], [beta]])
    
def Tt_gate(alfa : complex, beta : complex):
    return np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), np.exp(complex(0,-1)*np.pi/4)]], dtype=complex) * np.matrix([[alfa], [beta]]) 

def Rx_gate(alfa : complex, beta : complex, fi : float):
    def Rx(fi : float):
        return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(1,0)], [complex(1,0), complex(0,0)]], dtype=complex)

    return Rx(fi) * np.matrix([[alfa], [beta]])
    
def Ry_gate(alfa : complex, beta : complex, fi : float):
    def Ry(fi : float):
        return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(0,0), complex(0,-1)], [complex(0,1), complex(0,0)]], dtype=complex)

    return Ry(fi) * np.matrix([[alfa], [beta]])
    
def Rz_gate(alfa : complex, beta : complex, fi : float):
    def Rz(fi : float):
        return cos(fi/2) * np.matrix('1 0; 0 1') + complex(0,1) * sin(fi/2) * np.matrix([[complex(1,0), complex(0,0)], [complex(0,0), complex(-1,0)]], dtype=complex)
    
    return Rz(fi) * np.matrix([[alfa], [beta]])


gate_list = { 'X' : X_gate, 'Y' : Y_gate, 'Z' : Z_gate, 'S': S_gate, 'St' : St_gate, 'T' : T_gate, 
            'Tt' : Tt_gate, 'M' : M_gate, 'H' : H_gate, 'Rx' : Rx_gate, 'Ry' : Ry_gate, 'Rz' : Rz_gate}