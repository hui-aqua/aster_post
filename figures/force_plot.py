import numpy as np
import os
import matplotlib.pyplot as plt

def read_total_force(force_file):
    force=np.loadtxt(force_file)
    force_sum=np.sum(force,axis=0)
    return force_sum

def plot_time_history(data):
    plt.figure()
    plt.plot(data['time'],-data['force'][:,0]/1000,label='Fx')
    plt.plot(data['time'],-data['force'][:,1]/1000,label='Fy')
    plt.plot(data['time'],-data['force'][:,2]/1000,label='Fz')   
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Force (KN)')
    plt.xlim(0,int(max(data['time'])))
    # plt.ylim()
    plt.show()     


if __name__ == "__main__":
    print(os.getcwd())
    # path_to_result='E:\\UbuntuFiles\\roxelaqua\\U0.4\\asterinput'
    path_to_case='.\\U0.7'
    resu=np.load(os.path.join(path_to_case,'result_force.npz'))
    print(resu)
    plt.figure()
    plt.plot(resu['time'],resu['fx'],label='Fx')
    plt.plot(resu['time'],resu['fy'],label='Fy')
    plt.plot(resu['time'],resu['fz'],label='Fz')   
    plt.legend()
    # plt.ylim(-50000,50000)

    plt.show()
    print(np.linalg.norm(np.array([88930,17113,35603])))