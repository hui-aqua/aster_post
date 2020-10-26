import numpy as np
import matplotlib.pyplot as plt

def read_total_force(force_file):
    force=np.loadtxt(force_file)
    force_sum=np.sum(force,axis=0)
    return force_sum




    
if __name__ == "__main__":
    dt=0.02
    # itimes is the total iterations
    duration=30
    itimes=int(duration/dt)
    tend=itimes*dt
    time_frame=np.linspace(0,tend,itimes)
    # netting=np.zeros((itimes,3))
    # anchorF=np.zeros((itimes,3))
    # hdpe1Fo=np.zeros((itimes,3))
    # hdpe2Fo=np.zeros((itimes,3))
    # totalFn=np.zeros((itimes,3))
    # for k in range(itimes):
    #     print("k is " +str(k))
    #     totalFn[k]=read_total_force('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/Fnh_'+str(round((k)*dt,3))+'.txt')
    #     netting[k]= read_total_force('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/netting_'+str(round((k)*dt,3))+'.txt')
    #     anchorF[k]= read_total_force('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/anchor_'+str(round((k)*dt,3))+'.txt')
    #     hdpe1Fo[k]= read_total_force('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/hdpe_dyna_'+str(round((k)*dt,3))+'.txt')
    #     hdpe2Fo[k]= read_total_force('/home/hui/aster_test/roxelaqua/asterTest/pythonOutput/hdpe_buoy_'+str(round((k)*dt,3))+'.txt')


    # np.savez("30sForces.npa",netF=netting,anchorF=anchorF,hdpe1F=hdpe1Fo, hdpe2F=hdpe2Fo,totalF=totalFn)
    data=np.load("30sForces.npz")
    plt.figure()
    plt.plot(time_frame,data['anchorF'][:,0],label='Fx')
    plt.plot(time_frame,data['anchorF'][:,1],label='Fy')
    plt.plot(time_frame,data['anchorF'][:,2],label='Fz')   
    plt.legend()
    plt.ylim(-50000,50000)

    plt.show()     