# CEN0336_2024_12531993_Python05

O texto a seguir corresponde com o conteúdo dos arquivos adaptado para a visualização via GitHub.

## 1. Escreva um script no qual você construa um dicionário de suas coisas favoritas.

- Criação do dicionário:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

- Conferindo o resultado:

print(fav_dict)

- Retorno: {'livro': "Ranger's Apprentice",'música': 'Cabin In The Trees - Trung Kien Nguyen', 'árvore': 'Oak'}


## 2. Print o seu livro favorito.

- Determinando o dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

- Encontrando o valor ("Ranger's Apprentice") no dicionário a partir da sua chave ("livro"):

print(fav_dict["livro"])

- Retorno: Ranger's Apprentice


## 3. Print o seu livro favorito, mas use uma variável na chave.

- Determinação do dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

- Determinação do valor ("livro") como a variável ("fav_thing"):

fav_thing = "livro"

- Encontrando o valor ("Ranger's Apprentice") no dicionário a partir da variável ("fav_thing") representando a chave ("livro"):

print(fav_dict[fav_thing])

- Retorno: Ranger's Apprentice


## 4. Agora print a sua árvore favorita.

- Determinação do dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

- Encontrando o valor ("Oak") no dicionário a partir da sua chave ("árvore"):

print(fav_dict["árvore"])

- Retorno: Oak


## 5. Adicione o seu "organismo" favorito ao dicionário. Faça com que "organismo" seja o novo valor da chave fav_thing.

- Determinação do dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak"}

- Adicionando ao dicionário (fav_dict) a nova chave (organismo) e seu valor (cavalo):

fav_dict["organismo"] = "cavalo"

- Confirmando a adição:

print(fav_dict)

- Retorno:

{'livro': "Ranger's Apprentice", 'música': 'Cabin In The Trees - Trung Kien Nguyen', 'árvore': 'Oak', 'organismo': 'cavalo'}          

- Tornando "organismo" o novo valor da chave "fav_thing":

fav_thing = "organismo"

- Obtendo o valor da chave "organismo" através da chave "fav_thing":

print(fav_dict[fav_thing])

- Retorno:

cavalo


## 6. Obtenha um valor da linha de comando para fav_thing e print o valor desse item do dicionário. Talvez você queira imprimir todas as chaves para o usuário, para que eles saibam o que escolher. Dê uma olhada em input(). Aqui está um link (https://www.tutorialspoint.com/python/python_files_io.htm).

- Determinação do dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak", "organismo" : "cavalo"}

- Determinando "fav_thing":

fav_thing = "livro"

- Pedindo o valor de "livro" no dicionário através da chave "fav_thing":

print(fav_dict[fav_thing])

- Retorno:

Ranger's Apprentice


## 7. Altere o valor do seu organismo favorito.

- Determinação do dicionário para a busca:

fav_dict = {"livro" : "Ranger's Apprentice","música" : "Cabin In The Trees - Trung Kien Nguyen","árvore" : "Oak", "organismo" : "cavalo"}

- Alterando o valor da chave "organismo" para "cachorro":

fav_dict["organismo"] = "cachorro"

- Obtendo o valor da chave "organismo" modificada:

print(fav_dict["organismo"])

- Retorno:

cachorro


## 8. Obtenha fav_thing da linha de comando e um novo valor para essa chave. Altere o valor com o valor inserido pelo usuário.

- Determinação do dicionário:

fav_dict = {"livro" : "Ranger's Apprentice",
            "música" : "Cabin In The Trees - Trung Kien Nguyen",
            "árvore" : "Oak",
            "organismo" : "cachorro"
            }

