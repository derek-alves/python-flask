class Mae:
    def __init__(self) -> None:
        self.endereco = "Rua do Balcao"
        self.sobrenome = "Silva"

    def comer(self) -> None:
        print("Estou comendo !!!")

    def estudar(self) -> None:
        print("Estou estudando :D")


class Filha(Mae):
    def __init__(self) -> None:
        super().__init__()


clara = Filha()
clara.estudar()
