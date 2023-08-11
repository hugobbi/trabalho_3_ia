from typing import Iterable, Set, Tuple

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
        if isinstance(self, outro):
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
    
    def isRoot(self) -> bool:
        return self.pai is None
    
    def printNodo(self) -> None:
        print(f"Estado\t= {self.get_estado()}")
        print(f"Ação\t= {self.get_acao()}")
        print(f"Pai\t= {self.get_pai()}")
        print(f"Custo\t= {self.get_custo()}")

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


def astar_hamming(estado:str) -> list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


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