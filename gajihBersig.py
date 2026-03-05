def hitung_gaji_bersih(gapok, tunjangan):
    bruto = gapok + tunjangan
    potongan = (bruto * 0.02) + (bruto * 0.05) 
    gaji_bersih = bruto - potongan
    return gaji_bersih


hasil_gaji = hitung_gaji_bersih(5000000, 750000)
print(f"Gaji Bersih Karyawan: Rp {hasil_gaji:,.0f}")