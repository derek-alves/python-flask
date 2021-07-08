from base_study.dependecy_inversion.db.interface_repository import RepositorioInterface


class MongoRepositorio(RepositorioInterface):

    def inserir(self, dado: any) -> None:
        print("Inserindo {} no banco Mongo".format(dado))

    def deletar(self, dado: any) -> None:
        print("Removendo {} no banco Mongo".format(dado))
