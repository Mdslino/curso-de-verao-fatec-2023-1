# Curso de Verão 2023/1 Fatec São José dos Campos

## Rastreabilidade e Observabilidade

## Objetivo

Esse repositório foi utilizado como artefato para exemplificar um sistema em execução com cobertura de um
sistema de observabilidade.

## Softwares utilizados

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Elasticsearch](https://www.elastic.co/pt/elasticsearch/)
- [Kibana](https://www.elastic.co/pt/kibana/)
- [Heartbeat](https://www.elastic.co/pt/beats/heartbeat)
- [Elastic APM](https://www.elastic.co/pt/apm)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Como executar

Primeiramente, é necessário ter o Docker e o Docker Compose instalados na máquina.

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Após a instalação, basta executar o comando abaixo na raiz do projeto:

```bash
docker-compose up -d
```

## Como acessar

- [Kibana](http://localhost:5601/)
- [Heartbeat](http://localhost:5601/app/uptime)
- [Elastic APM](http://localhost:5601/app/apm)
- [Flask](http://localhost:8000/)

As páginas da aplicação web são:

- [Home](http://localhost:8000/)
- [Cadastro](http://localhost:8000/auth/signup)
- [Login](http://localhost:8000/auth/login)
- [TODO](http://localhost:8000/todo)
