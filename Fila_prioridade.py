import heapq

class FilaPrioridade:
    def __init__(self):
        self.fila = []

    def adicionar_usuario(self, usuario):
        heapq.heappush(self.fila, (usuario.idade, usuario.nome))

    def proximo_usuario(self):
        if self.fila:
            idade, nome = heapq.heappop(self.fila)
            return nome, idade
        else:
            return None