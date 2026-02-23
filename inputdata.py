def input_gender():
    while True: 
        gender = input("Masukkan gender (L/P): ").strip().upper()
        if gender == "L":
            return "Laki-laki"
        elif gender == "P":
            return "Perempuan"
        else:
            print("Input tidak valid! Masukkan L atau P.")

def input_berat(): 
    while True:
        try:
            berat = float(input("Masukkan berat badan (kg): "))
            if berat > 0:
                return berat
        except ValueError:
            print("Input harus berupa angka!")

def input_tinggi(): 
    while True:
        try:
            tinggi = float(input("Masukkan tinggi badan (cm): "))
            if tinggi > 0:
                return tinggi
        except ValueError:
            print("Input harus berupa angka!")
