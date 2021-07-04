from repositorio import Repositorio
from databases import PostgresDB

db_conn = PostgresDB()

repo = Repositorio()
repo.insert(db_conn)
repo.select(db_conn)
