class Fila:    
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item): # enfileirar
        self._vet.append(item)
    
    def dequeue(self): # desenfileirar
        if not self.is_empty():
            return self._vet.pop(0)
        return None

    def front(self): # mostrar o 1o da fila, sem remover!
        if not self.is_empty():
            return self._vet[0]
        return None
                
    def is_empty(self): # retorna se a fila esta vazia
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self): # representacao da fila como string
        return str(self._vet)

## TESTES ##
# if __name__ == "__main__":
#     # Criando uma Fila
#     f = Fila()
#     assert len(f) == 0, "Deve ser zero!"

#     # Enfileirando um item
#     f.enqueue(1)
#     assert len(f) == 1, "A fila deveria estar com 1 elemento"

#     f.enqueue(2)
#     assert f.front() == 1, "1o elemento da fila deve ser 1"

#     f.enqueue("imed")
#     f.enqueue(77)

#     senha_chamada = str(f.dequeue())
#     chamadas = []
#     chamadas.append(senha_chamada)
#     print("Elemento removido: " + str(f.dequeue()))

#     print(f)