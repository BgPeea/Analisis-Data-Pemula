import pandas as pd

df = pd.read_excel("anvragh_cleaned.xlsx")

# Tambah kolom Hari
hari_map = {"20-22 Agt": 3, "23-26 Agt": 4, "27-29 Agt": 3}
df['Hari'] = df['Periode'].map(hari_map)
df['Biaya_per_Hari'] = df['Jumlah'] / df['Hari']

# PIVOT TABLE 1: Periode vs Kategori
pivot1 = pd.pivot_table(df, values='Jumlah', 
                        index='Periode', 
                        columns='Kategori', 
                        aggfunc='sum', 
                        fill_value=0, margins=True, margins_name='TOTAL')
print(pivot1)

# PIVOT TABLE 2: Biaya harian
pivot2 = pd.pivot_table(df, values='Biaya_per_Hari', 
                        index='Kategori', 
                        columns='Periode', 
                        aggfunc='sum', fill_value=0)
print(pivot2)