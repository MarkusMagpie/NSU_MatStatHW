import numpy as np
from scipy.stats import chi2

data = np.array([
    0.037, 0.941, 0.683, 0.15, 0.84, 0.137, 0.374, 0.316, 0.907, 0.042,
    0.729, 0.065, 0.709, 0.299, 0.105, 0.703, 0.149, 0.049, 0.107, 0.470, 
    0.258, 0.364, 0.415, 0.123, 0.311, 0.752, 0.999, 0.409, 0.337, 0.654
])

k = 10 # число интервалов
n = len(data)

# сколько реально наблюдений из data попали в каждый интервал (частоты) и границы интервалов
observed_freq, edges = np.histogram(data, bins=k, range=(0, 1))

# ожидаемые частоты для равномерного распределения U[0,1]
expected_freq = n / k 

# расстояние хи-квадрат
chi_sq_stat = np.sum((observed_freq - expected_freq)**2 / expected_freq)

# степени свободы
df = k - 1

# p-value - вероятность получить статистику не менее наблюдаемой под H_0 => вычисляю хвост
# P(chi_sq_stat >= chi_sq_stat(на данной выборке)) = 1 - F(chi_sq_stat(на данной выборке)) = 1 - P(chi_sq_stat < chi_sq_stat(на данной выборке))
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html
p_value = 1 - chi2.cdf(chi_sq_stat, df)

print(f"наблюдаемые частоты: {observed_freq}")
print(f"ожидаемые частоты: {expected_freq:.3f}")
print(f"расстояние хи-квадрат/Пирсона: {chi_sq_stat:.3f}")
print(f"степени свободы (k-1): {df}")
print(f"p-value: {p_value:.4f}")


if (p_value <= 0.05): 
    print("отвергаем H_0: данные НЕ следуют равномерному распределению U[0, 1]")
elif (p_value >= 0.1):
    print("принимаем H_0: данные согласуются с равномерным распределением U[0, 1]")