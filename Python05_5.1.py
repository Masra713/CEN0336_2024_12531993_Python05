# 5. Adicione o seu "organismo" favorito ao dicionário. Faça com que "organismo" seja o novo valor da chave fav_thing.

# Determinação do dicionário para a busca:
fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

# Adicionando ao dicionário (fav_dict) a nova chave (organismo) e seu valor (cavalo):
fav_dict["organismo"] = "cavalo"

# Confirmando a adição:
print(fav_dict)
# Retorno:
# {'livro': "Ranger's Apprentice", 'música': 'Cabin In The Trees - Trung Kien Nguyen', 'árvore': 'Oak', 'organismo': 'cavalo'}          

# Tornando "organismo" o novo valor da chave "fav_thing":
fav_thing = "organismo"

# Obtendo o valor da chave "organismo" através da chave "fav_thing":
print(fav_dict[fav_thing])
# Retorno:
# cavalo