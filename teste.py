from solucao import *
import time


# 123456_78 2
# 12345_678 13
# 2_3541687 23
# 185423_67 none
nodo_raiz = Nodo("185423_67", None, None, 0)

start = time.time()
caminho = astar_hamming(nodo_raiz.get_estado())
end = time.time()

# 23553

if caminho is None:
    print("Não há soluções")
else:
    print(caminho)
    print(len(caminho))

print(f"tempo={end-start} s")