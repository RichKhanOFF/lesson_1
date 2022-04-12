print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
print ( " Assalomu alaykum hurmatli mijoz '\n' RICH KHAN SHOP  Onlayn do'konimizga hush kelibsiz : " )
print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
print ( " Bizning Saytimiz orqali istalgan telefoningizni sotib olishingiz mumkin : ")
print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
print ( " Brend nomini tanlang : ")
print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
print ( " 1 - Samsung", "\n", "2 - IPHONE", "\n", "3 - Xiaomi")
print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

a = int ( input ( " Brend raqamini tanlang : " ) )
print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )


if a == 1:
    print ( " Samsung brendini tanlaganingiz uchun tashakkur ", "\n", "Qaysi rusumini tanlamoqchisiz ")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
    print ( " 1. Samsung A12 ", "\n", "2. Samsung A22", "\n", "3. Samsung A32 ")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    b = int ( input ( " Tanlagan rusumingiz raqamini kiriting : " ) )
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    if b == 1:
        print ( " Samsung A12 smartfoni tanlaganingiz uchun tashakkur. Narxi 1800000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((1800000 - e) + (1800000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((1800000 - e) + (1800000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    elif b == 2:
        print ( " Samsung A22 smartfoni tanlaganingiz uchun tashakkur. Narxi 2500000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((2500000 - e) + (2500000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((2500000 - e) + (2500000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )



    elif b == 3:
        print ( " Samsung A32 smartfoni tanlaganingiz uchun tashakkur. Narxi 3200000 : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((3200000 - e) + (3200000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((3200000 - e) + (3200000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        
    else :
        print ( " Noto'g'ri malumotni kiritdingiz : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )















elif a == 2:
    print ( " IPHONE brendini tanlaganingiz uchun tashakkur ", "\n", "Qaysi rusumini tanlamoqchisiz ")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
    print ( " 1. IPHONE 13 pro", "\n", "2. IPHONE 13 pro max")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    b = int ( input ( " Tanlagan rusumingiz raqamini kiriting : " ) )
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    if b == 1:
        print ( " IPHONE 13 pro smartfoni tanlaganingiz uchun tashakkur. Narxi 15 000 000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((15000000 - e) + (15000000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((15000000 - e) + (15000000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )



    elif b == 2:
        print ( " IPHONE 13 pro max smartfoni tanlaganingiz uchun tashakkur. Narxi 18 000 000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((18000000 - e) + (18000000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((18000000 - e) + (18000000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            else :
                print ( " Noto'g'ri malumotni kiritdingiz : " )
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        else :
            print ( " Noto'g'ri malumotni kiritdingiz : " )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )


    else :
        print ( " Noto'g'ri malumotni kiritdingiz : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )








elif a == 3:
    print ( " Xiaomi brendini tanlaganingiz uchun tashakkur ", "\n", "Qaysi rusumini tanlamoqchisiz ")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
    print ( " 1. Xiaomi note 9", "\n", "2. Xiaomi note 9 plus")
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    b = int ( input ( " Tanlagan rusumingiz raqamini kiriting : " ) )
    print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

    if b == 1:
        print ( " Xiaomi note 9 tanlaganingiz uchun tashakkur. Narxi 2 500 000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((2500000 - e) + (2500000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((2500000 - e) + (2500000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )



    elif b == 2:
        print ( " Xiaomi note 9 plus smartfoni tanlaganingiz uchun tashakkur. Narxi 3 000 000 so'm : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
        print ( " To'lov usulini tanlang : ", "\n" )
        print ( " 1. Naqt  ", "\n", "2. Kredit ")
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        c = int ( input ( " Tanlagan rangingizni kiriting : " ) )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        if c == 1:
            print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        elif c == 2:
            print ( " Muddatni kiriting " )
            print ( " 1. 1 yilga 20 %", "\n", "2. 2 yilga 30 %", "\n")
            d = int ( input ( "Muddatni kiriting : " ) )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            if d == 1:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((3000000 - e) + (3000000 - e)*0.2)/12
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 12 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            elif d == 2:
                e = int ( input ( " Boshlang'ich to'lov limitni kiriting: ") )
                f = ((3000000 - e) + (3000000 - e)*0.3)/24
                print ( f"Hurmatli mijoz {e} so'm toladingiz {f} so'mdan 24 oy to'laysiz ")
                print (" To'lovni amalga oshiring ", "\n", "1 hafta ichida buyurtmangiz yetkaziladi ")
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )
            else :
                print ( " Noto'g'ri malumotni kiritdingiz : " )
                print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )

        else :
            print ( " Noto'g'ri malumotni kiritdingiz : " )
            print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )


    else :
        print ( " Noto'g'ri malumotni kiritdingiz : " )
        print ( "\n", "<<<<<<<<<<<<<<<<<<<<************************************>>>>>>>>>>>>>>>>>>>>", "\n" )


















































































# elif a == 3:
#     print ( " <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", "\n")
#     print ( " Texnikalar bo'limimizga hush kelibsi : ", "\n" )
#     print ( " <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", "\n")

#     print ( "1 - Samsung ", "\n" "2 - Artel ", "\n" , "3 - Shivaki ", "\n"  )
#     print ( " <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", "\n")
#     b = int ( input ( " Brendni tanlang : "))
#     print ()
#     if b == 1 :
#         print ( " Samsung bo'limimizga xush kelibsiz", "\n", " Bizdagi samsung mahsulotlari " )
       

#     elif b == 2 :
#         print ( " 1 ta Tesha narxi 20000 ming ", "\n" " va yrtkazib berish narxi 8000 ming ", "\n" )





#     elif b == 3 :
#         print ( " 1 ta ollta narxi 40000 ming ", "\n" " va yrtkazib berish narxi 8000 ming ", "\n" )
        


#     elif b == 4 :
#         print ( " 1 ta Ketmon narxi 45000 ming ", "\n" " va yetkazib berish narxi 8000 ming ", "\n" )
    

    
#         else :
#             print ( " Siz malum bo'lmagan malumot turini tanladingiz")
#     else :
#         print ( " Siz malum bo'lmagan malumot turini tanladingiz")