- Determinando como "fav_thing" o valor da chave "livro" (Ranger's Apprentice):

fav_thing=fav_dict["livro"]

- Obtendo o valor da chave "fav_thing":

print(fav_thing)

- Retorno:

Ranger's Apprentice

- Alterando o valor da chave "livro" para "The Brotherband Chronicles":

fav_dict["livro"]="The Brotherband Chronicles"

- Obtendo o dicionário atualizado:

print(fav_dict)

- Retorno:

{'livro': 'The Brotherband Chronicles', 'música': 'Cabin In The Trees - Trung Kien Nguyen', 'árvore': 'Oak', 'organismo': 'cachorro'}

- Atualizando o valor da chave "fav_thing":

fav_thing=fav_dict["livro"]

- *Sem repetir esse comando, o "print" a seguir iria retornar o valor anterior da chave "fav_thing": Ranger's Apprentice, apesar do valor ter sido alterado no dicionário

- Obtendo o valor da chave "livro" a partir da chave "fav_thing":

print(fav_thing)

- Retorno:

The Brotherband Chronicles


## 9. Use um loop for para imprimir cada chave e valor do dicionário.

- Determinação do dicionário:

fav_dict={'livro': 'The Brotherband Chronicles',

'música': 'Cabin In The Trees - Trung Kien Nguyen',

'árvore': 'Oak',

'organismo': 'cachorro'}

- Uso do loop "for" para para imprimir cada chave e valor do dicionário:

for favoritos in fav_dict: # determinando as chaves do dicionário como "favoritos"

coisas=fav_dict[favoritos] # determinando os valores das chaves "favoritos" como "coisas"
    
print(favoritos,":",coisas) # obtendo cada chave e seu respectivo valor do dicionário "fav_dict"

- Retorno:

livro : The Brotherband Chronicles

música : Cabin In The Trees - Trung Kien Nguyen

árvore : Oak

organismo : cachorro


## 10. Crie um conjunto usando as duas sintaxes diferentes para criar um conjunto, myset = set() e myset2 = {}. Qual é a diferença? Importa como você cria o conjunto?

- Criação dos dois conjuntos a partir das duas sinteses diferentes:

mySet = set("ATGTGGG") # No caso, o conjunto "mySet" criado por "set()" considera cada letra da chave "ATGTGGG" individualmente

mySet2 = {"ATGCCT"} # Aqui o conjunto "mySet2" criado por chaves "{}" considera a chave "ATGCCT" como um único elemento

- Para exemplificar, a união dos dois conjuntos:

print(mySet|mySet2)

- Retorno (os elementos podem vir em outra ordem):

{'T', 'A', 'G', 'ATGCCT'}

- Na resposta fornecida, temos como elementos provenientes do conjunto "mySet" os elementos "T", "A" e "G". Podemos ver que suas duplicatas foram removidas

- Temos também o elemento "ATGCCT", proveniente do conjunto "mySet2", que apesar de ser formado pelos elementos do conjunto "mySet", aparece por ser considerado um único elemento 


## 11. Escreva um script para encontrar a interseção, diferença, união e diferença simétrica entre esses dois conjuntos.

- Comjuntos fornecidos:

SetA = {3,14,15,9,26,5,35,9}

SetB = {60,22,14,0,9}

- Operações requeridas:

print("interseção:", SetA&SetB) # Uso do "&" para a obtenção dos elementos ao mesmo tempo em ambos os conjuntos

print("diferença SetA SetB:", SetA-SetB) # Uso do "-" para obtenção dos elementos em "SetA" mas não em "SetB"

print("diferença SetB SetA:", SetB-SetA) # Uso do "-" para obtenção dos elementos em "SetB" mas não em "SetA"

print("união:", SetA|SetB) # Uso do "|" para obtenção de todos os elementos em um dos conjuntos ou em ambos

print("diferênça simétrica:", SetA^SetB) # Uso do "^" para a obtenção dos elementos em "SetA" ou "SetB", mas não em ambos

- Retorno:

interseção: {9, 14}

diferença SetA SetB: {3, 35, 5, 15, 26}

diferença SetB SetA: {0, 60, 22}

união: {0, 35, 3, 5, 9, 14, 15, 22, 26, 60}

diferênça simétrica: {0, 3, 5, 15, 22, 26, 35, 60}


## 12. Se você criar um conjunto usando uma sequência de DNA, o que você obterá? Tente com esta sequência:

- Sequência de DNA fornecida:

DNA = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC"

- Criação do conjunto com "set()", retornando cada letra que aparece na sequência de DNA, sem suas duplicatas:

Seq1 = set(DNA)

print(Seq1)

- Retorno:

{'A', 'C', 'T', 'G'}

- Criação do conjunto com "{}", retornando toda a sequência de DNA, pois ela foi colocada como um único elemento:

Seq2 = {DNA}

print(Seq2)

- Retorno:
{'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'}


## 13. Composição de Nucleotídeos. Escreva um script que:

- determine os caracteres únicos nesta sequência:

SeqDNA = "GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA"

- itere sobre cada caractere único e conte o número encontrado na sequência

- armazene cada contagem em um dicionário. Exemplo: nt_comp['A'] = 2

- quando terminar de contar cada caractere, calcule e relate a composição de nucleotídeos e o conteúdo de GC.

- Criação de um dicionário "nt_count":

nt_count={}

- Criando o conjunto "unique" a partir da função "set()":

unique = set(SeqDNA)

- Determinando os caracteres que aparecem em "SeqDNA", sem suas duplicatas:

print("nucleotídeos únicos na sequência:", unique)

- Retorno:

nucleotídeos únicos na sequência: {'A', 'C', 'T', 'G'}

- Uso do "for" para a iterar sobre cada nucleotídeo único:

for nt in unique:

count = SeqDNA.count(nt) # Para contar o número em que aparece esse nucleotídeo na SeqDNA
    
nt_count[nt] = count # Adicionando a contagem no dicionário criado anteriormente

- Pedindo as chaves (nucleotídeos) e valores (vezes em que aparece) do dicionário:

print("vezes que aparecem cada nucleotídeo:", nt_count)

- Retorno:

vezes que aparecem cada nucleotídeo: {'A': 360, 'C': 227, 'T': 370, 'G': 206}

- Contando o conteúdo de GC (em porcentagem):

conteudo_CG = 100 * (nt_count["C"] + nt_count["G"]) / (nt_count["A"] + nt_count["T"] + nt_count["C"] + nt_count["G"])

- Também poderia ser realizado por:

conteudo_CG = ((SeqDNA.count("C") + SeqDNA.count("G")) / (SeqDNA.count("A") + SeqDNA.count("T") + SeqDNA.count("C") + SeqDNA.count("G")))*100

- Imprimindo o resultado:

print("conteúdo CG (%):", conteudo_CG)

- Retorno:

conteúdo CG (%): 37.23129836629407

