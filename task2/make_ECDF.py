import matplotlib.pyplot as plt
import numpy as np

data = [0.037, 0.941, 0.683, 0.15, 0.84, 0.137, 0.374, 0.316, 0.907, 0.042,
        0.729, 0.065, 0.709, 0.299, 0.105, 0.703, 0.149, 0.049, 0.107, 0.470, 
        0.258, 0.364, 0.415, 0.123, 0.311, 0.752, 0.999, 0.409, 0.337, 0.654]

x = np.sort(data)
n = len(x) # размер выборки=30

# ЭФР значения на каждом элементе: i/n (i от 1 до n) 
y = np.arange(1, n+1) / n # массив [1, 2, ..., n], делим каждый элемент на n => [1/n, 2/n, ..., n/n]

# теориетическая ФР для U[0,1] <=> F(X)=X на [0,1] 
x_line = np.linspace(0, 1, 100)

plt.figure(figsize=(10, 5))
plt.step(x, y, where='post', label='ЭФР', color='blue') # ЭФР - ступенчатый график (where - положение вертикального перехода между ступенками (pre, mid, post))
plt.plot(x_line, x_line, linestyle='--', label='теоретическая ФР U[0,1]', color='red')

plt.xlabel('значение элемента выборки X_i', fontsize=14)
plt.ylabel('F_30^(*)(t) (ФР)', fontsize=14)
plt.title('эмпирическая и теоретическая ФР', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig("ECDF.png")
plt.show()
