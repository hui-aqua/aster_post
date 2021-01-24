import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.gridspec as gc

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["figure.figsize"] = (6.3, 3.2)
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['font.weight'] = 'regular'
plt.rcParams['font.size'] = '10'
plt.rcParams["mathtext.default"] = "it"
plt.rcParams["mathtext.fontset"] = "stix"

path_to_case='.\\U0.4_failed'
resu=np.load(os.path.join(path_to_case,'result_volume.npz'))

print('mean  '+str(np.mean(resu['volume'])))
print('std  '+str(np.std(resu['volume'])))
print('max  '+str(np.max(resu['volume'])))
print('min  '+str(np.min(resu['volume'])))
print('range  '+str(np.ptp(resu['volume'])))



plt.figure()
path_to_case='.\\U0.4'
resu=np.load(os.path.join(path_to_case,'result_volume.npz'))

print('mean  '+str(np.mean(resu['volume'])))
print('std  '+str(np.std(resu['volume'])))
print('max  '+str(np.max(resu['volume'])))
print('min  '+str(np.min(resu['volume'])))
print('range  '+str(np.ptp(resu['volume'])))
plt.plot(resu['time'],resu['volume'],label='$U$ = 0.4 m/s')


path_to_case='.\\U0.7'
resu=np.load(os.path.join(path_to_case,'result_volume.npz'))

print('mean  '+str(np.mean(resu['volume'])))
print('std  '+str(np.std(resu['volume'])))
print('max  '+str(np.max(resu['volume'])))
print('min  '+str(np.min(resu['volume'])))
print('range  '+str(np.ptp(resu['volume'])))
plt.plot(resu['time'],resu['volume'],label='$U$ = 0.7 m/s')

path_to_case='.\\U1.0'
resu=np.load(os.path.join(path_to_case,'result_volume.npz'))

print('mean  '+str(np.mean(resu['volume'])))
print('std  '+str(np.std(resu['volume'])))
print('max  '+str(np.max(resu['volume'])))
print('min  '+str(np.min(resu['volume'])))
print('range  '+str(np.ptp(resu['volume'])))
plt.plot(resu['time'],resu['volume'],label='$U$ = 1.0 m/s')



plt.xlim(0,10)
plt.ylim(0,60000)
plt.xlabel('Time (s)')
plt.ylabel('Volume (m$^3$)')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(path_to_case,'volume_time2.png'),dpi=600)
plt.show()