from typing import Iterable, Set, Tuple
from solucao import *

nodo_raiz = Nodo("2_3541687", None, None, 0)
filhos = expande(nodo_raiz)

print(nodo_raiz)
for filho in filhos:
    filho.printNodo()
    print("")