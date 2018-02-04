import pandas as pd

# years of data available
years = ['1996_97', '1997_98', '1998_99', '1999_00', '2000_01', '2001_02',
        '2002_03', '2003_04', '2004_05', '2005_06', '2006_07', '2007_08',
        '2008_09', '2009_10', '2010_11', '2011_12', '2012_13', '2013_14',
        '2014_15', '2015_16']

# read in useful column names, prep for remapping to developer names
colnms = pd.read_excel('./data/useful_columns.xlsx')
col_list = list(colnms['VARIABLE NAME'].dropna())
col_names = list(colnms['developer-friendly name'].dropna())
namemap = dict(zip(col_list, col_names))

# iterate over the years
for year in years:
    df = pd.read_csv('./rawdata/MERGED'+year+'_PP.csv',header=0)
    df = df[col_list]
    df.rename(columns=namemap, inplace=True)
    df.to_csv('data/'+year+'_clean.csv', header=True, index=False)
    print(year)
