## Empedans Projesi_v2

import math #math kutuphanesi yuklenmistir.

print("Empedans hesaplamak için lütfen istenen değerleri giriniz.")

volt = float(input("Lütfen voltaj değerini giriniz.")) # Veri girişi.
hertz = float(input("Lütfen hertz değerini giriniz.")) # Veri girişi.
direnc = float(input("Lütfen direnç değerini giriniz.")) # Veri girişi.
fahrad = float(input("Lütfen kondansatör değerini giriniz.")) # Veri girişi.
henry = float(input("Lütfen bobin değerini giriniz.")) # Veri girişi.

def emp(v= volt, h= hertz, r= direnc, f= fahrad, b= henry): # Yalnızca seri bağlı devrelerde empedans hesabı yapan bir fonksiyon tanımlama.
    """
    The parameters of the function is defined below:
    v = volt,
    h = hertz,
    r = resistance
    b = inductance
    This function gets the v, h, r, f, b values and returns impedance of the circuit...
    """
    xl = 2*(math.pi)*h*b # Endüktif reaktans hesaplar.
    xc = (2*(math.pi)*h*f)**-1 # Kapasitif reaktans hesaplar.
    z = complex(r,(xl-xc)) # Toplam empedans hesaplar
    print(round(abs(z),2)) # Sonucu 2 ondalıklı olarak ekrana yazar.
    
emp(volt, hertz, direnc, fahrad, henry) # Öncelikle kodu  emp(v, h, r, f, b) yazdım ve hata aldım. 
# Biraz araştırma yaptıktan sonra parametrelere atanan değişkenleri buraya emp() içine gerektiğini farkettim ve düzelttim.




