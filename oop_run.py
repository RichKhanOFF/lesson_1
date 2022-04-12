# from  oop_yak import Odam, Quruvchi, Dasturchi
#
#
# odam1 = Odam("Sarvar", 13)
# quruvchi1 = Quruvchi()
# dasturchi = Dasturchi("nimadir", 13, 5)
# print(odam1.info())
# print()
# print(quruvchi1.info())
# print()
# print(dasturchi.info())
# print()
# print(dasturchi.info_2())









from oop_yak import  Person, Student, Quruvchi

odam1 = Person("Xumoyun", "To'xtayev", 2002)
odam2 = Person("Tohir", "Bozorov", 1991)
# print(odam1.name)
student = Student("Vali", "Valyev", 2003, 2, "TUTA")
quruvchi1 = Quruvchi("Eshmat", "Toshnatov", 1960, 40)

print(odam1.info())
print()
print(odam2.info())
print()
print(student.info())
print()
# print(student.degree)
# print()
# print(quruvchi1.get_staj(),"\n",quruvchi1.age)