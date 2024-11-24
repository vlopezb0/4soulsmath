import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

def monstruo(vida,dado):

    if dado != 0:
        p = 1/dado
    else:
        p = 1

    n = vida

    x = range(vida+1)

    rv = binom(n, p)

    ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=10, label='frozen pmf')

    ax.legend(loc='best', frameon=False)

    plt.show()


def combate(isaac_vida,isaac_ataque,monstruo_vida,monstruo_ataque,probabilidad_golpeo):
    k = round(monstruo_vida / isaac_ataque)-1
    n = round(isaac_vida / monstruo_ataque)-1 + round(monstruo_vida / isaac_ataque)
    p = probabilidad_golpeo
    
    print("(",k,n,p,")")

    return 1- binom.cdf(k,n,p)

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1)
    
    isaac_vida = 2
    isaac_ataque = 1
    monstruo_vida = 1
    monstruo_ataque = 2
    monstruo_dado = 4
    
    probabilidad_golpeo= (7-monstruo_dado)/6

    prob = combate(isaac_vida, isaac_ataque, monstruo_vida, monstruo_ataque, probabilidad_golpeo)
    
    print(prob)
    