# 11. Escreva um script para encontrar a interseção, diferença, união e diferença simétrica entre esses dois conjuntos.

# Comjuntos fornecidos:
SetA = {3,14,15,9,26,5,35,9}
SetB = {60,22,14,0,9}

# Operações requeridas:
print("interseção:", SetA&SetB) # Uso do "&" para a obtenção dos elementos ao mesmo tempo em ambos os conjuntos
print("diferença SetA SetB:", SetA-SetB) # Uso do "-" para obtenção dos elementos em "SetA" mas não em "SetB"
print("diferença SetB SetA:", SetB-SetA) # Uso do "-" para obtenção dos elementos em "SetB" mas não em "SetA"
print("união:", SetA|SetB) # Uso do "|" para obtenção de todos os elementos em um dos conjuntos ou em ambos
print("diferênça simétrica:", SetA^SetB) # Uso do "^" para a obtenção dos elementos em "SetA" ou "SetB", mas não em ambos
# Retorno:
# interseção: {9, 14}
# diferença SetA SetB: {3, 35, 5, 15, 26}
# diferença SetB SetA: {0, 60, 22}
# união: {0, 35, 3, 5, 9, 14, 15, 22, 26, 60}
# diferênça simétrica: {0, 3, 5, 15, 22, 26, 35, 60}