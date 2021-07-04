class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__local = None

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local(self) -> None:
        endereco = self.__local.buscar_endereco()
        print(endereco)

    def salvar_local(self, local: any) -> None:
        self.__local = local

    def buscar_local(self) -> any:
        return self.__local

    def se_apresentar(self) -> None:
        print("Ola, eu sou {}".format(self.__nome))
