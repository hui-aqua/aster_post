import matplotlib.pyplot as plt
import numpy as np

def read_posi(file_name):
    posi=np.loadtxt(file_name)
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(posi[:,0],posi[:,1],posi[:,2])

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    plt.show()


if __name__ == "__main__":
    read_posi('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/posi_7.56.txt')