arquivo = open('L0Q1.in', 'r').readlines()


class RespostaRL0Q1():
    matriz_pontos = []
    matriz_distancias = []
    matriz_distancias_origem = []
    matriz_pontos_ordenados = []
    matriz_dicionarios = []
    array_resultados = []

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.executar()

    def insertion_sort(self, A):
        for j in range(1, len(A)):
            key = A[j]
            i = j-1
            while i > 0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key

    def tratar_arquivo(self):
        for linha in arquivo:
            linha_atual = linha.strip().split("s")[1].strip().split(" ")
            self.matriz_pontos.append([eval(valor) for valor in linha_atual])

    def distancia_dois_pontos(self, ponto_a, ponto_b=[0, 0]):
        xa, ya = ponto_a
        xb, yb = ponto_b
        return ((xb-xa)**2 + (yb - ya)**2)**(1/2)

    def criar_array_distancia_dois_pontos(self, array):
        array_distancias = []
        for i in range(len(array) - 1):
            resultado = self.distancia_dois_pontos(
                array[i], array[i+1])
            array_distancias.append(resultado)
        return array_distancias

    def criar_matriz_distancia_dois_pontos(self):
        for array_pontos in self.matriz_pontos:
            self.matriz_distancias.append(
                self.criar_array_distancia_dois_pontos(array_pontos))

    def criar_array_distancia_dois_pontos_origem(self, array_pontos):

        return [
            self.distancia_dois_pontos(x) for x in array_pontos]

    def criar_matriz_distancia_dois_pontos_origem(self):
        for array_pontos in self.matriz_pontos:
            self.matriz_distancias_origem.append(
                self.criar_array_distancia_dois_pontos_origem(array_pontos))

    def criar_array_dicionario(self, array_pontos, array_distancias_origem):
        dicionario = {}
        for i in range(len(array_pontos)):
            dicionario[array_distancias_origem[i]] = array_pontos[i]

        return dicionario

    def criar_matriz_dicionarios(self):
        for i in range(len(self.matriz_distancias_origem)):
            self.matriz_dicionarios.append(self.criar_array_dicionario(
                self.matriz_pontos[i], self.matriz_distancias_origem[i]))

    def criar_array_pontos_ordenados(self, array_distancias_origem_ordenadas, array_dicionario):
        array = array_distancias_origem_ordenadas
        array_pontos_ordenados = []
        for valor in array:
            ponto_atual = array_dicionario[valor]
            array_pontos_ordenados.append(ponto_atual)
        return array_pontos_ordenados

    def criar_matriz_pontos_ordenados(self):
        matriz_origem = self.matriz_distancias_origem
        matriz_dicionarios = self.matriz_dicionarios
        criar_array = self.criar_array_pontos_ordenados
        for i in range(len(matriz_origem)):
            self.insertion_sort(matriz_origem[i])
            array_ordenado = criar_array(
                matriz_origem[i], matriz_dicionarios[i])
            self.matriz_pontos_ordenados.append(array_ordenado)

    def transforma_array_string(self, array):
        string = ""
        for ponto in array:
            string += str(ponto).replace(" ", "") + " "
        return string.strip()

    def criar_array_distances(self):
        return [round(sum(valor), 2) for valor in self.matriz_distancias]

    def criar_array_shurtcuts(self):
        return [round(self.distancia_dois_pontos(array_pontos[0], array_pontos[-1]), 2) for array_pontos in self.matriz_pontos]

    def criar_array_resultados(self):
        array_distances = self.criar_array_distances()
        array_shortcuts = self.criar_array_shurtcuts()
        
        for i in range(len(self.matriz_pontos_ordenados)):
            string_pontos = self.transforma_array_string(self.matriz_pontos_ordenados[i])
            string_completa = f"points {string_pontos} distance {array_distances[i]} shortcut {array_shortcuts[i]}"
            self.array_resultados.append(string_completa)
        
    def escrever_arquivo(self):
        resposta = open('L0Q1.out', 'w')
        array = self.array_resultados
        for i in range(len(array)):
            resposta.write(array[i])
            if(i < len(array)-1):
                resposta.write("\n")
        resposta.close()

    def executar(self):
        self.tratar_arquivo()
        self.criar_matriz_distancia_dois_pontos()
        self.criar_matriz_distancia_dois_pontos_origem()
        self.criar_matriz_dicionarios()
        self.criar_matriz_pontos_ordenados()
        self.criar_array_resultados()
        self.escrever_arquivo()


resposta = RespostaRL0Q1(arquivo)