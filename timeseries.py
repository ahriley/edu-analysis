import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# options for what to actually plot
names = ['Texas A & M University-College Station', 'Rice University', 'The University of Texas at Austin']
plotname = ['tamu', 'rice', 'ut-austin']
plotthing = 'race-time'
cols_wanted = ['demographics.race_ethnicity.black', 'demographics.race_ethnicity.white',
        'demographics.race_ethnicity.hispanic', 'demographics.race_ethnicity.asian']
plotlabels = ['black', 'white', 'hispanic', 'asian']

# years of data available
years = ['1996_97', '1997_98', '1998_99', '1999_00', '2000_01', '2001_02',
        '2002_03', '2003_04', '2004_05', '2005_06', '2006_07', '2007_08',
        '2008_09', '2009_10', '2010_11', '2011_12', '2012_13', '2013_14',
        '2014_15', '2015_16']

# import all the dataframes, grab what's important
df = pd.DataFrame(index=names, columns=years)
for year in years:
    df_temp = pd.read_csv('data/'+year+'_clean.csv')
    df_temp.set_index('name', inplace=True)
    df_temp = df_temp[cols_wanted]
    for name in df.index:
        dems = list(df_temp.loc[name])
        df[year][name] = dems

for col in cols_wanted:
    df[col] = ""

for name in names:
    for i in range(len(cols_wanted)):
        col = cols_wanted[i]
        breakdown = []
        for year in years:
            breakdown.append(df[year][name][i])
        df[col][name] = breakdown

for i in range(len(names)):
    for j in range(len(cols_wanted)):
        col = cols_wanted[j]
        plt.plot(np.array(range(len(years)))-4, df[col][names[i]], 'o', label=plotlabels[j])
    plt.legend(loc='best')
    plt.xlabel('Starting School Year')
    plt.ylabel('% enrolled')
    plt.ylim(0,1)
    plt.savefig('plots/'+plotname[i]+'-'+plotthing+'.png', bbox_inches='tight')
    plt.close()
