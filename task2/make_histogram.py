import matplotlib.pyplot as plt # для графиков

data = [0.037, 0.941, 0.683, 0.15, 0.84, 0.137, 0.374, 0.316, 0.907, 0.042,
        0.729, 0.065, 0.709, 0.299, 0.105, 0.703, 0.149, 0.049, 0.107, 0.470, 
        0.258, 0.364, 0.415, 0.123, 0.311, 0.752, 0.999, 0.409, 0.337, 0.654]

n = len(data)
k = 10 
x_min, x_max = min(data), max(data)
print("a = {}, b = {}".format(x_min, x_max))
h = (x_max - x_min) / k # ширина каждого бина (отрезка)

# границы интервалов
bins = [x_min + i*h for i in range(k+1)]

# сама гистограмма плотности
plt.figure(figsize=(10, 5))
plt.hist(
    data,
    bins=bins,          # списко границ интервалов [t_0, t_1], ..., [t_(k-1), t_k] (bins=10 разбил бы на равные по ширине интервалы)
    density=True,       # =False показывал бы просто v_j (док-во что сумма частот равна 30), а не v_j / (nh) - отчего сумарная площадь нашей гистограммы равна 1
    alpha=0.75,         # прозрачность столбцов
    edgecolor='black'
)

plt.xlabel('значение', fontsize=14)
plt.ylabel('оценка плотности', fontsize=14)
plt.title(f'гистограмма плотности (n={n}, k={k}, h={h:.3f})', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig("histogram.png")
plt.show()

# www.geeksforgeeks.org/how-to-calculate-and-plot-a-cumulative-distribution-function-with-matplotlib-in-python/