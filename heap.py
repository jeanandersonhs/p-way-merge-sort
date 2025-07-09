class Node:
    """Classe que representa um nó no Min-Heap"""
    def __init__(self, value, bit=0):
        self.value = value
        self.bit = bit  # bit de controle para o merge sort, se necessário
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f"Node({self.value})"
    
    def valor(self):
        """Retorna o valor do nó"""
        return self.value


class MinHeap:
    """Implementação de uma Min-Heap usando"""
    
    def __init__(self):
        self.heap = []

    def __len__(self):
        """Retorna o tamanho do heap"""
        return self.heap
    
    def _parent_index(self, index):
        """Retorna o índice do pai do nó no índice dado"""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """Retorna o índice do filho esquerdo do nó no índice dado"""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """Retorna o índice do filho direito do nó no índice dado"""
        return 2 * index + 2
    
    def _has_parent(self, index):
        """Verifica se o nó tem pai"""
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        """Verifica se o nó tem filho esquerdo"""
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        """Verifica se o nó tem filho direito"""
        return self._right_child_index(index) < len(self.heap)
    
    def _parent(self, index):
        """Retorna o valor do pai do nó no índice dado"""
        return self.heap[self._parent_index(index)]
    
    def _left_child(self, index):
        """Retorna o valor do filho esquerdo do nó no índice dado"""
        return self.heap[self._left_child_index(index)]
    
    def _right_child(self, index):
        """Retorna o valor do filho direito do nó no índice dado"""
        return self.heap[self._right_child_index(index)]
    
    def _swap(self, index1, index2):
        """Troca dois elementos de posição no heap"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _heapify_up(self, index):
        """Move o elemento para cima até encontrar sua posição correta"""
        while (self._has_parent(index) and 
               self._parent(index).value > self.heap[index].value):
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)
    
    def _heapify_down(self, index):
        """Move o elemento para baixo até encontrar sua posição correta"""
        while self._has_left_child(index):
            smaller_child_index = self._left_child_index(index)
            
            # Encontra o menor filho
            if (self._has_right_child(index) and 
                self._right_child(index).value < self._left_child(index).value):
                smaller_child_index = self._right_child_index(index)
            
            # Se o nó atual é menor que o menor filho, está na posição correta
            if self.heap[index].value < self.heap[smaller_child_index].value:
                break
            
            self._swap(index, smaller_child_index)
            index = smaller_child_index
    
    def push(self, value, bit=0):
        """Adiciona um novo elemento ao heap"""
        node = Node(value, bit)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)
    
    def pop(self):
        """Remove e retorna o menor elemento do heap"""
        if len(self.heap) == 0:
            raise IndexError("pop from empty heap")
        
        # Salva o elemento mínimo
        min_item = self.heap[0]
        
        # Move o último elemento para o topo
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        
        # Reorganiza o heap se ainda há elementos
        if len(self.heap) > 0:
            self._heapify_down(0)
        
        return min_item
    
    def peek(self):
        """Retorna o menor elemento sem removê-lo"""
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")
        return self.heap[0].value
    
    def heapify(self, values):
        """Transforma uma lista de valores em uma min-heap"""
        # Limpa o heap atual
        self.heap = []
        
        # Adiciona todos os valores como nodes
        for value in values:
            self.heap.append(Node(value))
        
        # Aplica heapify de baixo para cima, começando do último nó interno
        # O último nó interno está no índice (n//2 - 1)
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def is_empty(self):
        """Verifica se o heap está vazio"""
        return len(self.heap) == 0
    
    def size(self):
        """Retorna o tamanho do heap"""
        return len(self.heap)
    
    def __str__(self):
        """Representação string do heap"""
        if len(self.heap) == 0:
            return "[]"
        return "[" + ", ".join(str(node.value) for node in self.heap) + "]"
    
    def __repr__(self):
        return f"MinHeap({[node.value for node in self.heap]})"


# Exemplo de uso
if __name__ == "__main__":
    # Criando um min-heap
    heap = MinHeap()
    
    print("=== Testando push ===")
    values = [10, 4, 15, 20, 2, 8, 1]
    for val in values:
        heap.push(val)
        print(f"Inserido {val}, heap: {heap}")
    
    print(f"\nMenor elemento (peek): {heap.peek()}")
    print(f"Tamanho do heap: {heap.size()}")
    
    print("\n=== Testando pop ===")
    while not heap.is_empty():
        min_val = heap.pop()
        print(f"Removido {min_val}, heap: {heap}")
    
    print("\n=== Testando heapify ===")
    lista = [20, 15, 8, 10, 5, 7, 6, 2, 9, 1]
    print(f"Lista original: {lista}")
    
    heap.heapify(lista)
    print(f"Após heapify: {heap}")
    
    print("\nRemoção ordenada após heapify:")
    while not heap.is_empty():
        print(f"Removido: {heap.pop()}")