# ANALISIS BORBOR - VERSI SIMPLE UNTUK FILE CLEAN
import pandas as pd
import matplotlib.pyplot as plt

# 1. Baca file - INI YANG KEMARIN KETINGGALAN
df = pd.read_excel("anvragh_cleaned.xlsx")

# 2. Lihat isi
print(df.head())
print(f"\nTotal Biaya: Rp {df['Jumlah'].sum():,}")

# 3. Analisis per Kategori (yang kemarin error)
# Artinya: kelompokkan Kategori -> jumlahkan Jumlah -> urutkan terbesar
per_kategori = df.groupby("Kategori")["Jumlah"].sum().sort_values(ascending=False)
print("\n--- Per Kategori ---")
print(per_kategori)

# 4. Analisis per Periode
per_periode = df.groupby("Periode")["Jumlah"].sum()
print("\n--- Per Periode ---")
print(per_periode)

# 5. Analisis per Rincian / Orang
per_rincian = df.groupby("Rincian")["Jumlah"].sum().sort_values(ascending=False)
print("\n--- Per Rincian Top 5 ---")
print(per_rincian.head(5))

# 6. Bikin grafik
per_kategori.plot(kind='bar')
plt.title("Total per Kategori")
plt.ylabel("Rupiah")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("chart_kategori_simple.png")
print("\nGrafik disimpan!")