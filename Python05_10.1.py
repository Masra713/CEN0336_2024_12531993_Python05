# 10. Crie um conjunto usando as duas sintaxes diferentes para criar um conjunto, myset = set() e myset2 = {}. Qual é a diferença? Importa como você cria o conjunto?

# Criação dos dois conjuntos a partir das duas sinteses diferentes:
mySet = set("ATGTGGG") # No caso, o conjunto "mySet" criado por "set()" considera cada letra da chave "ATGTGGG" individualmente
mySet2 = {"ATGCCT"} # Aqui o conjunto "mySet2" criado por chaves "{}" considera a chave "ATGCCT" como um único elemento

# Para exemplificar, a união dos dois conjuntos:
print(mySet|mySet2)
# Retorno (os elementos podem vir em outra ordem):
# {'T', 'A', 'G', 'ATGCCT'}

# Na resposta fornecida, temos como elementos provenientes do conjunto "mySet" os elementos "T", "A" e "G". Podemos ver que suas duplicatas foram removidas
# Temos também o elemento "ATGCCT", proveniente do conjunto "mySet2", que apesar de ser formado pelos elementos do conjunto "mySet", aparece por ser considerado um único elemento 