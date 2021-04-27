import timeit
import numpy as np
setup = "import numpy as np"
snippet_1 = """
A = np.arange(1000)
"""
snippet_2 = """
B = [x for x in range(1000)]
"""
snippet_3 = """
C = []
for x in range(1000):
    C.append(x)
"""
print(timeit.timeit(stmt=snippet_1, setup=setup, number=10000))
print(timeit.timeit(stmt=snippet_2, number=10000))
print(timeit.timeit(stmt=snippet_3, number=10000))