import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# picking out universities
names = ['Texas A & M University-College Station', 'Rice University', 'The University of Texas at Austin']
plotnames = ['tamu', 'rice', 'ut-austin']

df = pd.read_csv('data/2015_16_clean.csv', index_col=0)

for name,plotname in zip(names,plotnames):
    ###################
    # race pie chart
    ###################
    races = ['demographics.race_ethnicity.white', 'demographics.race_ethnicity.black',
            'demographics.race_ethnicity.hispanic', 'demographics.race_ethnicity.asian',
            'demographics.race_ethnicity.aian', 'demographics.race_ethnicity.nhpi',
            'demographics.race_ethnicity.two_or_more', 'demographics.race_ethnicity.unknown',
            'demographics.race_ethnicity.non_resident_alien']
    race_names = [race[28:] for race in races]

    values = []
    for race in races:
        values.append(df[race][name])

    race_names = [x for _,x in sorted(zip(values,race_names))][::-1]
    values = np.sort(values)[::-1]

    patches, texts = plt.pie(values, startangle=90)
    plt.legend(patches, race_names, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.title('Demographic breakdown: '+name)
    plt.savefig('plots/'+plotname+'-race-pie.png', bbox_inches='tight')
    plt.close()

    ###################
    # income pie chart
    ###################
    if df['ownership'][name] == 1:
        base = 'title_iv.public.by_income_level.'
    elif df['ownership'][name] == 2:
        base = 'title_iv.private.by_income_level.'
    else:
        base = ''
        print("Error with public/private classification")
    levels = ['0-30000', '30001-48000', '48001-75000', '75001-110000', '110001-plus']

    values = []
    for level in levels:
        values.append(df[base+level][name])

    patches, texts = plt.pie(values, startangle=90)
    plt.title('Income background breakdown: '+name)
    plt.legend(patches, levels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('plots/'+plotname+'-income-pie.png', bbox_inches='tight')
    plt.close()
