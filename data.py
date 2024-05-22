import numpy as np
def data(size, mean=0, scale=.5):
    x = np.linspace(0, 2*np.pi, num=size)
    y = np.sin(x)
    yp = y.copy()
    noise = np.random.normal(loc=mean, scale=scale, size=(size))
    for i in range(size):
        if np.random.rand() < .2:
            yp[i] += noise[i]
    return x, y, yp