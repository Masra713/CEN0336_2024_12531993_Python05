# 6. Obtenha um valor da linha de comando para fav_thing e print o valor desse item do dicionário. Talvez você queira imprimir todas as chaves para o usuário, para que eles saibam o que escolher. Dê uma olhada em input(). Aqui está um link (https://www.tutorialspoint.com/python/python_files_io.htm).

# Determinação do dicionário para a busca:
fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak", "organismo" : "cavalo"}

# Determinando "fav_thing":
fav_thing = "livro"

# Pedindo o valor de "livro" no dicionário através da chave "fav_thing":
print(fav_dict[fav_thing])
# Retorno:
# Ranger's Apprentice