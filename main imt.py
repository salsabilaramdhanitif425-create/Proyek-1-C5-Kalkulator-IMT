from input_data import input_gender, input_berat, input_tinggi
from converterAndHitungImt import cmTometer
from hitung_imt import hitung_imt
from kategori_IMT import kategori_imt
from output import tampilkan_hasil

def main():
    Gender = input_gender()
    Berat = input_berat()
    Tinggi_cm = input_tinggi()

    Tinggi_m = cm_ke_meter(Tinggi_cm)
    IMT = hitung_imt(Berat, Tinggi_m)
    Kategori = kategori_imt(IMT, Gender)

    tampilkan_hasil(Gender, Berat, Tinggi_cm, IMT, Kategori)
if __name__ == "__main__":

    main()

