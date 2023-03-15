## Eğik Atış Projesi_v2

import math
is_on = True

def egik_atis(v, a):
    """
    Bu fonksiyon aşağıdaki parametreleri kullanir:
    v = hiz,
    a = aci
    Fonksiyon bu verilerle eğik atis yapilan bir cismin maksimmum yüksekliğini, menzilini ve ucus suresini hesaplar.
    """
    g = 10 # g degeri 10 olarak kabul edilmiştir.
    menzil = ((v**2)/g) * (math.sin(math.radians(2*a))) # maksimum menzili hesaplar.
    t_ucus = (v*(math.sin(math.radians(a))))/ g * 2 # ucus suresini hesaplar.
    hmax = (g * ((t_ucus/2)**2)/2) # maksimum yuksekligi hesaplar.
    print(f"{v}m/s hizi ve {a}° acisi ile atilan cismin;\nMaksimum menzili {round(menzil,2)}m.'dir.\nUcus süresi {round(t_ucus,2)}s.'dir.\nMaksimum yuksekliği ise {round(hmax,2)}m'dir.")

while is_on: # Bu dongu ile kullanıcıya istedigi kadar hesaplama yapma sansi taninmistir.
    speed = float(input("Lütfen bir hiz değeri giriniz.")) # Veri girisi.
    angle = float(input("Lütfen ° cinsinden bir egim acisi değeri giriniz.")) # Veri girisi.
    egik_atis(speed,angle)
    cont = input("Yeni bir hesaplama yapmak ister misiniz ?(evet / hayir)") # Kullaniciya yeni bir hesaplama yapmak isteyip istemedigi sorulmaktadir.
    if cont == "evet":
        is_on = True
    else:
        print("Hoscakalin.")
        break