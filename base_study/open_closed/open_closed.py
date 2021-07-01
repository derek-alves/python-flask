class Circo:
    def apresentar(self, apresentador: any) -> None:
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self) -> None:
        print("Malabarista apresentando show")


class Palhaco:
    def apresentar_show(self) -> None:
        print("Palhaço apresentando show")


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
