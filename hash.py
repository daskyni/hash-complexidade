import zlib 

# Calcula a posição de cada livro conforme tamanho do vetor
def calculaPosicao(total_posicoes):
    with open('livros.txt', 'r') as file:
        indices = []
        for linha in file:
            livro = linha.strip()
            hash_livro = zlib.crc32(livro.encode())
            indice = hash_livro % total_posicoes
            indices.append(indice)
        return indices

# Mostra quais posições do vetor foram utilizadas
def imprimePosicoesOcupadas(indices, total_posicoes):
    posicoes_ocupadas = []
    for indice in indices:
        if indice not in posicoes_ocupadas:
            posicoes_ocupadas.append(indice)

    print(f"POSIÇÕES OCUPADAS: {sorted(posicoes_ocupadas)}\n")

    if all(pos in posicoes_ocupadas for pos in range(total_posicoes)):
        print("Todas as posições do vetor foram ocupadas!")
    else:
        print("Ainda há posições disponíveis!")

# Verifica se há mais de um título em um único índice
def temDuplicatas(indices):
    indices_vistos = set()
    for indice in indices:
        if indice in indices_vistos:
            return True  # Duplicata encontrada
        indices_vistos.add(indice)
    return False 

    
# Trocar número conforme número de posições no vetor
total_posicoes = 1021
indices = calculaPosicao(total_posicoes)
print(f"{indices}\n")

imprimePosicoesOcupadas(indices, total_posicoes)

if temDuplicatas(indices) == True:
    print("Há índices armazenando mais de um título!")
else:
    print("Cada índice armazena no máximo um título!")



