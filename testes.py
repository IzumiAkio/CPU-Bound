# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 19:39:30 2022

@author: Grupo 1
"""

import time
import pandas as pd
import numpy as np

#------------------------------------------------------------------------------

def main():
    
    ordem = int(input('Ordem de grandeza [6, 7, 8]: '))
    
    if ordem not in [6,7,8]:
        print('Digite um valor dentro do intervalo.')
        return None
    
    dominio = [i*(10**ordem) for i in range(2,9)]
    imagem = []
    real_virtual = input('Máquina real ou virtual (r/v) ? ')
    
    if real_virtual not in ['r','R','v','V']: return None
    
    n_testes = int(input('Número de testes por ponto: '))
    print('\nIniciando...')
    
    inicio = time.time()
    
    for i in range(len(dominio)):
        print('%dº ponto:' %(i+1))
        ponto = exp(dominio[i], n_testes)
        imagem.append(ponto)
        print()
    
    resultados = pd.DataFrame({'n':dominio, 'Tempo':imagem,
                               'no_testes': n_testes, 'ordem': ordem})
    
    if real_virtual in ['r','R']:
        resultados.to_csv('resultados_real.csv', index=False)
    else:
        resultados.to_csv('resultados_virtual.csv', index=False)
        
    fim = time.time()
    
    print('Tempo total: %.2fs' %(fim-inicio))
    print('Testes concluídos!')
    
    return None

#------------------------------------------------------------------------------

def sub(n):
    inicio = time.time()
    for i in range(n):
        n -= 1
    fim = time.time()
    return (fim - inicio)

#------------------------------------------------------------------------------

def exp(x,n):
    soma = 0
    for i in range(n):
        soma += sub(x)
        print('    %dº teste concluído' %(i+1))
    media = soma/n
    media = np.around(media, decimals=2)
    return media

#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()