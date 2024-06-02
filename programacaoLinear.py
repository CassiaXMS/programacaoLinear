
'''''-----SOLUÇÃO NÃO UTILIZANDO MATRIZ,BIBILIOTECA PULP--------------''''

'''import pulp

# Criação do problema
problema = pulp.LpProblem("Maximizar_Lucro", pulp.LpMaximize)

# Variáveis de decisão
x1 = pulp.LpVariable('P1', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('P2', lowBound=0, cat='Continuous')

# Função objetivo
problema += 1900 * x1 + 2100 * x2, "Lucro_Total"

# Restrições
problema += 4 * x1 + 2 * x2 <= 20, "Forja"
problema += 2 * x1 + 3 * x2 <= 10, "Polimento"
problema += 100 * x1 + 200 * x2 <= 500, "Materia_Prima"

# Resolução do problema
problema.solve()

# Exibição dos resultados
print("Status:", pulp.LpStatus[problema.status])
print("P1 (quantidade de produto P1 a ser produzido):", pulp.value(x1))
print("P2 (quantidade de produto P2 a ser produzido):", pulp.value(x2))
print("Lucro Total:", pulp.value(problema.objective))'''

'''''-----SOLUÇÃO UTILIZANDO MATRIZ BIBILIOTECA SCIPY--------------''''

from scipy.optimize import linprog

# Coeficientes da função objetivo (negativos para maximização)
c = [-1900, -2100]

# Matriz de coeficientes das restrições
A = [
    [4, 2],
    [2, 3],
    [100, 200]
]

# Vetor de limites das restrições
b = [20, 10, 500]

# Limites das variáveis (x1 >= 0, x2 >= 0)
x_bounds = (0, None)
bounds = [x_bounds, x_bounds]

# Resolução do problema
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Exibição dos resultados
print("Status:", result.message)
print("P1 (quantidade de produto P1 a ser produzido):", result.x[0])
print("P2 (quantidade de produto P2 a ser produzido):", result.x[1])
print("Lucro Total:", -result.fun)  # Negar o valor para obter o lucro máximo
