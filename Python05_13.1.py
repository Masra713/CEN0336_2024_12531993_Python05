# 13. Composição de Nucleotídeos. Escreva um script que:

# determine os caracteres únicos nesta sequência:

SeqDNA = "GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA"

# itere sobre cada caractere único e conte o número encontrado na sequência
# armazene cada contagem em um dicionário. Exemplo: nt_comp['A'] = 2
# quando terminar de contar cada caractere, calcule e relate a composição de nucleotídeos e o conteúdo de GC.

# Criação de um dicionário "nt_count":
nt_count={}

# Criando o conjunto "unique" a partir da função "set()":
unique = set(SeqDNA)

# Determinando os caracteres que aparecem em "SeqDNA", sem suas duplicatas:
print("nucleotídeos únicos na sequência:", unique)
# Retorno:
# nucleotídeos únicos na sequência: {'A', 'C', 'T', 'G'}

# Uso do "for" para a iterar sobre cada nucleotídeo único:
for nt in unique:
    count = SeqDNA.count(nt) # Para contar o número em que aparece esse nucleotídeo na SeqDNA
    nt_count[nt] = count # Adicionando a contagem no dicionário criado anteriormente

# Pedindo as chaves (nucleotídeos) e valores (vezes em que aparece) do dicionário:
print("vezes que aparecem cada nucleotídeo:", nt_count)
# Retorno:
# vezes que aparecem cada nucleotídeo: {'A': 360, 'C': 227, 'T': 370, 'G': 206}

# Contando o conteúdo de GC (em porcentagem):
conteudo_CG = 100 * (nt_count["C"] + nt_count["G"]) / (nt_count["A"] + nt_count["T"] + nt_count["C"] + nt_count["G"])

# Também poderia ser realizado por:
# conteudo_CG = ((SeqDNA.count("C") + SeqDNA.count("G")) / (SeqDNA.count("A") + SeqDNA.count("T") + SeqDNA.count("C") + SeqDNA.count("G")))*100

# Imprimindo o resultado:
print("conteúdo CG (%):", conteudo_CG)
# Retorno:
# conteúdo CG (%): 37.23129836629407