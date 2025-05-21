import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform
from scipy.special import kolmogorov

data = np.array([
    0.037, 0.941, 0.683, 0.15, 0.84, 0.137, 0.374, 0.316, 0.907, 0.042,
    0.729, 0.065, 0.709, 0.299, 0.105, 0.703, 0.149, 0.049, 0.107, 0.470, 
    0.258, 0.364, 0.415, 0.123, 0.311, 0.752, 0.999, 0.409, 0.337, 0.654
])

n = len(data)

# ЭФР
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, n + 1) / n
    return x, y

x, y = ecdf(data)

# построение графика ЭФР и теоретической ФР
plt.figure(figsize=(10, 5))
plt.step(x, y, where='post', label='ЭФР', color='blue')  # ЭФР - ступенчатый график (where - положение вертикального перехода между ступенками (pre, mid, post))
plt.plot(x, uniform.cdf(x), label='теоретическая ФР U[0,1]', linestyle='--', color='red') # теоретическая ФР отображаю f(x)=x на [0,1] 
#uniform.cdf(x) - теоретическая ФР для U[0,1] в точке x (F_0(x_i))

# нахождение точки максимального отклонения между эмпирической и теоретической ФР
d_plus = y - uniform.cdf(x) # F_n(x_i) - F_0(x_i) - (положительные отклонения ЭФР от теоретической) - насколько эмпирическая ФР выше теоретической на каждой упорядоченной точке 
d_minus = uniform.cdf(x) - (y - 1/n) # F_0(x_i) - (F_n(x_i) - 1/n) - (отрицательные отклонения теоретическая ФР выше ЭФР слева от точки x) 
# насколько теоретическая ФР выше ЭФР слева от точки X_i (при сравнении слева от каждого узда ЭФР = (i-1)/n)
d = np.maximum(d_plus, d_minus) # для каждой точки макисмальное отклонение между ЭФР и теоретической ФР
max_idx = np.argmax(d) # индекс точки где отклонение d максимально
sup_point = x[max_idx] # значение x в котором достигается максимальное отклонение d

# помечаю точку супремума на графике
plt.scatter(sup_point, y[max_idx], color='black', zorder = 2, label=f'максимальное отклонение (D={np.max(d):.3f})')
plt.vlines(sup_point, ymin=uniform.cdf(sup_point), ymax=y[max_idx], color='black', linestyle='dotted') 
# ymin - нижняя граница линии по оси Y - значение теоретической ФР в точке максимального отклонения F_0(sup_point)
# ymax - верхняя граница линии по оси Y - значение ЭФР в точке максимального отклонения F_n*(sup_point)

plt.xlabel('значение элемента выборки X_i', fontsize=14)
plt.ylabel('CDF', fontsize=14)
plt.title('эмпирическая и теоретическая ФР', fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig("ECDF_for_Kolmogorov_test.png")
plt.show()

# наибольшее отклонение (sup) по всем точкам между ЭФР и теоретической
d_statistic = np.max(d)

# элементы статистического критерия: мера близости (res) и квантиль (k_kvantil)  
res = np.sqrt(n) * d_statistic
# 1 - epsilon = 1 - 0.08 = 0.92. k_(0.92) = ?
# https://people.cs.pitt.edu/~lipschultz/cs1538/prob-table_KS.pdf
# https://vk.com/doc-50757966_626670653
k_kvantil = 1.269

# вычисляю РДУЗ (из мана:  It is equal to the (limit as n->infinity of the) probability that sqrt(n) * max absolute deviation > y)
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.kolmogorov.html
p_value = kolmogorov(res)

print(f"значение sup|F_n^(*)(t) - F_0(t)| = {d_statistic:.3f} в точке t = {sup_point:.3f}")
print(f"расстояние Колмогорова (res): {res:.3f}")
print(f"значение квантиля распределения Колмогорова уровня 1 - epsilon (k_kvantil): {k_kvantil:.3f}")

if res > k_kvantil:
    print(f"отвергаем H_0: данные НЕ следуют равномерному распределению на [0, 1] ({res:.3f} >= {k_kvantil:.3f})")
else:
    print(f"принимаем H_0: данные согласуются с равномерным распределением на [0, 1] ({res:.3f} < {k_kvantil:.3f})")

print()

print(f"РДУЗ (p-value): {p_value:.3f}")

if (p_value <= 0.05): 
    print("РДУЗ <= 0.05 => отвергаем H_0")
elif (p_value >= 0.1):
    print("РДУЗ >= 0.1 => принимаем H_0")