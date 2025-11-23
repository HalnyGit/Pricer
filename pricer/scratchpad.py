
#Python 3

# import numpy as np
# import pandas as pd
# import scipy as sp
# import matplotlib.pyplot as plt
# import scipy.interpolate

# import schedule_builder

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
# =============================================================================
# 
# import numpy as np
# import pandas as pd
# 
# df1= pd.DataFrame({'tenor':['1w', '1m', '3m', '2y'],
#                    'rate':[2.40, 2.51, 2.66, 2.92],
#                    'end_date':['14022020', '09022020', '07052020', '07022022']})
# 
# df2 = pd.DataFrame({'tenor':['3x6', '6x9', '9x12'],
#                    'rate':[2.95, 3.06, 3.98],
#                    'end_date':['07082020', '09112020', '08022021']})
# 
# df3 = pd.DataFrame({'tenor':['2y', '3y', '4y'],
#                    'rate':[1.80, 1.81, 1.84],
#                    'end_date':['08022022', '07022023', '07022024']})
# 
# df4 = pd.DataFrame({'tenor':['2y', '3y', '4y'],
#                    'rate':[1.70, 1.71, 1.74],
#                    'end_date':['08022022', '07022023', '07022024']})
# 
# 
# rates = {'pln_ois':df1, 'pln_fra_3m':df2, 'pln_irs_6m':df3, 'pln_irs_3m':df4}
# 
# for frame in rates:
#     rates[frame]['rate_type'] = frame
# 
# 
# dfA= pd.DataFrame({'rate_type':['pln_ois', 'pln_ois', 'pln_fra_3m', 'pln_fra_3m', 'pln_ois', 'pln_irs_6m', 'pln_irs_6m'],
#                    'tenor':['1w', '1m', '3x6', '9x12', '2y', '3y', '4y']})
# 
# temp_list = []
# for elem in set(dfA['rate_type']):
#     temp_list.append(rates[elem])
#     
# dfAux = pd.concat(temp_list)
# 
# another_temp_list = []
# for elem in temp_list:
#     another_temp_list.append(dfA.merge(elem, on=['rate_type', 'tenor']))
#     
# dfAux = pd.concat(another_temp_list)
# 
# 
# #dfA['rate'] = dfA.apply(lambda x: rates[x['label']][rates[x['label']]['tenor']==x['tenor']]['rate'], axis=1)
# 
# #dfAux = pd.concat([df1, df2, df3])
# #dfA = pd.merge(dfA, dfAux, how = 'left', on = ['tenor']).drop(['end_date'], axis = 1)
# 
# #expected outcome
# dfB= pd.DataFrame({'label':['ois', 'ois', 'fra', 'fra', 'irs', 'irs', 'irs'],
#                    'tenor':['1w', '1m', '3x6', '9x12', '2y', '3y', '4y'],
#                    'rate':[2.40, 2.51, 2.95, 3.98, 1.80, 1.81, 1.84 ]})
# =============================================================================

######################################

#market rates
years = np.arange(1, 11, 1)
market_rates = np.array([0.75, 1.00, 1.25, 1.5, 1.75, 2.00, 2.10, 2.25, 2.25, 2.30 ])


def calc_df(r, qdf):
    '''
    Parameters
    ----------
    r : float, represents rate
    qdf : cumulative sum of dicount factors        
    Returns: floats, discount factors, function assums annual payment of rates!
    '''
    return(1 - qdf * r/100)/(1 + r/100)

def calc_zc(df, t):
    ''' 
    Parameters
    ----------
    df : float, discount factor
    t : float, time in years

    Returns
    -------
    float, zero coupon rate, continous compounding

    '''
    return (np.log(1/df)*1/t)*100

def calc_fwdrate(z1, z2, t1, t2, df=True):
    '''
    Parameters
    ----------
    z1 : float, discount factor or continouosly compounded zero rate of time t1
    z2 : float, discount factor or continouosly compounded zero rate of time t2
         t1 < t2
    t1 : float, time 1
    t2 : float, time 2
    df : boolean, True if dicount factors provided, False for zero coupon rate
    Returns
    -------
    float, forward rate
    ''' 
    if not df:
        z1 = np.exp(-z1/100*t1)
        z2 = np.exp(-z2/100*t2)        
    return (z1/z2-1)*1/(t2-t1)*100

# calculation of zero coupon rates and discount factors from market rates

# discount factors
dfactors = np.array([])
for r in market_rates:
    dfactors = np.append(dfactors, calc_df(r, dfactors.sum()))
    
# zero rates
zrates = np.array([])
for y, df in enumerate(dfactors):
    zrates = np.append(zrates, calc_zc(df, y+1))

