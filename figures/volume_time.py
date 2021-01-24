import matplotlib.pyplot as plt
import numpy as np
import os


path_to_case='.\\U0.4_failed'

resu=np.load(os.path.join(path_to_case,'result_volume.npz'))

print('mean  '+str(np.mean(resu['volume'])))
print('std  '+str(np.std(resu['volume'])))
print('max  '+str(np.max(resu['volume'])))
print('min  '+str(np.min(resu['volume'])))
print('range  '+str(np.ptp(resu['volume'])))



plt.figure()
plt.plot(resu['time'],resu['volume'])
# plt.xlim(0,10)
plt.ylim(0,60000)
plt.xlabel('Time (s)')
plt.ylabel('Volume (m$^3$)')
plt.savefig(os.path.join(path_to_case,'volume_time.png'),dpi=600)
plt.show()