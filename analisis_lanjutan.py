
# ==============================================
# LEVEL 2: PIVOT TABLE + BIAYA HARIAN
# File: anvragh_cleaned.xlsx
# ==============================================
import pandas as pd
import matplotlib.pyplot as plt

# 1. Baca data clean
df = pd.read_excel("anvragh_cleaned.xlsx")

# 2. Tambah kolom Hari (dari Periode) -> ini kunci untuk hitung efisiensi
hari_map = {"20-22 Agt": 3, "23-26 Agt": 4, "27-29 Agt": 3}
df['Hari'] = df['Periode'].map(hari_map)

# Hitung biaya per hari
df['Biaya_per_Hari'] = df['Jumlah'] / df['Hari']

# Hitung berapa orang di setiap Rincian (2 Orang, 3 Orang, atau 1)
def hitung_orang(rincian):
    if "2 Orang" in rincian: return 2
    if "3 Orang" in rincian: return 3
    return 1

df['Jumlah_Orang'] = df['Rincian'].apply(hitung_orang)
df['Biaya_per_Orang_per_Hari'] = df['Biaya_per_Hari'] / df['Jumlah_Orang']

print("Data + Biaya Harian:")
print(df.head(10))

# 3. PIVOT TABLE - ini yang paling dipakai di kerjaan data analyst
# Pivot 1: Lihat komposisi biaya per Periode
pivot1 = pd.pivot_table(df, values='Jumlah', index='Periode', columns='Kategori', 
                        aggfunc='sum', fill_value=0, margins=True, margins_name='TOTAL')
print("\n=== PIVOT Periode vs Kategori ===")
print(pivot1)

# Pivot 2: Lihat biaya harian (biar tau periode mana yang paling boros per hari)
pivot2 = pd.pivot_table(df, values='Biaya_per_Hari', index='Kategori', 
                        columns='Periode', aggfunc='sum', fill_value=0)
print("\n=== PIVOT Biaya per Hari ===")
print(pivot2)

# 4. Analisis Honor - paling konsisten
honor_df = df[df['Kategori']=='HONOR']
print("\n=== Honor per Orang per Hari (konsisten!) ===")
print(honor_df[['Periode','Rincian','Jumlah','Biaya_per_Orang_per_Hari']])

# 5. Grafik Stacked (komposisi biaya per periode)
pivot_plot = pd.pivot_table(df, values='Jumlah', index='Periode', columns='Kategori', aggfunc='sum', fill_value=0)
pivot_plot.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Komposisi Biaya per Periode')
plt.ylabel('Rupiah')
plt.xticks(rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("chart_stacked.png")

# Grafik Trend Harian
biaya_harian_total = df.groupby('Periode')['Jumlah'].sum() / df.groupby('Periode')['Hari'].first()
biaya_harian_total.plot(marker='o', figsize=(8,5))
plt.title('Trend Biaya Harian Total')
plt.ylabel('Rupiah / Hari')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_trend_harian.png")

# 6. Simpan ke Excel Lanjutan
with pd.ExcelWriter("analisis_lanjutan_borbor.xlsx") as writer:
    df.to_excel(writer, sheet_name='Data Lengkap', index=False)
    pivot1.to_excel(writer, sheet_name='Pivot Periode vs Kategori')
    pivot2.to_excel(writer, sheet_name='Pivot Biaya Harian')

print("\nSelesai! File analisis_lanjutan_borbor.xlsx tersimpan.")
