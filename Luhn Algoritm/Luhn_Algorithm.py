credit_card = []
total = []
control = 0

print("""
############################################################################################################
Bu program, sadece Visa/Master ve American Express kredi kartlarınızın geçerli olup olmadığını kontrol eder.
############################################################################################################
""",flush=True)

card_number = input("Lütfen kredi kartı numaranızı tuşlayınız.")


if len(str(card_number)) == 16:                             # Visa/Master'a göre algoritma hesaplanır.
    for num in card_number:
        credit_card.append(int(num))                        # Kredi kartı numaraları bir listeye kaydedilir.
    for multiplied in range (0,len(credit_card),2):         # Listenin ilk elemanından sonra 1 er atlayarak bulunan elemanlar 2 ile çarpılır.
        if (credit_card[multiplied]*2)<10:
            total.append(credit_card[multiplied]*2)         # Çarpım sonucu elde ediken sayılar tek basamaklı ise doğrudan total listesine yazdırılır.
        else:
            for split in  str(credit_card[multiplied]*2):   # 2 basamaklı olan sayılar ise tek basamağa ayrılarak total listesine eklenir.
                total.append(int(split))
    for single in range (1,len(credit_card),2):             # Kredi kartındaki çarpılmayan sayılar doğrudan total listesine kaydolur.
        total.append(credit_card[single]) 
    for number in total:                                    # Total listesinin elemanları toplanır.
        control += number 
    if control % 10 == 0:
        print("Girdiğiniz kredi kartı geçerli bir Visa/Master kartıdır.")
    else:
        print("Girdiğiniz kredi kartı geçersizdir.")    
elif len(str(card_number)) == 15:                           # American exppress'e göre algoritma hesaplanır
    for num in card_number:                                 # Kredi kartı numaraları bir listeye kaydedilir.
        credit_card.append(int(num))
    for multiplied in range (1,len(credit_card),2):         # Listenin ikinci elemanından sonra 1 er atlayarak bulunan elemanlar 2 ile çarpılır.
        if (credit_card[multiplied]*2)<10:
            total.append(credit_card[multiplied]*2)         # Çarpım sonucu elde ediken sayılar tek basamaklı ise doğrudan total listesine yazdırılır.
        else:
            for split in  str(credit_card[multiplied]*2):   # 2 basamaklı olan sayılar ise tek basamağa ayrılarak total listesine eklenir.
                total.append(int(split))
    for single in range (0,len(credit_card),2):             # Kredi kartındaki çarpılmayan sayılar doğrudan total listesine kaydolur.
        total.append(credit_card[single])
    for number in total:                                    # Total listesinin elemanları toplanır.
        control += number
    if control % 10 == 0:
        print("Girdiğiniz kredi kartı geçerli bir  Amerikan Express kartıdır.")
    else:
        print("Girdiğiniz kredi kartı geçersizdir.")
else:
    print("Girdiğiniz kredi kartı geçersizdir.")

    
    