from input_data import input_gender, input_berat, input_tinggi
from converterAndHitungImt import cmToMeter, hitungImt
from kategori_IMT import kategori_imt
from output import tampilkan_hasil

def main():
    Gender = input_gender()
    Berat = input_berat()
    Tinggi_cm = input_tinggi()

    Tinggi_m = cmToMeter(Tinggi_cm)
    IMT = hitungImt(Berat, Tinggi_m)
    Kategori = kategori_imt(IMT, Gender)

    tampilkan_hasil(Gender, Berat, Tinggi_cm, IMT, Kategori)
if __name__ == "__main__":

    main()


