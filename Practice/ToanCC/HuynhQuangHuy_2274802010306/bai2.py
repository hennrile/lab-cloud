import numpy as np
import matplotlib.pyplot as plt 
import os

fs = [1, 2, 4]
all_time = np.linspace(0, 2, 200)
t = all_time [:100]

for f in fs:
    y = np.sin(2*np.pi*f*t)
    plt.plot(t, y, label = "{} Hz".format(f))

plt.legend()

os.chdir('C:\\Users\\TGDD\\OneDrive\\Desktop\\Learn IT\\Practice\\ToanCC\\DoThi\\')
plt.savefig('basic_python_bai2.pdf')
plt.show()
