import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.interpolate

t=np.array([0, 10, 15, 20, 22.5, 30])
v=np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67,])

plt.close('all')
plt.figure(1)
plt.grid(axis='both', which='major', color=[166/255,166/255, 166/255],
         linestyle='-', linewidth=2)
plt.grid(axis='both', which='minor', color=[166/255, 166/255, 166/255],
         linestyle=':', linewidth=2)
plt.minorticks_on()
plt.xlabel('time (s)')
plt.ylabel('volocity (m/s)')
plt.title('Projectile of a rocket')
plt.scatter(t, v, 50, [255/255, 0/255, 0/255], label='orignal data')
plt.legend(loc='upper left')
plt.plot([16,16], [0, np.max(v)], color=[0/255, 176/255, 80/255],
         linestyle=':', linewidth=2)
t16=16
v16_nearest=v[2]
plt.scatter(t16, v16_nearest, 50, color=[0/255, 112/255, 192/255],
            label='nearest point interpolation')

fvcubic=sp.interpolate.interp1d(t, v, kind='cubic')
tnew=np.arange(start=0, stop=30, step=1)
vcubic=fvcubic(tnew)
plt.plot(tnew, vcubic, color=[0/255, 112/255,192/255])






