from liner_system import com_linear_data
from noliner_system import com_nolinear_data
import matplotlib.pyplot as plt




if __name__ == '__main__':

    ax1 = plt.subplot(211)
    ax1.margins(0.05)
    t1,x1,v1 = com_nolinear_data(5)
    ax1.plot(t1, x1,'--',label='nolinear(5x)')
    ax1.plot(t1, v1,'--',label='nolinear(5v)')
    t2,x2,v2 = com_nolinear_data(20)
    ax1.plot(t2, x2,'--',label='nolinear(20x)')
    ax1.plot(t2, v2,'--',label='nolinear(20v)')
    t3,x3,v3 = com_nolinear_data(45)
    ax1.plot(t3, x3,'--',label='nolinear(45x)')
    ax1.plot(t3, v3,'--',label='nolinear(45v)')
    plt.xlabel('t')
    plt.ylabel('value')
    ax1.set_title('Nolinear')
    ax1.legend(bbox_to_anchor=(1,1))


    ax2 = plt.subplot(212)
    ax2.margins(0.05)
    t11,x11,v11 = com_linear_data(5)
    ax2.plot(t11, x11,'--',label='linear(5x)')
    ax2.plot(t11, v11,'--',label='linear(5v)')
    t22,x22,v22 = com_linear_data(20)
    ax2.plot(t22, x22,'--',label='linear(20x)')
    ax2.plot(t22, v22,'--',label='linear(20v)')
    t33,x33,v33 = com_linear_data(45)
    ax2.plot(t33, x33,'--',label='linear(45x)')
    ax2.plot(t33, v33,'--',label='linear(45v)')
    plt.xlabel('t')
    plt.ylabel('value')
    ax2.set_title('Linear')
    ax2.legend(bbox_to_anchor=(1,1))

    plt.tight_layout(pad=0.4,h_pad=0.6,w_pad=5.0)
    plt.show()