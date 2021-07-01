class Repositorio:
    def select(self, db_connection: any) -> None:
        conection = db_connection.connectar()
        print("conectei ao banco {}".format(conection))
        print("fazendo um SELECT * FROM...")
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:

        conection = db_connection.connectar()
        print("conectei ao banco {}".format(conection))
        print("fazendo um Insert * FROM...")
        db_connection.desconectar()