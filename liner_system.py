# python定义线性系统
import math
from scipy.integrate import odeint
import numpy as np
# y：定义变量名称
# t：仿真时间，定义成时间序列
# u：模型的参数 = 0
#----------模型定义--------
def Model(y, t, u):
    x1, x2 = y
    dx1=x2
    dx2=-2*x1-x2+u
    return [dx1, dx2]
def com_linear_data(init_position):
    y0 = [init_position*math.pi/180, 0.0]
    t = np.linspace(0, 10, 1000)
    u=0
    sol = odeint(Model, y0, t, args=(u,))
    return t,sol[:,0],sol[:,1]