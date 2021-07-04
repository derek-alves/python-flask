
class Casa:
    def __init__(self) -> None:
        self.__endereco = "Rua dos Limoeiros"
        self.__proprietario = None

    def acender_luzes(self) -> None:
        print("Estou acendendo as luzes")

    def buscar_endereco(self) -> None:
        return self.__endereco

    def salve_proprietario(self, proprietario: any) -> None:
        self.__proprietario = proprietario

    def buscar_proprietario(self) -> any:
        return self.__proprietario
