# Aluna: Maria Thereza
# Disciplina: Sistemas Operacionais I - UFPB
# Projeto 02: Algoritmos de Substituição de Páginas


import sys

def fifo(capacidade, referencias):
    memoria = []
    faltas = 0
    for pagina in referencias:
        if pagina not in memoria:
            if len(memoria) < capacidade:
                memoria.append(pagina)
            else:
                memoria.pop(0)
                memoria.append(pagina)
            faltas += 1
    return faltas

def otm(capacidade, referencias):
    memoria = []
    faltas = 0
    for i in range(len(referencias)):
        pagina_atual = referencias[i]
        if pagina_atual not in memoria:
            if len(memoria) < capacidade:
                memoria.append(pagina_atual)
            else:
                # decide qual página substituir (a que demorar mais a ser usada)
                indice_substituir = -1
                maior_distancia = -1
                
                for j in range(len(memoria)):
                    try:
                        # Busca a próxima ocorrência da página da memória no futuro
                        proxima_ocorrencia = referencias.index(memoria[j], i + 1)
                    except ValueError:
                        # Se não for mais usada, é a candidata ideal
                        proxima_ocorrencia = float('inf')
                    
                    if proxima_ocorrencia > maior_distancia:
                        maior_distancia = proxima_ocorrencia
                        indice_substituir = j
                
                memoria[indice_substituir] = pagina_atual
            faltas += 1
    return faltas

def lru(capacidade, referencias):
    memoria = []
    # Usaremos uma lista para rastrear a ordem de uso (último elemento é o mais recente)
    faltas = 0
    for pagina in referencias:
        if pagina not in memoria:
            if len(memoria) < capacidade:
                memoria.append(pagina)
            else:
                memoria.pop(0) # Remove o menos recentemente usado (primeiro da lista)
                memoria.append(pagina)
            faltas += 1
        else:
            # Se já está na memória, atualiza a posição para "mais recente"
            memoria.remove(pagina)
            memoria.append(pagina)
    return faltas

def main():
    # Leitura da entrada conforme especificado (um número por linha)
    try:
        entrada = sys.stdin.read().split()
        if not entrada:
            return
        
        # O primeiro número é a quantidade de quadros 
        capacidade = int(entrada[0])
        # Os demais são a sequência de referências [cite: 10, 14]
        referencias = [int(x) for x in entrada[1:]]
        
        # Execução e impressão EXATA conforme o formato solicitado [cite: 11, 15, 36]
        print(f"FIFO {fifo(capacidade, referencias)}")
        print(f"OTM {otm(capacidade, referencias)}")
        print(f"LRU {lru(capacidade, referencias)}")
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()