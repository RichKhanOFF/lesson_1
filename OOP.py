# # Class bilan ishlash uchun birinchi misol
# class Mashinalar:
#     def __init__(self):
#         print("Nimadir")
#
#     def nima(self):
#         return "Salom OOP"
#
#     def nima1(self):
#         return "NIMADIR1"
#
# x = Mashinalar()
# print(x.nima())
# print(x.nima1())

#
# class Mashina:
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color
#         self.year = year
#
#     def matiz(self):
#         return (f"1-Mashina nomi: {self.name}\n1-Mashina rangi: {self.color}\n1-Mashina yili: {self.year}")
#     def cobalt(self):
#         return (f"2-Mashina nomi: {self.name}\n2-Mashina rangi: {self.color}\n2-Mashina yili: {self.year}")
#
# x = Mashina("Matiz", "Sariq", 2022)
# y = Mashina("Cobalt", "Qora", 2017)
#
# print(x.matiz())
# print()
# print()
# print(y.cobalt())

#
# class Telefonlar:
#     def __init__(self, name, color, year, money):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.money = money
#
#     def Telephone_information(self):
#         return (f"Telefon nomi: {self.name}\nTelefon rangi: {self.color}\nTelefon yili: {self.year}\nTelefon narxi: {self.money}")
#
# x = Telefonlar("POCO X3 PRO", "GOLD", 2022, "300$")
# y = Telefonlar("REDMI NOTE 10", "GREEN", 2022, "200$")
# v = Telefonlar("REDMI NOTE 9", "BLUE", 2021, "170$")
# b = Telefonlar("SAMSUNG A20", "RED", 2019, "170$")
#
# print("                                       ASSALOMU ALAYKUM BIZNING ONLINE DO`KONIMIZGA XUSH KELIBSIZ!!!")
# print()
# print()
# print(x.Telephone_information())
# print()
# print()
# print(y.Telephone_information())
# print()
# print()
# print(v.Telephone_information())
# print()
# print()
# print(b.Telephone_information())
# print()
# print()




# class Telefonlar:
#     client_sum = int(input("Pulingizni kiriting: "))
#     def __init__(self, name, color, year, money):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.money = money
#
#     def Car_information(self):
#         return (f"Qimmat mashina\nMashina nomi: {self.name}\nMashina rangi: {self.color}\nMashina yili: {self.year}\nMashina narxi: {self.money}")
#     def Car_info(self):
#         if self.money > self.client_sum:
#             return (f"Qimmat mashina\nMashina nomi: {self.name}\nMashina rangi: {self.color}\nMashina yili: {self.year}\nMashina narxi: {self.money}")
#
# x = Telefonlar("Matiz", "Oq", 2003, "10")
# y = Telefonlar("Spark", "Qora", 2017, "20")
#
# print()
# print()
# print(x.Car_info())
# print()
# print()
# print(y.Car_info())
# print()
# print()




class Matn:
    def __init__(self, word, name):
        self.word = word
        self.name = name
        self.age = 19

    def uzunlik(self):
        s = 0
        for i in self.word:
            s +=1
        return s

    def nimadir(self):
        return f"({self.name} {self.age})"






