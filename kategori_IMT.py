def kategori_imt(imt, gender):
    if gender == 'Laki-Laki':
        if imt < 20 :
            return 'Kurus'
        elif 20 <= imt < 25 :
            return 'Normal' 
        elif 25 <= imt < 30:
            return 'Gemuk'
        else:
            return 'Obesitas'
        
    if gender == 'Perempuan':
        if imt < 18.5 :
            return 'Kurus'
        elif 18.5 <= imt < 25 :
            return 'Normal' 
        elif 25 <= imt < 30:
            return 'Gemuk'
        else:
            return 'Obesitas'