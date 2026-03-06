def split_bill(tagihan_awal, jumlah_orang):
    pajak = 0.10
    total_akhir = tagihan_awal + (tagihan_awal * pajak)
    bayar_per_orang = total_akhir / jumlah_orang
    return total_akhir, bayar_per_orang
    
total, per_orang = split_bill(347500, 4)
print(f"Total setelah pajak: Rp {total:,.0f}")
print(f"Masing-masing bayar: Rp {per_orang:,.0f}")
