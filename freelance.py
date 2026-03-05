def freelance():
    print("\n=== Konversi Waktu Freelance ===")
    jam = int(input("Masukkan jam kerja: "))
    menit = int(input("Masukkan menit kerja: "))
    upah_per_jam = float(input("Masukkan upah per jam: "))
    
    total_jam = jam + (menit / 60)
    total_bayar = total_jam * upah_per_jam
    
    print("Total jam (desimal):", total_jam)
    print("Total bayaran:", total_bayar)