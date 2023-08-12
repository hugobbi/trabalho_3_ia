from typing import Iterable, Set, Tuple
from solucao import *

# 123456_78
# 2_3541687
nodo_raiz = Nodo("123456_78", None, None, 0)

caminho = astar_hamming(nodo_raiz.get_estado())

print(caminho)