# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:21:39 2022

@author: Grupo 1
"""

import matplotlib.pyplot as plt
import numpy as np
import testes

#------------------------------------------------------------------------------

def main():
    
    teste = input('Realizar testes (s/n) ? ') 
    
    if teste in ['s', 'S']: testes.main()

    ordem = np.loadtxt('resultados_real.csv', delimiter = ',',
                       skiprows=1, usecols=3)
    ordem = ordem[0]
    n_testes = np.loadtxt('resultados_real.csv', delimiter = ',',
                          skiprows=1, usecols=2)
    n_testes = n_testes[0]

    x = [i*10**(ordem-6) for i in range(2,9)]
        
    y1 = np.loadtxt('resultados_real.csv', delimiter=',', skiprows=1,
                    usecols=1)
    y2 = np.loadtxt('resultados_virtual.csv', delimiter=',', skiprows=1,
                    usecols=1)
    
    linha(x, y1, y2, n_testes)
    barra(x, y1, y2)

    return None

#------------------------------------------------------------------------------

def linha(x, y1, y2, n_testes):
    
    plt.plot(x, y1, label = 'Host', linestyle='dashed', marker='o')
    plt.plot(x, y2, label = 'Guest', linestyle='dashed', marker='o')
    
    plt.xlabel('n (milhões)')
    plt.ylabel('tempo (s)')
    plt.title('Tempo de execução médio (%d teste(s))' %n_testes)
    plt.legend()
    plt.show()
    
    return None

#------------------------------------------------------------------------------

def barra(x, y1, y2):
    
    plt.bar(x, sub(y2,y1))
    
    plt.xlabel('n (milhões)')
    plt.ylabel('tempo (s)')
    plt.title('Diferença de tempo em segundos')
    plt.show()
    
    return None

#------------------------------------------------------------------------------

def sub(a,b):
    subtracao = []
    for i in range(len(a)):
        subtracao.append(a[i]-b[i])
    return subtracao

#------------------------------------------------------------------------------   

if __name__ == '__main__':
    main()