import pandas as pd

df = pd.read_csv('HIST_PAINEL_COVIDBR_20ago2020_MT.csv')
print(df.columns)

# df_semana = df.groupby(['semanaEpi']).sum()
# print(df_semana.head())

