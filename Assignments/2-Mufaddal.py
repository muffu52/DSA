import numpy as np
import matplotlib.pyplot as plt

# unable to use np.float128 as dtype, using np.longdouble as replacement
x = np.logspace(0,15,100,dtype=np.longdouble)

y_1 = np.ones(100)
y_n = x
y_square = x*x
y_squareroot = np.sqrt(x)
y_nlogn = x*np.log(x)
y_cube = x**3
y_2n = 2**x

fig = plt.figure()
p = fig.add_subplot(1,1,1)
p.set_yscale('log')
p.set_xscale('log')

# set limits for graph
p.set_xlim(1,10**15)
p.set_ylim(1,10**19)
p.plot(x,y_1,label='1')
p.plot(x,y_n,label='n')
p.plot(x,y_square,label='n^2')
p.plot(x,y_squareroot,label='sqrt(n)')
p.plot(x,y_nlogn,label='nlogn')
p.plot(x,y_cube,label='n^3')
p.plot(x,y_2n,label='2^n')

plt.xlabel("X")
plt.title("Functions")
plt.legend()
plt.show()