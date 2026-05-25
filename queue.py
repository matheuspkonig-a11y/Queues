class Queue:
    '''Instancia a Queue com a opção de impor ou não um limite de elementos.'''
    def __init__(self, max_size = None):
        self._elements = []
        self._max_size = max_size

    def size(self):
        '''Retorna a quantidade de elementos presentes na lista em INT.'''
        return len(self._elements)

    def is_empty(self):
        '''Retorna True se a lista estiver vazia, caso contrário retorna False. '''
        return self.size() == 0
    

    def is_full(self):
        '''Retorna True se o tamanho da Queue tiver alcançado ou excedido o limite. 
        Caso não tenha chego ou não possua limite retorna False. '''
        if self._max_size is None:
            return False
        
        return self.size() >= self._max_size

    def clear(self):
        '''Remove todos os elementos da lista.'''
        self._elements.clear()

    def enqueue(self, element):
        '''Adiciona um elemento à lista. Se a Queue já estiver cheia causa um Overflow Error'''
        if self.is_full():
            raise OverflowError("Não foi possível adicionar o elemento, pois o limite da Queue foi atingido.")

        self._elements.append(element)
    

    def dequeue(self): 
        '''Remove o primeiro elemento da lista. Se já estiver vazia causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não é possível remover elementos da lista, pois ela já está vazia.")
        
        removed_element = self._elements.pop(0)
        return removed_element

    def peek(self):
        '''Retorna o valor do primeiro elemento da lista. Se estiver vazia causa um Index Error.'''
        if self.is_empty():
            raise IndexError("Não há elementos na lista para visualizar.")
        return self._elements[0]
    

if __name__ == "__main__" :

    '''Nesse exemplo nossa Queue será uma Fila de Espera para entrar em uma partida PvP,
      e os Elementos serão Jogadores'''
    print("\n-------------------Procurando Partida-------------------\n")

    fila = Queue(10)

    print(f"Servidor iniciado... Fila está vazia? ", fila.is_empty())

    # tenta remover um elemento com a lista vazia, retornando erro
    try:
        fila.dequeue()
    except IndexError as erro_exclusao:
        print(f"Erro : {erro_exclusao}")         

    # adiciona cinco novos elementos
    fila.enqueue("ThunderingBubba")
    fila.enqueue("GainfulSnore")
    fila.enqueue("LudicrousPlunk")
    fila.enqueue("LuxuriantCarrots")
    fila.enqueue("DeadpanCauldron")

    # tamanho da Queue
    print(f"Players aguardando: ", fila.size())
    
    # mostra o primeiro elemento da Queue
    print(f"Primeiro Player na fila: ", fila.peek())

    # remove o primeiro elemento da Queue
    fila.dequeue()

    # confirma que o tamanho da Queue diminuiu
    print(f"Players aguardando: ", fila.size())

    # mostra o elemento que assumiu o lugar do que foi removido
    print(f"Primeiro Player na fila: ", fila.peek())

    # adiciona mais 6 elementos
    fila.enqueue("DefectivePotato")
    fila.enqueue("WoebegoneKindergarten")
    fila.enqueue("QuixoticWatson")
    fila.enqueue("WackyDustin")
    fila.enqueue("XenialIce")
    fila.enqueue("SqualidExterminator")

    # mostra novamente o tamanho da Queue
    print(f"Players aguardando: ", fila.size())

    # tenta colocar mais um elemento depois de atingir o limite, retornando erro
    try:
        fila.enqueue("LongingChester")
    except OverflowError as erro_entrada:
        print(f"Erro : {erro_entrada}") 

    # confirma que a fila está com a ocupação máxima
    print(f"A fila está cheia? ", fila.is_full() )
    
    print("\n-------------------Partida Encontrada-------------------\n")

    # como os jogadores acharam uma partida, a fila de espera foi limpa
    fila.clear()
    
    # tenta visualizar primeiro elemento com a lista vazia, retorna erro
    try:
        fila.peek()
    except IndexError as erro_visualizacao:
        print(f"Erro : {erro_visualizacao}")

    # mostra o tamanho da fila, que agora está vazia
    print(f"Players aguardando: ", fila.size())