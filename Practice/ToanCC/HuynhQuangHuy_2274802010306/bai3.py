import numpy as np
import matplotlib.pyplot as plt
import os

def vedothi2(fs):
    all_time = np.linspace(0,2,200)
    t = all_time [:100]
    fig, ax = plt.subplots()

    for f in fs:
        y = np.sin(2*np.pi*f*t)
        ax.plot(t,y, label = '{} Hz'.format(f))

    plt.legend()


    os.chdir('C:\\Users\\TGDD\\OneDrive\\Desktop\\Learn IT\\Practice\\ToanCC\\DoThi\\')
    plt.savefig('basic_python_bai3.pdf')
    plt.show()

if __name__ == "__main__":
    fs = [1,2,4]
    vedothi2(fs)