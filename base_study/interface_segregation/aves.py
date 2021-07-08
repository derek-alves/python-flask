from interface import Ave, AveQueNaoVoa


class Canario(Ave):

    def comer(self):
        print("Estou comendo")

    def voar(self):
        print("Estou voando")

    def gritar(self):
        print("Estou gritando")


class Pinguim(AveQueNaoVoa):

    def comer(self):
        print("Estou comendo")
        self.__acasalar()

    def gritar(self):
        print("Estou gritando")

    def __acasalar(self):
        print("Agora vou acasalar .....")