# *** INTERPOLATION AND FORWARD RATES ***
# 1) linear interpolation of zero rates
# 2) linear interpolation of logarithm of dicount factors
# 3) cubic spline of logarithm of discount factor
# 4) monotone cubic spline of logarithm of discount factor

quarters = np.arange(1, 10.25, 0.25)

# ad.1a) linear interpolation of zerocoupon curves
fzcr_linear = sp.interpolate.interp1d(years, zrates, kind='linear')
zcr_linear = fzcr_linear(quarters)
 
# ad.1b) forward rates from lineary interpolated zero rates
fr_of_zclin = np.array([])
for i in range(len(quarters)-1):
    fr_of_zclin = np.append(fr_of_zclin, calc_fwdrate(zcr_linear[i], zcr_linear[i+1], quarters[i], quarters[i+1], False))

# ad.2a) linear interpolation of log of discount factor
log_dfactors = np.log(dfactors)

flog_df_linear = sp.interpolate.interp1d(years, log_dfactors, kind='linear')
log_df_linear = flog_df_linear(quarters)
df_loglinear = np.exp(log_df_linear)

# ad.2b) forward rates from log linear interpolation of dicount factors
fr_of_dfloglin = np.array([])
for i in range(len(quarters)-1):
    fr_of_dfloglin = np.append(fr_of_dfloglin, calc_fwdrate(df_loglinear[i], df_loglinear[i+1], quarters[i], quarters[i+1], True))

# ad.3a) cubic spline interpolation of log of discount factor
flog_df_cubic = sp.interpolate.interp1d(years, log_dfactors, kind='cubic')
log_df_cubic = flog_df_cubic(quarters)
df_logcubic = np.exp(log_df_cubic)

# ad.3b) forward rates from log cubic interpolation of dicount factors
fr_of_dflogcubic = np.array([])
for i in range(len(quarters)-1):
    fr_of_dflogcubic = np.append(fr_of_dflogcubic, calc_fwdrate(df_logcubic[i], df_logcubic[i+1], quarters[i], quarters[i+1], True))

# ad.4a) monotone cubic spline interpolation of log of discount factor
flog_df_monotone_cubic = sp.interpolate.PchipInterpolator(years, log_dfactors)
log_df_monotone_cubic = flog_df_monotone_cubic(quarters)
df_log_monotone_cubic = np.exp(log_df_monotone_cubic)

# ad.4b) forward rates from log monotone cubic interpolation of dicount factors
fr_of_dflogmonotonecubic = np.array([])
for i in range(len(quarters)-1):
    fr_of_dflogmonotonecubic = np.append(fr_of_dflogmonotonecubic, calc_fwdrate(df_log_monotone_cubic[i], df_log_monotone_cubic[i+1], quarters[i], quarters[i+1], True))


#plot
plt.close('all')
plt.figure(1)
plt.grid(axis='both', which='major', linestyle='-', linewidth=2)
plt.grid(axis='both', which='minor', linestyle='-', linewidth=1)
plt.tick_params(axis='both', colors='red')
plt.minorticks_on()
plt.xlabel('years')
plt.ylabel('rate')
plt.xticks(years)
plt.title('Yield term structure 1')
plt.scatter(years, market_rates, label='market rates')
plt.scatter(years, zrates, label='zero rates cnt.cmpd')
plt.plot(quarters, zcr_linear, label='zero coupon rates linear')
plt.plot(quarters[:-1], fr_of_zclin, label='fwd rates from linear interp.of zero coupon rates')
plt.plot(quarters[:-1], fr_of_dfloglin, label='fwd rates from linear interp. of log of discount factors')
plt.plot(quarters[:-1], fr_of_dflogcubic, label='fwd rates from cubic interp. of log of discount factors')
plt.plot(quarters[:-1], fr_of_dflogmonotonecubic, label='fwd rates from monotone cubic interp. of log of discount factors')
plt.legend(loc='lower left')

plt.figure(2)
plt.grid(axis='both', which='major', linestyle='-', linewidth=2)
plt.grid(axis='both', which='minor', linestyle='-', linewidth=1)
plt.minorticks_on()
plt.xlabel('years')
plt.ylabel('discount factor')
plt.xticks(years)
plt.title('Discount factor')
plt.scatter(years, dfactors, label='discount factor')
plt.plot(quarters, df_loglinear, label='linear interpolated log of DF')
plt.plot(quarters, df_logcubic, label='cubic interpolated log of DF')
plt.plot(quarters, df_log_monotone_cubic, label='monotone cubic interpolated log of DF')
plt.legend(loc='lower left')






