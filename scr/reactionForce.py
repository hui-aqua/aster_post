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
    print('mean force is '+str(np.mean(result['force'],axis=0)))
    print('std force is '+str(np.std(result['force'],axis=0)))
    print('max force is '+str(np.max(result['force'],axis=0)))
    print('min force is '+str(np.min(result['force'],axis=0)))
    print('range force is '+str(np.ptp(result['force'],axis=0)))

    return result



if __name__ == "__main__":
    print(os.getcwd())
    # path_to_result='E:\\UbuntuFiles\\roxelaqua\\U0.4\\asterinput'
    path_to_case='.\\U0.7'
    resu=read_reaction_file(os.path.join(path_to_case,'asteroutput'))
    np.savez(os.path.join(path_to_case,'result_force'),time=resu['time'],
                                                        fx=resu['force'][:,0],
                                                        fy=resu['force'][:,1],
                                                        fz=resu['force'][:,2],
                                                        mx=resu['torque'][:,0],
                                                        my=resu['torque'][:,1],
                                                        mz=resu['torque'][:,2],)