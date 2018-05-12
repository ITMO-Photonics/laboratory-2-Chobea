import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)
coord = np.array([5000.,9000.]) # область появления мяча
velocity = np.array([0.,0.]) # вектор начальной скорости

def init():
    ax.set_xlim([0., 10000.])
    ax.set_ylim([0., 10000.])
    return circle, # отображаемая область

g = 9.8 # ускорение свободного падения

def updatefig(frame):
    coord[1] = coord[1] + velocity[1] * 0.5 # начальная координата плюс смещение на вектор скорости
    velocity[1] = velocity[1] - g # на каждый кадр будет ускорение вниз по у
    if coord[1] <= 236.:
        coord[1] = 236 # неупругий удар, 236 - для избежания деформации
    circle.set_xdata(coord[0])
    circle.set_ydata(coord[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=1000, init_func=init, interval=30, blit=True, repeat=False)
plt.show()
