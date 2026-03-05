def estimasi_bbm(jarak, konsumsi_per_liter=40, harga_per_liter=13000):
    total_liter = jarak / konsumsi_per_liter
    total_biaya = total_liter * harga_per_liter
    return total_biaya

biaya = estimasi_bbm(180)
print(f"Total biaya bensin: Rp {biaya:,.0f}")