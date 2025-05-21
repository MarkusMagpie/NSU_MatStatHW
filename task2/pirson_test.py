import numpy as np
from scipy.stats import chi2, uniform

data = np.array([
    0.037, 0.941, 0.683, 0.15, 0.84, 0.137, 0.374, 0.316, 0.907, 0.042,
    0.729, 0.065, 0.709, 0.299, 0.105, 0.703, 0.149, 0.049, 0.107, 0.470, 
    0.258, 0.364, 0.415, 0.123, 0.311, 0.752, 0.999, 0.409, 0.337, 0.654
])

k = 10 # число интервалов
n = len(data)

# сколько реально наблюдений из data попали в каждый интервал (частоты) и границы интервалов
observed_freq, edges = np.histogram(data, bins=k, range=(0, 1))

# uniform.cdf(x) - теоретическая ФР для U[0,1] в точке x (F_0(x_i))
F = uniform.cdf 
# вероятности попадания в каждый интервал
p_j = np.diff(F(edges))  
# ожидаемое количество элементов в каждом интервале j
expected_freq = n * p_j

# расстояние хи-квадрат
res = np.sum((observed_freq - expected_freq)**2 / expected_freq)

# степени свободы
df = k - 1

c_kvantil = chi2.ppf(0.92, df)

# p-value - вероятность получить статистику не менее наблюдаемой под H_0 => вычисляю хвост
# P(res >= res(на данной выборке)) = 1 - F(res(на данной выборке)) = 1 - P(res < res(на данной выборке))
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html
p_value = 1 - chi2.cdf(res, df)

# print(f"наблюдаемые частоты: {observed_freq}")
# print(f"ожидаемые частоты: {expected_freq:.3f}")
print(f"расстояние хи-квадрат/Пирсона (res): {res:.3f}")
print(f"значение квантиля распределения хи-квадрат уровня 1 - epsilon (c_kvantil): {c_kvantil:.3f}")

if (res > 15.421):
    print(f"отвергаем H_0: данные НЕ следуют равномерному распределению U[0, 1] ({res:.3f} >= 15.421)")
else:
    print(f"принимаем H_0: данные согласуются с равномерным распределением U[0, 1] ({res:.3f} < 15.421)")

print(f"\nРДУЗ (p-value): {p_value:.4f}")

if (p_value <= 0.05): 
    print("РДУЗ <= 0.05 => отвергаем H_0")
elif (p_value >= 0.1):
    print("РДУЗ >= 0.1 => принимаем H_0")