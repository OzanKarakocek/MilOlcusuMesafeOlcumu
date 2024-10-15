print("Mil Mesafe Ölçü Çeviriciye Hoş Geldiniz")

print("Metrik Ölçüler\n Kilometre(km)\n Metre(m)\n Desimetre(dm)\n Santimetre(cm)\n Milimetre(mm)\n Mikrometre(µm)\n Nanometre(nm)\n Angstrom(Å)")
print("İngiliz/Amerika Ölçüler\n League\n Mil(mi)\n Furlong\n Zincir\n Rod(rd)\n Yarda(yd)\n Foot(ft)\n Link\n El(Hand)\n İnç(inç)\n Çizgi\n Milİnç(mil)\n Thou(thou)")
print("Deniz Ölçüler\n Deniz Mili\n Fathom")
print("Astronomik Ölçüler\n Parsec(pc)\n Işık Yılı\n Astronomik Ünite(AE)\n Işık Dakikası\n Işık Saniyesi")

birkm=1.609344
birmetre=1.609344
birdesimetre=16.09344
birsantimetre=160.9344
birmilimetre=1.609344
birmikrometre=1609344000
birnanometre=1.609344000000
birangstrom=16.093440000000

birleague=0.3333333
birmil=1
birfurlong=8
birzincir=80
birrod=320
biryard=1.760
birfoot=5.280
birlink=8.000
birel=15.840
birinc=63.360
bircizgi=633.600
birmilinc=63.360000
birthou=63.360000

birdenizmili=0.8689762
birfathom=880

birparsec=0.000000000000052155282
birisikyili=0.0000000000001701078
birastronomikunite=0.000000010757803
birisikdakikasi=0.000000089469935
birisiksaniyesi=0.0000054

olcu=input("Mil Ölçüsünü Dönüştürmek İstediğiniz Ölçü Birimini Seçiniz: ")
mil=input("Dönüştürmek İstediğiniz Mil Değerini Seçiniz: ")



if olcu==("Kilometre"):
        print(float(mil)*birkm , "Km'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Metre"):
        print(float(mil)*birmetre , "M'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Desimetre"):
        print(float(mil)*birdesimetre , "Dm'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Santimetre"):
        print(float(mil)*birsantimetre , "Cm'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Milimetre"):
        print(float(mil)*birmilimetre , "Mm'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Mikrometre"):
        print(float(mil)*birmikrometre , "μm'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Nanometre"):
        print(float(mil)*birnanometre , "Nm'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Angstrom"):
        print(float(mil)*birangstrom , "Å'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")

if olcu==("League"):
        print(float(mil)*birleague , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Mil"):
        print(float(mil)*birmil , "Mi'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Furlong"):
        print(float(mil)*birfurlong , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Zincir"):
        print(float(mil)*birzincir , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Rod"):
        print(float(mil)*birrod , "Rd'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Yarda"):
        print(float(mil)*biryard , "Yd'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Foot"):
        print(float(mil)*birfoot , "Ft'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Link"):
        print(float(mil)*birlink , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("El"):
        print(float(mil)*birel , "Hand'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("İnç"):
        print(float(mil)*birinc , "İn'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Çizgi"):
        print(float(mil)*bircizgi , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Milİnç"):
        print(float(mil)*birmilinc , "İnçMil'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Thou"):
        print(float(mil)*birthou , "Thou'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")

if olcu==("Deniz Mili"):
        print(float(mil)*birdenizmili , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Fathom"):
        print(float(mil)*birfathom , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")

if olcu==("Parsec"):
        print(float(mil)*birparsec , "Pc'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Işık Yılı"):
        print(float(mil)*birisikyili , "Mi'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Astronomik Ünite"):
        print(float(mil)*birastronomikunite , "Ae'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Işık Dakikası"):
        print(float(mil)*birisikdakikasi , "Mi'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")
elif olcu==("Işık Saniyesi"):
        print(float(mil)*birisiksaniyesi , "'dir")
        print("Uygulamayı Kullandığınız İçin Teşekkür Ederiz İyi Günler Dileriz")


