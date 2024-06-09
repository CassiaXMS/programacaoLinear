'''-----EXERCÍCIO PRGRAMAÇÃO LINEAR COM MATRIZES--------------'''

'''EXERCÍCIO: 
       
        Função objetivo: Max L = 1900 x1 + 2100 x2
        
        Sujeito à:                  4x1+ 2x2 <= 20
                                    2x1+ 3x2 <= 10
                                    100x1 + 200x2 <=500
                
        Não negatividade:           x1 >= 0; x2 => 0
'''

from scipy.optimize import linprog


# Coeficientes da FUNÇÃO OBJETIVO (negativos para maximização)
coeficientes = [-1900, -2100]


# Matriz de coeficientes das restrições
matriz_restricoes = [
    [4, 2],
    [2, 3],
    [100, 200]
]

# Vetor de limites das restrições
vetor_restricoes = [20, 10, 500]

# Limites das variáveis (x1 >= 0, x2 >= 0)
x_bounds = (0, None)
bounds = [x_bounds, x_bounds]

# Resolução do problema
resultado = linprog(coeficientes, A_ub=matriz_restricoes, b_ub=vetor_restricoes, bounds=bounds, method='highs')

# Exibição dos resultados
print("\n SOLUÇÃO ÓTIMA: \n")
print(" Qtd. do P1 a ser produzido: ", resultado.x[0])
print(" Qtd. do P2 a ser produzido: ", resultado.x[1])
print(" Lucro Total: ", -resultado.fun)  # Negar o valor para obter o lucro máximo
