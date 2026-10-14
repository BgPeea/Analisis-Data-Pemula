# LEVEL 3: FORECASTING
import pandas as pd

df = pd.read_excel("anvragh_cleaned.xlsx")
hari_map = {"20-22 Agt": 3, "23-26 Agt": 4, "27-29 Agt": 3}
df['Hari'] = df['Periode'].map(hari_map)

total_hari = df['Hari'].sum()
honor_per_hari = df[df['Kategori']=='HONOR']['Jumlah'].sum() / total_hari
konsumsi_per_hari = df[df['Kategori']=='KONSUMSI']['Jumlah'].sum() / total_hari

# Forecast 10 hari September
forecast_A = {
    "HONOR": honor_per_hari * 10,
    "KONSUMSI": konsumsi_per_hari * 10,
    "OBAT buffer": 65000 * 1.1,
    "BBM buffer": 220000,
}
forecast_A["TOTAL"] = sum(forecast_A.values())

print(f"Forecast Realistis: Rp {forecast_A['TOTAL']:,.0f}")
# Simpan
pd.DataFrame([forecast_A]).to_excel("forecast_september.xlsx")