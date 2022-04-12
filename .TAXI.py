import math



print ( "      <<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>> ", "\n" )
print ( "                      Assalomu alaykum bizning RICH KHAN TAXI SERVICE online taxi xizmatimizga xush kelibsiz", "\n")
print ( "      --------------------------------------------------------------------------------", "\n" )
print ( "                      Sizga to'gri keladigan taksi turini tanlang  ", "\n" )
print ( "                       Ekanom  klass siz turgan manzilga borguncha 3$ va undan keyingi manzil kilometriga 1$ dan ")
print ( "                       Komfort  klass siz turgan manzilga borguncha 4$ va undan keyingi manzil kilometriga 1.8$ dan  ")
print ( "                       Biznes  klass siz turgan manzilga borguncha 5$ va undan keyingi manzil kilometriga 2.5$ dan ", "\n")
print ( "      <<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

print ( "Xizmat turini tanlang ", "\n", " Ekanom - 1", "\n", " Kamfort - 2 ", "\n", " Busines - 3 " )

a = int ( input ( " a = " ) )

if a == 1:
    print ( " Siz Ekanom tarifini tanladingiz : ", "\n", "3 $  chaqirish uchun  har kilometrga 1 $ dan")
    print ( " Kodinatangizni tanlang " )
    x = int ( input ( " x = " ) )
    y = int ( input ( " y = " ) )
    print ( f" sizning kordinatangiz {x} : {y}")
    print ( " Manzil kordinatasini tanlang : " )
    x_1 = int ( input ( " x_1 = " ) )
    y_1 = int ( input ( " y_1 = " ) )
    print ( f" sizning manzil kordinatangiz {x} : {y}")


    l = math.sqrt( math.fabs( x - x_1 )**2 + math.fabs( y - y_1 )**2 )
    k = 3 + l*1
    print ( f" Yo'l masofasi {l} va yo'l narxi {k} $ ")

    print ( " Xizmatni davom ettirilsinmi? ", "\n", " 1 - ha ", "\n", "2 - yo'q ")
    d = int ( input ( " d = " ) )
    if d == 1 :
        print ( " Taksimiz yaqin 20 minut ichida yetib boradi " )
    elif d == 2:
        print ( " Tashrifingiz uchun raxmat " )
    else :
        print ( " Siz noto'gri ma'lumot kiritdingiz " )




elif a == 2:
    print ( " Siz Komfort tarifini tanladingiz : ", "\n", "4 $   chaqirish uchun  har kilometrga 1.8 $ dan")
    print ( " Kodinatangizni tanlang " )
    x = int ( input ( " x = " ) )
    y = int ( input ( " y = " ) )
    print ( f" sizning kordinatangiz {x} : {y}")
    print ( " Manzil kordinatasini tanlang : " )
    x_1 = int ( input ( " x_1 = " ) )
    y_1 = int ( input ( " y_1 = " ) )
    print ( f" sizning manzil kordinatangiz {x} : {y}")

    l = math.sqrt( math.fabs( x - x_1 )**2 + math.fabs( y - y_1 )**2 )
    k = 4 + l*1.8
    print ( f" Yo'l masofasi {l} va yo'l narxi {k} $ ")


    print ( " Xizmatni davom ettirasizmi ", "\n", " 1 - ha ", "\n", "2 - yo'q ")
    d = int ( input ( " d = " ) )
    if d == 1 :
        print ( " Taksimiz yaqin 20 minut ichida yetib boradi " )
    elif d == 2:
        print ( " Tashrifingiz uchun raxmat " )
    else :
        print ( " Siz noto'gri malumot kiritdingiz " )











elif a == 3:
    print ( " Siz Business tarifini tanladingiz : ", "\n", "5 $  chaqirish uchun  har kilometrga 2.5 $ dan")
    print ( " Kodinatangizni tanlang " )
    x = int ( input ( " x = " ) )
    y = int ( input ( " y = " ) )
    print ( f" sizning kordinatangiz {x} : {y}")
    print ( " Manzil kordinatasini tanlang : " )
    x_1 = int ( input ( " x_1 = " ) )
    y_1 = int ( input ( " y_1 = " ) )
    print ( f" sizning manzil kordinatangiz {x} : {y}")


    l = math.sqrt( math.fabs( x - x_1 )**2 + math.fabs( y - y_1 )**2 )
    k = 5 + l*2.5
    print ( f" Yo'l masofasi {l} va yo'l narxi {k} $ ")


    print ( " Xizmatni davom ettirasizmi ", "\n", " 1 - ha ", "\n", "2 - yo'q ")
    d = int ( input ( " d = " ) )
    if d == 1 :
        print ( " Taksimiz yaqin 20 minut ichida yetib boradi " )
    elif d == 2:
        print ( " Tashrifingiz uchun raxmat " )
    else :
        print ( " Siz noto'gri malumot kiritdingiz " )