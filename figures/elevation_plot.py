import numpy as np
import matplotlib.pyplot as plt
file_elevation='E:\\UbuntuFiles\\roxelaqua\\U0.4\\pythonOutput\\elevations_1h.txt'
elevations=np.loadtxt(file_elevation)
dt=1
t_end=100
t=np.arange(0,t_end,dt)
plt.figure()
plt.plot(t,elevations[:int(t_end/dt)])
plt.xlabel('Time (s)')
plt.ylabel('Elevation (m)')
plt.xlim(0,t_end)
plt.ylim(-4,4)
plt.show()     