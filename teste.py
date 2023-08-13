from solucao import *
import time

# 123456_78
# 12345_678
# 2_3541687
# 185423_67
nodo_raiz = Nodo("185423_67", None, None, 0)

start = time.time()
caminho = astar_hamming(nodo_raiz.get_estado())
end = time.time()

# 23553

print(caminho)
print(len(caminho))
print(f"tempo={end-start} s")