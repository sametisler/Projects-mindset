import math
is_on = True

while is_on:
    speed = float(input("Lütfen bir hiz değeri giriniz."))
    angle = float(input("Lütfen ° cinsinden bir eğim acisi değeri giriniz."))
    g = 10
    def egik_atis(v = speed,a = angle):
        menzil = ((v**2)/g) * (math.sin(math.radians(2*angle)))
        t_ucus = (v*(math.sin(math.radians(angle))))/ g * 2
        hmax = (g * ((t_ucus/2)**2)/2)
        print(f"{speed}m/s hızı ve {angle}° açısı ile atılan cismin;\nMaksimum menzili {round(menzil,2)}m.'dir.\nUçuş süresi {round(t_ucus,2)}s.'dir.\nMaksimum yüksekliği ise {round(hmax,2)}m'dir.")
    egik_atis()
    cont = input("Yeni bir hesaplama yapmak ister misiniz ?(evet / hayır)")
    if cont == "evet":
        is_on = True
    else:
        is_on = False
        print("Hoşçakalın.")
