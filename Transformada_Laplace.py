"""
Instituto Federal de Santa Catarina
Aluno: Yuri Marques Barboza
Turma: Sinais e Sistemas 2022/2

Script: Transformada de Laplace
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import control

#------------------------------------------- Para plot 2D----------------------------------------#
print("Digite as funções do numerador e denominador de acordo com o exemplo:\nDigitando: 1,2,3\nVocê terá a função s^2+2*s+3")
numerador = input("Escreva a função do numerador: ") # Entrada do usuario para a função do numerador
lista_n = list(map(int,numerador.split(',')))        # Arruma o input do usuario em uma lista separando os digitos por ,
formN = np.poly1d(lista_n, variable = 's')           # Cria o polinomio da função utilizando os valores digitados pelo usuario

denominador = input("Escreva a função do denominador: ") # Entrada do usuario para a função do denomidador
lista_d = list(map(int,denominador.split(',')))          # Arruma o input do usuario em uma lista separando os digitos por ,
formD = np.poly1d(lista_d, variable = 's')               # Cria o polinomio da função utilizando os valores digitados pelo usuario

print("Função do numerador: \n",formN)
print("\nFunção do denomidador: \n",formD)

transferencia = control.tf(lista_n,lista_d) # Cria a função transferência
print('Função Transferência', transferencia)

polos = control.pole(transferencia) # Calcula os polos da função transferência
zeros = control.zero(transferencia) # Calcula os zeros da função transferência

print('polos=', polos)
print('zeros=', zeros)

plt.figure()
control.pzmap(transferencia,1,1,transferencia) # Plota o diagrama de polos e zeros
plt.show()


#------------------------------------------- Para plot 3D----------------------------------------#

fig = plt.figure()              # Cria figura para plot 3D
ax = plt.axes(projection='3d')  # Define o plot como 3D

x = np.arange(-10, 10, 0.4)     # Retorna os valores uniformemente espaçados dentro de um determinado intervalo
y = np.arange(-10, 10, 0.4)     # Retorna os valores uniformemente espaçados dentro de um determinado intervalo

X,Y=np.meshgrid(x,y);           # Cria uma grade retangular a partir de x,y representando a indexação cartesiana ou a indexação de matriz

s = X + 1j * Y                  # Define s como número complexo.

ZN = np.polyval(formN,s)        # Polyval resolve o polinômio em valores específicos, nesse caso s
ZD = np.polyval(formD,s)        # Polyval resolve o polinômio em valores específicos, nesse caso s
Z = abs(np.divide(ZN,ZD))       # Z é a divisão da função do numerador pelo denominador, retornando o valor absoluto da divisão

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False) # plot_surface é a função que gera um gráfico em 3D do tipo surface

ax.set_xlabel('Eixo Real de s') # Legenda para o eixo x
ax.set_ylabel('Eixo Imaginario de s') # Legenda para o eixo y
ax.set_zlabel('Magnitude') # Legenda para o eixo z

fig.colorbar(surf, shrink=0.5, aspect=5) # Adiciona uma barra de cores que mapeia os valores para as cores
 
plt.show() # Mostra o gráfico

#------------------------------------------- Para plot sigma = 0----------------------------------------#

x = np.arange(-10, 10, 0.1)     # Retorna os valores uniformemente espaçados dentro de um determinado intervalo
y = np.arange(-10, 10, 0.1)     # Retorna os valores uniformemente espaçados dentro de um determinado intervalo

X,Y=np.meshgrid(x,y) # Cria uma grade retangular a partir de x,y representando a indexação cartesiana ou a indexação de matriz

s = 1j * Y # Como sigma = 0 então é usado s apenas na região de número complexo.

ZN = np.polyval(formN,s)  # Polyval resolve o polinômio em valores específicos, nesse caso s
ZD = np.polyval(formD,s)  # Polyval resolve o polinômio em valores específicos, nesse caso s
Z = abs(np.divide(ZN,ZD)) # Z é a divisão da função do numerador pelo denominador, retornando o valor absoluto da divisão

plt.plot(Y,Z) # Plota o grafico 2D do campo imaginario e da magnitude

plt.xscale("log") # Seleciona a escala para o eixo x como logaritma
plt.yscale("log") # Seleciona a escala para o eixo y como logaritma

plt.xlabel('Parte Imaginaria') # Label do eixo x
plt.ylabel('Magnitude')        # Label do eixo y

plt.show() # Mostra o grafico
