class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class ListaLigada:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def esta_vazia(self):
        return self._quantidade == 0

    def imprimir(self):
        if self.esta_vazia():
            print("\nA lista está vazia.")
            return

        celula_atual = self.inicio
        posicao = 0
        print("\n--- Conteúdo da Lista ---")
        while celula_atual is not None:
            print(f"[{posicao}] {celula_atual.conteudo}")
            celula_atual = celula_atual.proximo
            posicao += 1
        print("-------------------------")

    def inserir_no_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1

    def inserir_no_fim(self, conteudo):
        if self.esta_vazia():
            self.inserir_no_inicio(conteudo)
            return

        celula_final = self._celula(self._quantidade - 1)
        celula = Celula(conteudo)
        celula_final.proximo = celula
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao < 0 or posicao > self.quantidade:
            raise IndexError(f"Posição inválida {posicao}. Permitido entre 0 e {self.quantidade}")

        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return

        if posicao == self.quantidade:
            self.inserir_no_fim(conteudo)
            return

        celula_anterior = self._celula(posicao - 1)
        celula = Celula(conteudo)
        celula.proximo = celula_anterior.proximo
        celula_anterior.proximo = celula
        self._quantidade += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("A lista está vazia! Não é possível remover.")

        removido = self._inicio
        self._inicio = self._inicio.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if self.esta_vazia():
            raise IndexError("A lista está vazia! Não é possível remover.")

        self._validar_posicao(posicao)

        if posicao == 0:
            return self.remover_do_inicio()

        celula_anterior = self._celula(posicao - 1)
        removido = celula_anterior.proximo
        celula_anterior.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        celula = self._celula(posicao)
        return celula.conteudo

    def pesquisar(self, termo):
        """Retorna a posição da primeira ocorrência onde o termo coincide com o nome da Loja."""
        celula_atual = self.inicio
        posicao = 0
        while celula_atual is not None:
            if hasattr(celula_atual.conteudo, 'nome') and termo.lower() in celula_atual.conteudo.nome.lower():
                return posicao, celula_atual.conteudo
            elif str(termo).lower() in str(celula_atual.conteudo).lower():
                return posicao, celula_atual.conteudo
            celula_atual = celula_atual.proximo
            posicao += 1
        return -1, None

    def limpar(self):
        self._inicio = None
        self._quantidade = 0

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        celula_atual = self.inicio
        for _ in range(posicao):
            celula_atual = celula_atual.proximo
        return celula_atual

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição inválida {posicao}")