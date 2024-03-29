arquivo = open('L1Q3.in', 'r').readlines()


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


class NoSimples():
    def __init__(self, chave):
        self.chave = chave
        self.proximo = None


class ListaSimples():
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir(self, chave):

        if self.cabeca:
            ponteiro = self.cabeca
            for i in range(1, self._tamanho):
                ponteiro = ponteiro.proximo
            no = NoSimples(chave)
            ponteiro.proximo = no
            no.proximo = self.cabeca
            self._tamanho += 1

        else:
            self.cabeca = NoSimples(chave)
            self.cabeca.proximo = self.cabeca
            self._tamanho += 1

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        ponteiro = self.cabeca
        if self._tamanho == 1:
            return ponteiro.chave
        if self._tamanho > 1:
            r = ""
            for i in range(self._tamanho):
                if i == self._tamanho - 1:
                    r = r + str(ponteiro.chave)
                else:
                    r = r + str(ponteiro.chave) + "->"
                ponteiro = ponteiro.proximo
            return r
        return ""

    def __str__(self):
        return self.__repr__()


class NoDuplo():
    def __init__(self, chave):
        self.chave = chave
        self.lista_simples = ListaSimples()
        self.proximo = None
        self.anterior = None


class ListaDupla():
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    def inserir(self, chave, tipo="inteiro"):
        if tipo == "inteiro":
            self.inserir_inteiro(chave)
        else:

            self.inserir_real(chave)

    def inserir_inteiro(self, chave):

        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = NoDuplo(chave)
            ponteiro.proximo.anterior = ponteiro
            self._tamanho += 1
        else:
            self.cabeca = NoDuplo(chave)
            self._tamanho += 1

    def inserir_real(self, chave):
        chave_atual = int(chave)
        ponteiro = self.cabeca
        condicao = True
        while(condicao):
            if ponteiro == None:
                return
            
            if ponteiro.chave == chave_atual:
                ponteiro.lista_simples.inserir(chave)
                return
            ponteiro = ponteiro.proximo

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        if self._tamanho > 0:
            r = "["
            ponteiro = self.cabeca
            while(ponteiro):
                if(ponteiro.proximo == None):
                    resultado = f"{ponteiro.chave}({ponteiro.lista_simples.__str__()})"
                else:
                    resultado = f"{ponteiro.chave}({ponteiro.lista_simples.__str__()})->"

                ponteiro = ponteiro.proximo
                r = r + resultado
            r = r + "]"
            return r
        return ""

    def __str__(self):
        return self.__repr__()

class RespostaRL1Q2(Base):

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.matriz_inicial = None
        self.array_listas = None
        self.executar()

    def tratar_arquivo(self, arquivo):
        tamanho = len(arquivo)
        matriz_temporaria = self.criar_array(tamanho)
        for i in range(tamanho):
            linha_atual_LE = arquivo[i].strip().split("LI")[0].replace("LE", "").strip().split(" ")
            linha_atual_LI = arquivo[i].strip().split("LI")[1].strip().split(" ")
            for j in range(len(linha_atual_LE)):
                linha_atual_LE[j] = eval(linha_atual_LE[j])
            for j in range(len(linha_atual_LI)):
                linha_atual_LI[j] = eval(linha_atual_LI[j])
            self.merge_sort(linha_atual_LE, 0, len(linha_atual_LE) - 1)
            self.merge_sort(linha_atual_LI, 0, len(linha_atual_LI) - 1)
            array_temporario = self.criar_array(2)
            array_temporario[0] = linha_atual_LE
            array_temporario[1] = linha_atual_LI
            matriz_temporaria[i] = array_temporario
        return matriz_temporaria

    def criar_array_listas(self):
        tamanho = len(self.matriz_inicial)
        array_temporario = self.criar_array(tamanho)
        for i in range(tamanho):
            lista = ListaDupla()
            linha_atual = self.matriz_inicial[i]
            
            le = linha_atual[0]
            for j in range(len(le)):
                lista.inserir(le[j])    
            
            li = linha_atual[1]
            for j in range(len(li)):
                lista.inserir(li[j], tipo="reais") 
            array_temporario[i] = lista.__str__()
        self.array_listas = array_temporario
            
            
    
    def escrever_arquivo(self):
        resposta = open('L1Q3.out', 'w')
        array = self.array_listas
        for i in range(len(array)):
            resposta.write(array[i].__str__())
            if(i < len(array)-1):
                resposta.write("\n")
        resposta.close()

    def executar(self):
        # Executar os metodos e atribuir valor aos atributos da classe de forma ordenada
        self.matriz_inicial = self.tratar_arquivo(self.arquivo)
        self.criar_array_listas()
        self.escrever_arquivo()

resposta = RespostaRL1Q2(arquivo)