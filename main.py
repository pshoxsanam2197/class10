# 1-masala
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Nom: {self.title}, Muallif: {self.author}")

class Library(Book):
    def __init__(self,name, kitoblar = []):
        self.name = name
        self.kitoblar = kitoblar

    def kitob_qow(self, kitob):
        self.kitoblar.append(kitob)

    def library_info(self):
        print(f"{self.name} kutubxonasining kitoblari")
        for k in self.kitoblar:
            k.info()
        print()

b1 = Book("O'tgan kunlar", "Abdulla Qodiriy")
b2 = Book("Mehrobdan chayon", "Abdulla Qodiriy")
b3 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev")

roy = [b1, b2, b3]

kutubxona = Library("A.Navoiy", roy)
kutubxona.library_info()

#2-masala
class Student:
    def __init__(self, name, ball):
        self.name = name
        self.ball = ball

    def info(self):
        print(f"Nomi: {self.name}")
        print(f"Ball: {self.ball}")

class Group:
    def __init__(self,guruh_nomi, talabalar=[]):
        self.guruh_nomi = guruh_nomi
        self.talabalar = talabalar

    def talaba_qoshish(self, talaba):
        self.talabalar.append(talaba)

    def guruh_info(self):
        print(f"{self.guruh_nomi} guruhning nomi:")
        for t in self.talabalar:
            t.info()
            print()

s1 = Group("IT", 23)
s2 = Student("Ali", 85)
s3 = Student("Vali", 90)

roy = [s1, s2, s3]

talaba = Group("IT-23", roy)

talaba.guruh_info()
talaba.talaba_qoshish()
talaba.guruh_info()
