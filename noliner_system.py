import math
import matplotlib.pyplot as plt
class system():
    def __init__(self):
        self.pa = 0
        self.pv = 0
        self.px = 0
        self.a = 1
        self.b = 2
        self.c = 1
        self.u = 0
        self.delta_t = 0.01
    def system(self):
        self.pa = -1*self.a*self.pv-self.b*math.sin(self.px)+self.c*self.u
        self.pv = self.pv+self.pa*self.delta_t
        self.px = self.px+self.pv*self.delta_t
        self.u = 0

def com_nolinear_data(init_position):
    a = system()
    a.px = init_position*math.pi/180
    x = []
    y = []
    v = []
    for i in range(1000):
        x.append(i*0.01)
        a.system()
        y.append(a.px)
        v.append(a.pv)
    return x,y,v