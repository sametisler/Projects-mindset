import math

volt = float(input("Lütfen voltaj değerini giriniz."))
hertz = float(input("Lütfen hertz değerini giriniz."))
direnc = float(input("Lütfen direnç değerini giriniz."))
fahrad = float(input("Lütfen kondansatör değerini giriniz."))
henry = float(input("Lütfen bobin değerini giriniz."))

def emp(v = volt, h= hertz, r = direnc, f = fahrad, b = henry):
    xl = 2*(math.pi)*h*b
    xc = (2*(math.pi)*h*f)**-1
    z = complex(r,(xl-xc))
    print(round(abs(z),2))
    
emp()
