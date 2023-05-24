import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 定义参数
m1 = 1000     # 车体质量
m2 = 50       # 车架质量
k1 = 20000    # 车架弹簧刚度
k2 = 5000     # 缓冲弹簧刚度
D = 500       # 缓冲阻尼系数

# 定义传递函数
def H(s):
    return k1 * (D*s + k2) / (m1*m2*s**4 + (m1+m2)*D*s**3 + (k1*m2+k2*m1+k2*m2)*s**2 + k1*D*s + k1*k2)

# 定义时域输入信号
def xi(t):
    return np.sin(2*np.pi*t*0.1)

# 定义求解函数
def f(t, y):
    y1, y2 = y      # y1表示位移，y2表示速度
    dy1 = y2
    dy2 = -2*zeta*omega_n*y2 - omega_n**2*y1 + k1*D*xi(t) + k1*k2*a*np.sin(omega*t)
    return [dy1, dy2]

# 定义初始条件
y0 = [0, 0]     # 初始位移和速度
a, omega = 0.2, 2      # 输入信号的振幅和角频率

# 计算ωn和ζ
omega_n = np.sqrt((k1*m2+k2*m1+k2*m2) / (m1*m2))
zeta = (m1+m2)*D / (2*np.sqrt((k1*m2+k2*m1+k2*m2)*(m1*m2)))

# 定义时间范围
t_start, t_end = 0, 30
t = np.linspace(t_start, t_end, 1000)

# 求解微分方程
sol = solve_ivp(f, [t_start, t_end], y0, t_eval=t)

# 绘制时域曲线
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0])
plt.xlabel('Time [s]')
plt.ylabel('Displacement [m]')
plt.title('Response of Vehicle Suspension with Different Input Signal')
plt.show()