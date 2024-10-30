# 9. Use um loop for para imprimir cada chave e valor do dicionário.

# Determinação do dicionário:
fav_dict={'livro': 'The Brotherband Chronicles',
          'música': 'Cabin In The Trees - Trung Kien Nguyen',
          'árvore': 'Oak',
          'organismo': 'cachorro'}

# Uso do loop "for" para para imprimir cada chave e valor do dicionário:
for favoritos in fav_dict: # determinando as chaves do dicionário como "favoritos" 
    coisas=fav_dict[favoritos] # determinando os valores das chaves "favoritos" como "coisas"
    print(favoritos,":",coisas) # obtendo cada chave e seu respectivo valor do dicionário "fav_dict"
# Retorno:
# livro : The Brotherband Chronicles
# música : Cabin In The Trees - Trung Kien Nguyen
# árvore : Oak
# organismo : cachorro