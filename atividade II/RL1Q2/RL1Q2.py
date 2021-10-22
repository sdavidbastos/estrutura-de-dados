arquivo = open('L1Q2.in', 'r').readlines()


class Pilha:

    def __init__(self, tam):
        self.pilha = [None] * tam
        self.topo = -1

    def esta_vazia(self):
        return self.topo == -1

    def esta_cheia(self):
        return self.topo == len(self.pilha) - 1

    def empilhar(self, novo):
        if not self.esta_cheia():
            self.topo = self.topo + 1
            self.pilha[self.topo] = novo

            return True
        return False

    def desempilheirar(self):
        if not self.esta_vazia():
            self.topo = self.topo - 1
            return self.pilha[self.topo + 1]

        return False

    def get_pilha(self):
        return self.S


class Base():

    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = A[p + i]
        for j in range(0, n2):
            R[j] = A[q + j+1]
        # eliminamos as linhas 8 e 9 pois não usaremos sentinelas
        i = 0
        j = 0
        for k in range(p, r+1):
            if(i < n1 and j < n2):
                if L[i] < R[j]:
                    A[k] = L[i]
                    i = i + 1
                else:
                    A[k] = R[j]
                    j = j + 1
            elif i == n1:
                A[k] = R[j]
                j = j + 1
            elif j == n2:
                A[k] = L[i]
                i = i + 1

    def merge_sort(self, A, p, r):
        if p < r:
            q = int((p+r)/2)
            self.merge_sort(A, p, q)
            self.merge_sort(A, q+1, r)
            self.merge(A, p, q, r)

    def criar_array(self, tamanho, valor=None):
        return [valor]*tamanho

    def criar_matriz_2d(self, linhas=1, colunas=1, valor=None):
        matriz = self.criar_array(colunas)

        for i in range(colunas):
            matriz[i] = self.criar_array(linhas, valor)

        return matriz

    def clonar_matriz_vazia_2d(self, matriz):
        tamanho_matriz = len(matriz)
        matriz_atual = self.criar_array(tamanho_matriz)
        for i in range(tamanho_matriz):
            tamanho_array = len(matriz[i])
            matriz_atual[i] = self.criar_array(tamanho_array, valor=None)
            for j in range(tamanho_array):
                tamanho_array_atual = len(matriz[i][j])
                matriz_atual[i][j] = self.criar_array(tamanho_array_atual)
        return matriz_atual

    def criar_dicionario(self, tamanho=1, padrao=[None, None]):
        return padrao * tamanho

    def soma(self, array):
        total = 0
        tamanho = len(array)
        for i in range(tamanho):
            total = total + array[i]
        return total


class RespostaRL1Q2(Base):

    matriz_inicial = None

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.executar()

    def tratar_arquivo(self, arquivo):
        tamanho = len(arquivo)
        matriz = self.criar_array(tamanho)
        for i in range(tamanho):
            linha_atual = arquivo[i].strip().split(" ")
            matriz[i] = linha_atual
        return matriz

    def criar_matriz_pilhas(self, matriz):
        matriz_temporaria = self.clonar_matriz_vazia_2d(matriz)
        print(matriz_temporaria)

    def executar(self):
        # Executar os metodos e atribuir valor aos atributos da classe de forma ordenada
        self.matriz_inicial = self.tratar_arquivo(self.arquivo)


RespostaRL1Q2(arquivo)
