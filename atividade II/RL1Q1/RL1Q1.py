arquivo = open('L1Q1.in', 'r').readlines()


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

    def gerar_matriz_vazia_2d(self, matriz):
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


class RespostaRL1Q1(Base):
    matriz_resultados = None
    matriz_chave_valor = None
    matriz_soma = None
    matriz_resultado_ordenado = None
    matriz_resultado_string = None

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.executar()

    def tratar_arquivo(self, arquivo):
        tamanho = len(arquivo)
        matriz = self.criar_array(tamanho)
        for i in range(tamanho):
            linha_atual = arquivo[i].strip().split("start")
            linha_tratada = self.tratar_linha(linha_atual)
            matriz[i] = linha_tratada
        return matriz

    def tratar_linha(self, linha):
        tamanho = len(linha) - 1
        array = self.criar_array(tamanho)
        for i in range(tamanho):
            linha_atual = linha[i+1].strip().split(" ")
            self.tratar_ordernar_elementos(linha_atual)
            array[i] = linha_atual
        return array

    def tratar_ordernar_elementos(self, elementos):
        tamanho = len(elementos)

        for i in range(tamanho):
            elementos[i] = eval(elementos[i])

        self.merge_sort(elementos, 0, tamanho - 1)

    def criar_matriz_chave_valor(self, array):
        tamanho_matriz = len(array)
        matriz_chave_valor = self.criar_array(tamanho_matriz)
        for i in range(tamanho_matriz):
            tamanho_array = len(array[i])
            matriz_chave_valor[i] = self.criar_array(tamanho_array)
            for j in range(tamanho_array):
                dicionario = self.criar_dicionario()
                dicionario[0] = self.soma(array[i][j])
                dicionario[1] = array[i][j]
                matriz_chave_valor[i][j] = dicionario
        return matriz_chave_valor

    def criar_matriz_soma_ordenado(self, array):
        tamanho_matriz = len(array)
        matriz_soma = self.criar_array(tamanho_matriz)

        for i in range(tamanho_matriz):
            tamanho_array = len(array[i])
            matriz_soma[i] = self.criar_array(tamanho_array)
            for j in range(tamanho_array):
                matriz_soma[i][j] = self.soma(array[i][j])

        for i in range(tamanho_matriz):
            array_atual = matriz_soma[i]
            tamanho = len(array_atual)
            self.merge_sort(array_atual, 0, tamanho-1)

        return matriz_soma

    def encontra_por_elemento(self, array, elemento):
        for i in range(len(array)):
            if(array[i][0] == elemento):
                return array[i][1]

    def criar_matriz_resultado_ordenado(self, matriz, matriz_soma):
        matriz_temporaria = self.gerar_matriz_vazia_2d(self.matriz_resultados)
        tamanho_matriz = len(matriz)

        for i in range(tamanho_matriz):
            tamanho_matriz_atual = len(matriz[i])
            for j in range(tamanho_matriz_atual):
                matriz_temporaria[i][j] = self.encontra_por_elemento(
                    matriz[i], matriz_soma[i][j])
        return matriz_temporaria

    def criar_matriz_resultado_string(self, matriz):
        tamanho = len(matriz)
        matriz_temporaria = self.gerar_matriz_vazia_2d(matriz)

        for i in range(tamanho):
            matriz_temporaria[i] = self.criar_array_resultado_string(matriz[i])

        return matriz_temporaria

    def criar_array_resultado_string(self, array):
        tamanho = len(array)
        for i in range(tamanho):
            array[i] = "start " + \
                str(array[i]).replace(
                    "[", "").replace("]", "").replace(",", "")
        return " ".join(array)

    def escrever_arquivo(self):
        resposta = open('L1Q1.out', 'w')
        matriz = self.matriz_resultado_string 
        for i in range(len(matriz)):
            resposta.write(matriz[i])
            if(i < len(matriz)-1):
                resposta.write("\n")
        resposta.close()

    def executar(self):
        # Executar os metodos e atribuir valor aos atributos da classe de forma ordenada
        self.matriz_resultados = self.tratar_arquivo(self.arquivo)
        self.matriz_chave_valor = self.criar_matriz_chave_valor(
            self.matriz_resultados)
        self.matriz_soma = self.criar_matriz_soma_ordenado(
            self.matriz_resultados)
        self.matriz_resultado_ordenado = self.criar_matriz_resultado_ordenado(
            self.matriz_chave_valor, self.matriz_soma)
        self.matriz_resultado_string = self.criar_matriz_resultado_string(
            self.matriz_resultado_ordenado)
        self.escrever_arquivo()


RespostaRL1Q1(arquivo)