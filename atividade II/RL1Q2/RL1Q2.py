arquivo = open('L1Q2.in', 'r').readlines()


class Pilha:

    def __init__(self, tam):
        self.pilha = [None] * tam
        self.topo = -1

    def elemento_topo(self):
        if(self.esta_vazia()):
            return False
        return self.pilha[self.topo]

    def esta_vazia(self):
        return self.topo == -1

    def esta_cheia(self):
        return self.topo == len(self.pilha) - 1

    def empilhar(self, novo):
        if not self.esta_cheia():
            self.topo = self.topo + 1
            self.pilha[self.topo] = novo

            return novo
        return False

    def desempilhar(self):
        if not self.esta_vazia():
            self.topo = self.topo - 1
            return self.pilha[self.topo + 1]

        return False


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

# Para cada nome da lista e necessario criar um resultado


class Resultado():
    pushes = ""
    pops = 0

    def escrever_resultado(self):
        resposta = self.pushes.strip()
        resposta_final = f"{self.pops}x-pop {resposta}"
        if(self.pops <= 0):
            resposta_final = resposta
        return resposta_final


"""
Para conseguir executar os pushes o pops sem perder os dados, optei por
utilizar uma pilha principal e auxiliar
"""


class PilhaComposta(Base):

    def __init__(self, array_nomes):
        self.array_nomes = array_nomes
        self.tamanho = len(array_nomes)
        self.pilha_principal = Pilha(self.tamanho)
        self.pilha_auxiliar = Pilha(self.tamanho)
        self.array_resultados = self.criar_array(self.tamanho)
        self.inserir_nomes()

    def inserir_nomes(self):
        # Primeiro nome da pilha não precisa de validacao
        primeiro_nome = self.pilha_principal.empilhar(self.array_nomes[0])
        resultado = Resultado()
        resultado.pushes = "push-" + primeiro_nome
        self.array_resultados[0] = resultado

        for i in range(1, self.tamanho):
            nome_atual = self.array_nomes[i]

            # O indice vai indicar em qual resultado temos que trabalhar
            self.inserir_nome(nome_atual, i)

    def inserir_nome(self, nome_atual, index):
        resultado_atual = Resultado()

        self.inserir_nomes_na_pilha_auxiliar(nome_atual, resultado_atual)

        self.array_resultados[index] = resultado_atual

    def inserir_nomes_na_pilha_auxiliar(self, nome, resultado: Resultado):
        condicao = True

        """
        Basicamente utilizamos dois loops:
        primeiro loop => joga os dados da pilha principal na pilha auxiliar
        segundo loop => joga os dados da pilha auxiliar na pilha principal 
        """
        while(condicao):
            """
            Se a pilha_principal esta vazia, significa que 
            o processo de mover da pilha principal para a 
            pilha auxiliar foi concuido.
            """
            esta_vazia = self.pilha_principal.esta_vazia()

            if(esta_vazia):
                self.pilha_auxiliar.empilhar(nome)
                self.reenserir_nomes_na_pilha_principal(resultado)
                break
            elif(self.verifica_ordenacao(self.pilha_principal.elemento_topo(), nome)):
                nome_pop = self.pilha_principal.desempilhar()
                resultado.pops += 1
                self.pilha_auxiliar.empilhar(nome_pop)
            else:
                self.pilha_auxiliar.empilhar(nome)
                self.reenserir_nomes_na_pilha_principal(resultado)
                break

    def reenserir_nomes_na_pilha_principal(self, resultado_atual: Resultado):
        condicao = self.pilha_auxiliar.esta_vazia()
        while(not condicao):
            nome = self.pilha_auxiliar.desempilhar()
            resultado_atual.pushes += f" push-{nome}"
            self.pilha_principal.empilhar(nome)
            condicao = self.pilha_auxiliar.esta_vazia()
    # Poe dois nomes em um array e verifica se estao ordenados

    def verifica_ordenacao(self, a, b):
        array_temporario = self.criar_array(2)
        array_temporario[0] = a
        array_temporario[1] = b

        self.merge_sort(array_temporario, 0, len(array_temporario) - 1)

        if(array_temporario == [a, b]):
            return False
        return True


class RespostaRL1Q2(Base):

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.matriz_inicial = None
        self.array_pilha = None
        self.executar()

    def tratar_arquivo(self, arquivo):
        tamanho = len(arquivo)
        matriz_temporaria = self.criar_array(tamanho)
        for i in range(tamanho):
            linha_atual = arquivo[i].strip().split(" ")
            matriz_temporaria[i] = linha_atual
        return matriz_temporaria

    def criar_array_pilha(self, matriz):
        tamanho = len(matriz)
        array_temporaria = self.criar_array(tamanho)

        for i in range(tamanho):
            linha_atual = matriz[i]
            array_temporaria[i] = PilhaComposta(linha_atual)

        return array_temporaria

    def executar(self):
        # Executar os metodos e atribuir valor aos atributos da classe de forma ordenada
        self.matriz_inicial = self.tratar_arquivo(self.arquivo)
        self.array_pilha = self.criar_array_pilha(self.matriz_inicial)


resposta = RespostaRL1Q2(arquivo)