#Merubah dari cm ke m dengan menggunakan komentar
def cm_ke_m(cm):
    return cm/100
#Hasil dari konvensi
Nilai_cm = float(input("masukkan nilai dalam cm: "))
Nilai_m =cm_ke_m(Nilai_cm)
print(f"{Nilai_cm} cm sama dengan {Nilai_m}m")