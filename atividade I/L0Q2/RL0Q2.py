arquivo = open('L0Q2.in', 'r').readlines()


class RespostaRL0Q2():

    array_dados = []

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.executar()

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

    def tratar_arquivo(self):
        linhas = [linha.strip().split(" ") for linha in arquivo]
        for linha in linhas:
            self.array_dados.append(self.criar_dicionario_por_tipo(linha))

    def criar_dicionario_por_tipo(self, array):
        dicionario = {"str": [], "int": [], "float": [], "p": [
        ], "distancias": [], "distancias_origem": [], "distancias_pontos": {}, "pontos_ordenados": []}
        for elemento in array:
            try:
                elemento_atual = eval(elemento)
                if(type(elemento_atual) == int):
                    dicionario["int"].append(elemento_atual)

                if(type(elemento_atual) == float):
                    dicionario["float"].append(elemento_atual)

                if(type(elemento_atual) == tuple):
                    dicionario["p"].append(elemento_atual)

            except NameError:
                dicionario["str"].append(elemento.lower())
        return dicionario

    def ordenar_arrays(self):
        for dados in self.array_dados:
            self.merge_sort(dados["str"], 0, len(dados["str"])-1)
            self.merge_sort(dados["int"], 0, len(dados["int"])-1)
            self.merge_sort(dados["float"], 0, len(dados["float"])-1)
            self.merge_sort(dados["distancias_origem"], 0,
                            len(dados["distancias_origem"])-1)

    def distancia_dois_pontos(self, ponto_a, ponto_b=[0, 0]):
        xa, ya = ponto_a
        xb, yb = ponto_b
        return ((xb-xa)**2 + (yb - ya)**2)**(1/2)

    def criar_array_distancia_dois_pontos(self):
        for dados in self.array_dados:
            pontos = dados["p"]
            for i in range(len(pontos)):
                if(i < len(pontos)-1):
                    distancia = self.distancia_dois_pontos(
                        pontos[i], pontos[i+1])
                    dados["distancias"].append(distancia)
                distancia_origem = self.distancia_dois_pontos(pontos[i])
                dados["distancias_origem"].append(distancia_origem)

    def criar_dicionario_distancia_pontos(self):
        for dados in self.array_dados:
            for i in range(len(dados["distancias_origem"])):
                distancia_atual = dados["distancias_origem"][i]
                ponto_atual = dados["p"][i]
                dados["distancias_pontos"][distancia_atual] = ponto_atual

    def criar_array_pontos_ordenados(self):
        for dados in self.array_dados:
            for distancia_origem in dados["distancias_origem"]:
                ponto_atual = dados["distancias_pontos"][distancia_origem]
                dados["pontos_ordenados"].append(ponto_atual)

    def transforma_array_pontos_string(self, array):
        string = ""
        for elemento in array:
            string += str(elemento).replace(" ", "") + " "
        return string.strip()

    def transforma_array_numeros_string(self, array):
        string = ""
        for elemento in array:
            string += str(elemento) + " "
        return string.strip()

    def transforma_array_string_string(self, array):
        string = ""
        for elemento in array:
            string += elemento + " "
        return string.strip()

    def escrever_arquivo(self):
        resposta = open('L0Q2.out', 'w')
        array = self.array_dados
        for i in range(len(array)):
            nomes = self.transforma_array_string_string(array[i]["str"])
            inteiros = self.transforma_array_numeros_string(array[i]["int"])
            reais = self.transforma_array_numeros_string(array[i]["float"])
            pontos = self.transforma_array_pontos_string(
                array[i]["pontos_ordenados"])
            resposta_linha = f"str:{nomes} int:{inteiros} float:{reais} p:{pontos}"
            resposta.write(resposta_linha)
            if(i < len(array)-1):
                resposta.write("\n")
        resposta.close()

    def executar(self):
        self.tratar_arquivo()
        self.criar_array_distancia_dois_pontos()
        self.criar_dicionario_distancia_pontos()
        self.ordenar_arrays()
        self.criar_array_pontos_ordenados()
        self.escrever_arquivo()

resposta = RespostaRL0Q2(arquivo)