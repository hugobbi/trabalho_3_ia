from typing import Iterable, Set, Tuple
import heapq
from dataclasses import dataclass, field

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:"Nodo" or None, acao:str or None, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.acao = acao
        self.pai = pai
        self.custo = custo
    
    def __eq__(self, outro: "Nodo") -> bool:
        if isinstance(outro, Nodo):
            return (self.estado == outro.estado and self.acao == outro.acao and self.pai == outro.pai and self.custo == outro.custo) # pode dar ruim a comparacao do pai
        return False

    def __hash__(self) -> int:
        return hash((self.estado, self.acao, self.pai, self.custo)) # pode dar ruim o hash do pai
    
    def get_estado(self) -> str: 
        return self.estado
    
    def get_acao(self) -> str: 
        return self.acao
    
    def get_pai(self) -> "Nodo": 
        return self.pai
    
    def get_custo(self) -> int: 
        return self.custo
    
    def calcula_custo(self) -> int: # custo de uma ação para um nodo filho futuro
        return self.get_custo() + 1
    
    def ehRaiz(self) -> bool:
        return self.pai is None
    
    def ehEstadoFinal(self) -> bool:
        return self.get_estado() == "12345678_"
    
    def printNodo(self) -> None:
        print(f"Estado\t= {self.get_estado()}")
        print(f"Ação\t= {self.get_acao()}")
        print(f"Pai\t= {self.get_pai()}")
        print(f"Custo\t= {self.get_custo()}")

@dataclass(order=True)
class NodoFronteira(Nodo): # talvez seja usado, mas acho que não
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

def swap(string: str, idx1: int, idx2: int) -> str:
    string_lista = list(string)

    i1_salvo = string_lista[idx1]
    string_lista[idx1] = string_lista[idx2]
    string_lista[idx2] = i1_salvo

    string_trocada = "".join(string_lista)

    return string_trocada

def sucessor(estado:str) -> Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    possiveis_estados = set()
    indice_espaco = estado.index("_")

    """
    Tabuleiro:
    0 1 2 
    3 4 5
    6 7 8
    """
    if indice_espaco % 3 != 0: # espaço não está na primeira coluna
        estado_novo = swap(estado, indice_espaco, indice_espaco - 1)
        possiveis_estados.add(("esquerda", estado_novo))

    if (indice_espaco + 1) % 3 != 0: # espaço não está na última coluna
        estado_novo = swap(estado, indice_espaco, indice_espaco + 1)
        possiveis_estados.add(("direita", estado_novo))

    if indice_espaco > 2: # espaço não está na primeira linha
        estado_novo = swap(estado, indice_espaco, indice_espaco - 3)
        possiveis_estados.add(("acima", estado_novo))

    if indice_espaco < 6: # espaço não está na última linha
        estado_novo = swap(estado, indice_espaco, indice_espaco + 3)
        possiveis_estados.add(("abaixo", estado_novo))

    return possiveis_estados


def expande(nodo:Nodo) -> Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    estado_nodo = nodo.get_estado()
    possiveis_estados = sucessor(estado_nodo)
    nodos_filhos = set()
    for estado in possiveis_estados:
        nodo_filho = Nodo(estado[1], nodo, estado[0], nodo.calcula_custo())
        nodos_filhos.add(nodo_filho)
    return nodos_filhos

def calcula_hamming(estado: str) -> int: # distância de Hamming -> número de peças fora do lugar
    estado_final = "12345678_"
    hamming = 0
    for c1, c2 in zip(estado, estado_final):
        if c1 != c2:
            hamming += 1
    return hamming

def calcula_heuristica_hamming(nodo: Nodo) -> int:
    return nodo.get_custo() + calcula_hamming(nodo.get_estado())

def astar_hamming(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    explorados = []
    nodo_raiz = Nodo(estado, None, None, 0) # nodo inicial
    fronteira = [(calcula_heuristica_hamming(nodo_raiz), nodo_raiz)] # fronteira é implementada como min-heap priority queue, cada item é uma tupla
    caminho = []                                                     # (valor, nodo)
    while fronteira: # enquanto tiver nodos na fronteira
        nodo_atual = fronteira[0]
        if nodo_atual[1].ehEstadoFinal():
            caminho.append(nodo_atual[1].get_acao())
            return caminho
        # retirar nodo do heap
        if nodo_atual[1] not in explorados:
            explorados.append(nodo_atual[1])
            # adicionar vizinhos do nodo atual no heap
            vizinhos = sucessor(nodo_atual[1].get_estado())
        fronteira = []

    return None # não há solução




def astar_manhattan(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def bfs(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def astar_new_heuristic(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError