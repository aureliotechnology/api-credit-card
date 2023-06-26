# API Cartão de Crédito

API para manipulação de dados de cartões de crédito.

## Recursos

- Cadastro e gerenciamento de cartões de crédito.
- Verificação de validade dos dados do cartão.

## Tecnologias Utilizadas

Este projeto faz uso das seguintes tecnologias:

- **Django**
- **Django Rest Framework**
- **Django Rest Framework Simple JWT**
- **PostgreSQL**
- **Docker**
- **Docker Compose**
- **Pytest**
- **Arquitetura Hexagonal**


## Requisitos

- Docker
- Docker-compose

## Dependências

Este projeto utiliza as seguintes bibliotecas Python:

- [Django](https://www.djangoproject.com/) (4.2.2): Framework de alto nível para desenvolvimento web.
- [python-dateutil](https://dateutil.readthedocs.io/en/stable/) (2.8.2): Extensões para o módulo datetime do Python.
- [Django Rest Framework](https://www.django-rest-framework.org/) (3.14.0): Framework poderoso e flexível para construção de APIs web.
- [Django Rest Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) (5.2.2): Autenticação por tokens para Django Rest Framework.
- [psycopg2-binary](https://www.psycopg.org/docs/) (2.9.6): Adaptador PostgreSQL para Python.
- [pytest-django](https://pytest-django.readthedocs.io/en/latest/) (4.4.0): Um plugin para pytest que fornece um conjunto de ferramentas úteis para testar projetos Django.
- [pytest-factoryboy](https://pytest-factoryboy.readthedocs.io/) (2.1.0): Fixture de integração factory boy para pytest.
- [mixer](https://mixer.readthedocs.io/en/latest/) (7.2.1): Geração de dados aleatórios para seus testes.
- [model-bakery](https://model-bakery.readthedocs.io/en/latest/) (1.3.2): Biblioteca para criação de dados de teste no Django.
- [python-creditcard](https://github.com/maistodos/python-creditcard.git@main) (0.0.1) Biblioteca para validar os dados do cartão de credito.
Você pode instalar todas estas dependências de uma só vez utilizando o comando `pip install -r requirements.txt` no seu ambiente de desenvolvimento, mas se for usar o docker não se preocupe que tudo já esta prontinho.

## Instalação

Para instalar e configurar o projeto localmente, siga as etapas abaixo:

1. Clone o repositório:

```sh
$ git clone https://github.com/seu-usuario/api-cartao-de-credito.git
$ cd api-cartao-de-credito
$ docker-compose up
```
Agora você pode acessar a API pelo endereço http://localhost:8000

Se você não tiver o Docker instalado, consulte o Guia de instalação do Docker.

## Rotas da API

Aqui estão as principais rotas disponíveis na API:

- `POST /api/token/`: Obter token de acesso. Exemplo de corpo de requisição: 
```json
{ 
    "username": "admin", 
    "password": "admin" 
}
```
- `POST /api/token/refresh/`: Atualiza um token de acesso existente. Exemplo de corpo de requisição: 
```json
{ 
    "refresh": "seu-token-refresh" 
}
```
- `POST /api/creditcards/`: Cria um novo cartão de crédito. Espera receber no corpo da requisição um objeto JSON como este por exemplo.
```json
{
    "exp_date": "02/2026",
    "holder": "Fulano",
    "number": "4539578763621486",
    "cvv": "123"
}
```
- `GET /api/creditcards/`: Retorna uma lista de todos os cartões de crédito cadastrados.
- `GET /api/creditcards/{id}/`: Retorna os detalhes de um cartão de crédito específico.

Você pode usar a ferramenta de sua escolha para enviar requisições HTTP para a API, como cURL, Postman ou qualquer outra.

Lembre-se de que todas as rotas exigem autenticação. Para obter um token, faça uma requisição para o endpoint `api/token/` com seu nome de usuário e senha. Inclua o token nas requisições para as rotas da API no cabeçalho 'Authorization' no formato 'Bearer {seu-token}'.

Nota: Substitua `{id}` pelo ID do cartão de crédito.

## Licença

Este projeto está licenciado sob os termos da [MIT License](https://opensource.org/licenses/MIT).

## Considerações finais

Agradeço a atenção de olhar meu projeto, fico a disposição para qual quer sugestão de melhoria.

---

Feito por Aurélio Moreira.

