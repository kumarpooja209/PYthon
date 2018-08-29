import matplotlib.pyplot as plt
import numpy as np


'''x = np.arange(0,4*np.pi,0.1)  
y = np.sin(x)
plt.plot(x,y)
plt.show()'''


x = np.arange(0,2*np.pi,0.1)  
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
'''plt.show()


x = np.arange(0,4*np.pi-1,0.1)   
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)'''

plt.xlabel('x axis')   
plt.ylabel('sin and cos')
plt.title('sin and cos wave')
plt.legend(['sin', 'cos'])       
plt.show()
