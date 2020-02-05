
#Python 3

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.interpolate
# =============================================================================
# 
# t=np.array([0, 10, 15, 20, 22.5, 30])
# v=np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67,])
# 
# #Plot
# plt.close('all')
# plt.figure(1)
# plt.grid(axis='both', which='major', color=[166/255,166/255, 166/255],
#          linestyle='-', linewidth=2)
# plt.grid(axis='both', which='minor', color=[166/255, 166/255, 166/255],
#          linestyle=':', linewidth=2)
# plt.minorticks_on()
# plt.xlabel('time (s)')
# plt.ylabel('volocity (m/s)')
# plt.title('Projectile of a rocket')
# plt.scatter(t, v, 50, [255/255, 0/255, 0/255], label='orignal data')
# plt.legend(loc='upper left')
# plt.plot([16,16], [0, np.max(v)], color=[0/255, 176/255, 80/255],
#          linestyle=':', linewidth=2)
# 
# #nearest point interpolation
# t16=16
# v16_nearest=v[2]
# plt.scatter(t16, v16_nearest, 50, color=[0/255, 112/255, 192/255],
#             label='nearest point interp. t(16)')
# 
# #linear interpolation
# tlin=np.array([[1, t[2]],[1,t[3]]])
# vlin=v[[2, 3]]
# alin=np.linalg.solve(tlin, vlin)
# t16_lin=[1, 16]
# v16_lin=np.dot(alin, t16_lin)
# v16_lin=np.round(v16_lin, 3)
# plt.scatter(t16, v16_lin, 50, color=[0/255, 122/255, 192/255],
#             label='linear interp, t(16)')
# t0_lin=[1, 0]
# v0_lin=np.dot(alin, t0_lin)
# t30_lin=[1, 30]
# v30_lin=np.dot(alin, t30_lin)
# #plt.plot([0, 30], [v0_lin, v30_lin], 50, color=[0/255, 176/255, 80/255], linestyle=':', linewidth=2)
# 
# #quadratic interpolation
# tquad=np.array([[1, t[1], t[1]**2],
#                  [1, t[2], t[2]**2],
#                  [1, t[3], t[3]**2]])
# vquad=v[[1, 2, 3]]
# aquad=np.linalg.solve(tquad, vquad)
# t16_quad=[1, 16, 16**2]
# v16_quad=np.dot(aquad, t16_quad)
# v16_quad=np.round(v16_quad, 3)
# 
# #cubic interpolation
# tcubic=np.array([[1, t[1], t[1]**2, t[1]**3],
#                  [1, t[2], t[2]**2,t[2]**3],
#                  [1, t[3], t[3]**2,t[3]**3],
#                  [1, t[4], t[4]**2,t[4]**3],])
# vcubic=v[[1, 2, 3, 4]]
# acubic=np.linalg.solve(tcubic, vcubic)
# t16_cubic=[1, 16, 16**2, 16**3]
# v16_cubic=np.dot(acubic, t16_cubic)
# v16_cubic=np.round(v16_cubic, 3)
# 
# 
# #in-built interpolate function
# 
# #nearest point interpolation
# fvnearest=sp.interpolate.interp1d(t, v, kind='nearest')
# tnearest=np.arange(start=0, stop=30, step=1)
# vnearest=fvnearest(tnearest)
# plt.plot(tnearest, vnearest, color='blue', label='nearest point interp.')
# 
# #linear interpolation
# fvlinear=sp.interpolate.interp1d(t, v, kind='linear')
# tlinear=np.arange(start=0, stop=30, step=1)
# vlinear=fvlinear(tlinear)
# plt.plot(tlinear, vlinear, color='red', label='linear interp.')
# 
# #quadratic interpolation
# fvquadratic=sp.interpolate.interp1d(t, v, kind='quadratic')
# tquadratic=np.arange(start=0, stop=30, step=1)
# vquadratic=fvquadratic(tquadratic)
# plt.plot(tquadratic, vquadratic, color='green', label='quadratic interp.')
# 
# #cubic interpolation
# fvcubic=sp.interpolate.interp1d(t, v, kind='cubic')
# tnew=np.arange(start=0, stop=30, step=1)
# vcubic=fvcubic(tnew)
# plt.plot(tnew, vcubic, color='black', label='cubic interp.')
# plt.legend(loc='upper left')
# 
# =============================================================================
import numpy as np
import pandas as pd

df1= pd.DataFrame({'tenor':['1w', '1m', '3m', '2y'],
                   'rate':[2.40, 2.51, 2.66, 2.92],
                   'end_date':['14022020', '09022020', '07052020', '07022022']})

df2= pd.DataFrame({'tenor':['3x6', '6x9', '9x12'],
                   'rate':[2.95, 3.06, 3.98],
                   'end_date':['07082020', '09112020', '08022021']})

df3= pd.DataFrame({'tenor':['2y', '3y', '4y'],
                   'rate':[1.80, 1.81, 1.84],
                   'end_date':['08022022', '07022023', '07022024']})


d = {'ois':df1, 'fra':df2, 'irs':df3}


df4= pd.DataFrame({'label':['ois', 'ois', 'fra', 'fra', 'irs', 'irs', 'irs'],
                   'tenor':['1w', '1m', '3x6', '9x12', '2y', '3y', '4y']})

#df2['Population'] = df2.apply(lambda x: df1.loc[x['Year'] == df1['Year'], x['State']].reset_index(drop=True), axis=1)





