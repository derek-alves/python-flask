# Aplicação com o intuito de estudar docker + flask api

* Ferramentas
  * Flask
  * SQLAlchemy orm
  * docker

# Instalação via Docker

* Executando o banco de dados, api e web sem dedicar o terminal para o docker:
	```
	$ docker-compose up -d
	```

* **Nota:** Remova o -d para continuar no terminal do docker. **Caso ocorra algum problema em relação à conexão TCP/IP na porta 5432**, reinicie o container sem deletá-lo.

  * 1 - Encerrar todos os containers
 
    ```
    $ docker-compose down
    ```
  * 2 - Iniciar todos containers
    ```
    $ docker-compose start
    ```
  * 3 - Executar banco de dados, server e web novamente
    ```
    $ docker-compose up
    ```

* Encerrando o container sem estar no terminal do docker:
	```
	$ docker-compose stop
	```
* **Nota:** Caso esteja no terminal, utilize o comando ctrl+c.

* Com o docker-compose rodando, utilize o seguinte comando em um novo terminal:
  ```
  $ docker exec -it <id do container> sh
  ```
# Endpoints
* Base endpoint:
      ```
        http://localhost:3000
      ```

### Cadastrar um novo usuário
Endpoint: /
Method: POST

Request syntax:
```
{
    "name": String
}
```

Code 200 response syntax:
```
{
    "code": 200,
    {
      "message": string,
      
    }
}
```

### Retorn default
Endpoint: /
Method: GET

Code 200 response syntax:
```
{
    "code": 200,
    {
      "message": Ola, estou na aplicação
    }
}
```