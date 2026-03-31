
class Cliente:
    def __init__(self, nome,telefone):
        self._nome = nome
        self._telefone = telefone
#metodo get
    def get_nome(self):
        return self._nome
#metodo set
    def set_nome(self,n):
     self._nome = n