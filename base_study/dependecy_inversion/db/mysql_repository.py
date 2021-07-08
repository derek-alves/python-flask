from base_study.dependecy_inversion.db.interface_repository import RepositorioInterface


class MySqlRepositorio(RepositorioInterface):

    def inserir(self, dado: any) -> None:
        print("Inserindo {} no banco Mysql".format(dado))

    def deletar(self, dado: any) -> None:
        print("Removendo {} no banco Mysql".format(dado))
