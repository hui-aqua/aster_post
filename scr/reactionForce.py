import matplotlib.pyplot as plt
import numpy as np
import os


def read_reaction_file(floder):
    with open(os.path.join(floder,"reactionforce.txt"),'r') as f:
        lines=f.readlines()
    f.close()
    data=lines[5:]
    print(len(data))
    print(data[-1])

    time=[]
    force=[]
    torqu=[]
    for each in data[:-1]:
        time.append(float(each.split("   ")[-7].lstrip(" ")))
        force.append([float(each.split("   ")[-6].lstrip(" ")),float(each.split("   ")[-5].lstrip(" ")),float(each.split("   ")[-4].lstrip(" "))])
        torqu.append([float(each.split("   ")[-3].lstrip(" ")),float(each.split("   ")[-2].lstrip(" ")),float(each.split("   ")[-1].lstrip(" "))])

    result={'time':time,
            'force':np.array(force),
            'torque':np.array(torqu)
            }
    return result

def plot_time_history(data):
    plt.figure()
    plt.plot(data['time'],-data['force'][:,0],label='Fx')
    plt.plot(data['time'],-data['force'][:,1],label='Fy')
    plt.plot(data['time'],-data['force'][:,2],label='Fz')   
    plt.legend()
    # plt.ylim(-50000,50000)

    plt.show()     

if __name__ == "__main__":
    k=read_reaction_file('/home/hui/aster_test/roxelaqua/asterTest/asteroutput_10s')
    plot_time_history(k)
    