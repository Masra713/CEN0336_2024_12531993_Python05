# 8. Obtenha fav_thing da linha de comando e um novo valor para essa chave. Altere o valor com o valor inserido pelo usuário.

# Determinação do dicionário:
fav_dict = {"livro" : "Ranger's Apprentice",
            "música" : "Cabin In The Trees - Trung Kien Nguyen",
            "árvore" : "Oak",
            "organismo" : "cachorro"
            }

# Determinando como "fav_thing" o valor da chave "livro" (Ranger's Apprentice):
fav_thing=fav_dict["livro"]

# Obtendo o valor da chave "fav_thing":
print(fav_thing)
# Retorno:
# Ranger's Apprentice

# Alterando o valor da chave "livro" para "The Brotherband Chronicles":
fav_dict["livro"]="The Brotherband Chronicles"

# Obtendo o dicionário atualizado:
print(fav_dict)
# Retorno:
# {'livro': 'The Brotherband Chronicles', 'música': 'Cabin In The Trees - Trung Kien Nguyen', 'árvore': 'Oak', 'organismo': 'cachorro'}

# Atualizando o valor da chave "fav_thing":
fav_thing=fav_dict["livro"]
# *Sem repetir esse comando, o "print" a seguir iria retornar o valor anterior da chave "fav_thing": Ranger's Apprentice, apesar do valor ter sido alterado no dicionário

# Obtendo o valor da chave "livro" a partir da chave "fav_thing":
print(fav_thing)
# Retorno:
# The Brotherband Chronicles