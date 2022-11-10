import pygame

AtilanPara = 0
Hedef = 0
durum = True

while durum == True :

    print("İşlem seçiniz\n--------------\n1: Hedef Seç(1 Kez)\n2: Para At\n3: Para Çıkar\n4: Kaç Para Atıldığını Gör\n5: Hedefe Kaç Para Kaldığını Gör")
    secim = int(input("İşlem :"))

    if secim == 1 :
        Hedef =int(input("Hedef Giriniz :"))
        print("Hedef Oluşturuldu")


    elif secim == 2 and Hedef > 0 :
        AtilacakPara =int(input("Atılacak Para Miktarı :"))
        AtilanPara += AtilacakPara


    elif secim == 3 :
        print(AtilanPara , "Liranız Var")
        CikarilacakPara =int(input("Çıkarılacak Para :"))
        AtilanPara-= CikarilacakPara


    elif secim == 4 :
        print(AtilanPara)


    elif secim == 5 :
        HedefeKalanPara = Hedef-AtilanPara
        print(HedefeKalanPara)


    else :
        durum = False




