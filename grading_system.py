import pandas as pd

class ogrenci():
    ogrenci_isim = []
    ogrenci_durum = []
    ogrenci_detay = []
    ogrenci_dfList = []

    def __init__(self, isim, no, vize, final):
        self.isim = isim
        self.no = no 
        self.vize = vize
        self.final = final
        
        ortalama = ogrenci.ortalama_hesaplama(vize, final)
        durum = ogrenci.durum_sorgula(ortalama)
        
        self.ogrenci_detay.append([isim,str(no),str(ortalama),str(durum)])
        self.ogrenci_dfList.append([isim,str(durum)])
        self.ogrenci_isim.append(isim)
        self.ogrenci_durum.append(durum)
               
        # print (' '.join(self.ogrenci_detay[0]))

    def ortalama_hesaplama(vize, final):
        sonuc = float(vize)*(4/10) + float(final)*(6/10)
        return sonuc

    def durum_sorgula(ort):
        if(ort >=90):
            # print("Harf Notu: AA, Tebrikler, dersi geçtiniz.")
            status = "Geçti"
        elif(ort>=85):
            # print("Harf Notu: BA, Tebrikler, dersi geçtiniz.")
            status = "Geçti"
        elif(ort>=80):
            # print("Harf Notu: BB, Tebrikler, dersi geçtiniz.")
            status = "Geçti"
        elif(ort>=75):
            # print("Harf Notu: CB, Tebrikler, dersi geçtiniz.")
            status = "Geçti"
        elif(ort>=70):
            # print("Harf Notu: CC, Tebrikler, dersi geçtiniz. ")
            status = "Geçti"
        elif(ort>=65):
            # print("Harf Notu: DC, Tebrikler, dersi geçtiniz.")
            status = "Geçti"
        elif(ort>=60):
            # print("Harf Notu: DD, Dersten şartlı geçtiniz.")
            status = "Kaldı"
        elif(ort<55):
            # print("Harf Notu: FF, Dersten kaldınız. Tekrar alınız" )
            status = "Kaldı"
        return status

# ogrenci("Su","787887", "50", "40") 

kontrol = "d"
while kontrol == "d": 
    isim, no, vize, final = input("Sıralı bir şekilde İsim, Numara, Vize ve Final Notunu Giriniz:").split(",")
    ogrenci(isim,no,vize,final)
    kontrol = input("Ekleme yapmaya devam etmek için 'd' harfini giriniz:") #d ye basılmadığında işlem sonucunu döndürür. d =devam


# for detay in ogrenci.ogrenci_detay:
#     print((detay))

# list = [['su', 'Geçti'], ['firat', 'Geçti']]
# df = pd.DataFrame(ogrenci)


df = pd.DataFrame(list(zip(ogrenci.ogrenci_isim, ogrenci.ogrenci_durum)),
               columns =['İsim', 'Durum'])

print(df)

df.to_excel("output.xlsx")
