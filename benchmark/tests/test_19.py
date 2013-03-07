from qutip import *
from time import time

def test_19(N=1.0):
    """
    expectation values
    """
    test_name='expect vals [25]'
    N=25
    alpha=3j
    a=destroy(N)
    coh=coherent_dm(N,alpha)
    coh_dm=coherent_dm(N,alpha)
    n=num(N)

    tot_elapsed = 0
    for m in range(N):
        tic=time()
        expect(n,coh)
        expect(n,coh_dm)
        toc=time()
        tot_elapsed += toc - tic

    return [test_name], [tot_elapsed / N]
 

if __name__=='__main__':
    test_19()
