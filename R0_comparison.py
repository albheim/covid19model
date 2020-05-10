from pandas import read_csv, read_excel
from numpy import array, zeros, ones
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# data files - replaces the path placeholders with the correct names
df_m28 = read_csv('<path to march 28>/results/base-plot.csv')	 # data frame object from the the csv file
df_a29 = read_csv('<path to april 29>/results/base-plot.csv')
dfs = [df_m28, df_a29]

countries = ['Austria',
'Belgium',
'Denmark',
'France',
'Germany',
'Greece',
'Italy',
'Netherlands',
'Norway',
'Portugal',
'Spain',
'Sweden',
'Switzerland',
'United_Kingdom']

marksize=12
markerstyle = dict(color='#00bf7dff', linestyle='', marker='o', markersize=marksize)

fig, ax = plt.subplots(1, 2, figsize=(8,8))
y = 14
fntsz=15
R0s=1
R0e=8
alp=0.7
for i in range(2):
	ax[i].plot(array([R0s, R0e]),zeros(2),'k',alpha=alp)
	for q in range(R0s,R0e+1):
		ax[i].plot(array([q, q]),array([-0.1, 0.1]),'k',alpha=alp)
		ax[i].plot(array([q, q]),array([0, 14]),'k',alpha=0.2)
		if q%2==0:
			ax[i].text(q, -0.5, str(q), horizontalalignment='center', verticalalignment='center', fontsize=fntsz)
	ax[i].text(4.5, -1, '$R_0$', horizontalalignment='center', verticalalignment='center', fontsize=fntsz)
	
for country in countries:
	for i in range(len(dfs)):
		ax[i].plot(array([R0s, R0e]),y*ones(2),'k',alpha=0.2)
		try:
			rt = dfs[i].loc[(dfs[i].country==country),'rt'].iloc[0]
			rt_min = dfs[i].loc[(dfs[i].country==country),'rt_min'].iloc[0]
			rt_max = dfs[i].loc[(dfs[i].country==country),'rt_max'].iloc[0]
			ax[i].plot(array([rt_min, rt_max]),y*ones(2),'g',alpha=1,linewidth=4)
			ax[i].plot(rt,y, fillstyle='full', **markerstyle)
		except:
			pass
	if country=='United_Kingdom':
		ax[0].text(-2, y, 'United Kingdom', horizontalalignment='center', verticalalignment='center', fontsize=fntsz)
	else:
		ax[0].text(-2, y, country, horizontalalignment='center', verticalalignment='center', fontsize=fntsz)
	y -= 1

ax[0].text(4.5, 15, 'March 28', horizontalalignment='center', verticalalignment='center', fontsize=fntsz)
ax[1].text(4.5, 15, 'April 29', horizontalalignment='center', verticalalignment='center', fontsize=fntsz)

ax[0].set_axis_off()
ax[1].set_axis_off()
fig.tight_layout()
plt.show()
