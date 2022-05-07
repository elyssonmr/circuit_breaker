Apresentação sobre Circuit Breaker
==================================


Como rodar?
-----------

A apresentação é divida em um docker-compose para subir as applicações que exemplificam a apresentação.

Considerando que o `docker` e o `docker compose` estejam instalados use o comando:

`docker-compose up -d`

Para rodar o teste, garanta que você tenha o python instalado. Primeiro instale a dependências do projeto através do comando:

`pip install -r requirements.txt`

Após rode o comando do locust abaixo:

`locust -f locust_test.py --host=https://localhost:8000`


Abra o seu navegador no endereço que o comando do Locust irá lhe informar e escolha com quantos usuários deseja executar os testes e quando usuários por segundo serão serão criados para os testes.


A apresentação esta disponivel online em [http://elyssonmr.com/presentations/circuit_breaker](http://elyssonmr.com/presentations/circuit_breaker/) ou dentro da pasta `presentation` abrindo o `index.html` no seu navegador
