import numpy as np
import matplotlib.pyplot as plt

# 定义高斯分布的参数
mu = 20   # 均值
sigma = 100 # 标准差
# 生成数据
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# 绘制高斯分布曲线
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=rf'Gaussian ($\mu={mu}$, $\sigma={sigma}$)')
plt.title('Gaussian Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()