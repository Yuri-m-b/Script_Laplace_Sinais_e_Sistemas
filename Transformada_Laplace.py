"""
Instituto Federal de Santa Catarina
Aluno: Yuri Marques Barboza
Turma: Sinais e Sistemas 2022/2

Script: Transformada de Laplace
"""

#https://docs.sympy.org/latest/modules/physics/control/control_plots.html
from sympy.abc import s
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import pole_zero_plot
from sympy.physics.control.control_plots import pole_zero_numerical_data
from sympy import sympify
import sympy as sym
from sympy import poly

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

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
#\/-----------------------------\/---------------------------------------\/
# Essa parte do codigo é apenas uma manipulação das variaveis para que possam ser usadas na função de transferência

# PARA FUNÇÃO DO NUMERADOR
list_n_temp = []      # Lista temporaria que vai armazenar os digitos dados pelo usuario ao numerador da função
list_n_temp2 = []     # Lista temporaria que vai armazenar os "s" criados para serem usados na função transferencia posteriormente
list_n_final = []     # Lista temporaria que vai armazenar a função/expressão final do numerador
list_n_estrela = []   # Lista temporaria que vai armazenar o caracter "*"
size_n = len(lista_n) # Variavel que será usada como parametro para os loops, tendo como o valor o tamanho da lista_n
i = len(lista_n)      # Variavel que será usada como parametro para os loops, tendo como o valor o tamanho da lista_n
    
while i>0:            # Nesse loop, é criado e armazenado dentro da lista_n_temp2 o caracter "s**"
    if i == 1:
        sz = 1
    else:
        sz = str(s**(i-1))
    list_n_temp2.append(sz)
    i = i - 1
    
while i<size_n:       # Nesse loop, é onde sera colocado as expressões armazenadas nas listas temporarias dentro da lista final"
    list_n_temp.append(lista_n[i])
    list_n_estrela.append('*')
    temp_n = str(list_n_temp[i]) + str(list_n_estrela[i]) + str(list_n_temp2[i])
    list_n_final.append(temp_n)
    i = i + 1

i = 0
num_str = ' '.join(map(str,list_n_final))      # Converte a lista em uma string
num_str2 = num_str.replace(' ', '+')           # Substitui todos os espaços em brancos pelo sinal +
num_final = sympify(num_str2)                  # Cria a forma de expressão para a função do numerador

# PARA FUNÇÃO DO DENOMINADOR
list_d_temp = []                  # Lista temporaria que vai armazenar os digitos dados pelo usuario ao denominador da função
list_d_temp2 = []                 # Lista temporaria que vai armazenar os "s" criados para serem usados na função transferencia posteriormente
list_d_final = []                 # Lista temporaria que vai armazenar a função/expressão final do denominador
list_d_estrela = []               # Lista temporaria que vai armazenar o caracter "*"
size_d = len(lista_d)             # Variavel que será usada como parametro para os loops, tendo como o valor o tamanho da lista_n
i = len(lista_d)                  # Variavel que será usada como parametro para os loops, tendo como o valor o tamanho da lista_n
    
while i>0:                        # Nesse loop, é criado e armazenado dentro da lista_n_temp2 o caracter "s**"
    if i == 1:
        sz2 = 1
    else:
        sz2 = str(s**(i-1))
    list_d_temp2.append(sz2)
    i = i - 1
    
while i<size_d:                  # Nesse loop, é onde sera colocado as expressões armazenadas nas listas temporarias dentro da lista final"
    list_d_temp.append(lista_d[i])
    list_d_estrela.append('*')
    temp_d = str(list_d_temp[i]) + str(list_d_estrela[i]) + str(list_d_temp2[i])
    list_d_final.append(temp_d)
    i = i + 1

i = 0
den_str = ' '.join(map(str,list_d_final))      # Converte a lista em uma string
den_str2 = den_str.replace(' ', '+')           # Substitui todos os espaços em brancos pelo sinal +
den_final = sympify(den_str2)                  # Cria a forma de expressão para a função do numerador
#/\-----------------------------/\---------------------------------------/\


tf1 = TransferFunction(num_final, den_final, s) # Função da biblioteca Sympy que calcula a função transferência
pole_zero_plot(tf1) # Função da biblioteca Sympy que gera o mapa de polos e zero da função transferência



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
