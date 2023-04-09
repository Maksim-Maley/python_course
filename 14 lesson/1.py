class communication ():
    def priv(self):
        self.privet = "Hello"

    def question(self):
        self.ques = "?"

    def answer(self):
        self.ans = "ok"
    
    def poka(self):
        print("Пока")

class Humen(communication):
    def privetstvie(self):
        print(format(self.privet))
    def PriVet(self, otvet):
        self.privet = otvet
        print(otvet)

    def quest(self):
        print(format(self.ques))
    def QuesT(self, otvet1):
        self.QeSt = otvet1
        print(otvet1)

    def Answer(self):
        print(format(self.ques))
    def AnS(self, otvet2):
        self.AnSwer = otvet2
        print(otvet2)

    def poka(self):
        print("Пока инопланетянин")

class Aliens(communication):
    def privetstvie(self):
        print(format(self.privet))
    def PriVet(self, otvet):
        self.privet = otvet
        print(otvet)

    def quest(self):
        print(format(self.ques))
    def QuesT(self, otvet1):
        self.QeSt = otvet1
        print(otvet1)

    def Answer(self):
        print(format(self.ques))
    def AnS(self, otvet2):
        self.AnSwer = otvet2
        print(otvet2)
    
    def poka(self):
        print("Пока человек")

c = Humen()
c.PriVet("Привет")
c.privetstvie
    
a = Aliens()
a.PriVet("#%$^!)@")
a.privetstvie

c.QuesT("Что?")
c.quest

a.QuesT("Пр*в№т")
a.quest

c.AnS("Понятно, скажи еще раз")
c.Answer

a.AnS("Привет")
a.Answer

c.poka()

a.poka()
