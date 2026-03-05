def kebutuhan_cat(panjang, lebar, tinggi):
   
    luas_dinding = 2 * (panjang + lebar) * tinggi
    

    liter_cat = luas_dinding / 10
    
    return luas_dinding, liter_cat

luas, kebutuhan = kebutuhan_cat(4, 3, 3)
print(f"Luas dinding yang akan dicat: {luas} m2")
print(f"Estimasi kebutuhan cat: {kebutuhan:.1f} Liter")