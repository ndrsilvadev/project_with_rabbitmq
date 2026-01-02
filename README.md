# RabbitMQ with Python (Producer & Consumer) / RabbitMQ com Python (Producer & Consumer)

RabbitMQ with Python (Producer & Consumer)
This project demonstrates a simple implementation of a Producer and Consumer using RabbitMQ, Python, and the Pika library, with configuration via environment variables.

Este projeto demonstra uma implementação simples de **Publisher** e **Consumer** usando **RabbitMQ**, **Python** e a biblioteca **Pika**, com configuração via variáveis de ambiente.

---

## 📌 Technologies used / Tecnologias utilizadas

- Python 3.13+
- RabbitMQ
- Pika
- python-dotenv
- Python standard logging

---

## 📁 Project structure / Estrutura do projeto

```text
project_with_rabbitmq/
├── .venv
├── core/
│   └── setup_logging.py
├── docker_rabbitmq/
|   └── compose.yaml
├── src/consumer/
│   └── consumer.py
├── src/publisher/
│   └── publisher.py
├── main_consumer.py
├── main_publisher.py
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Environment variables / Variáveis de ambiente

- RABBITMQ_HOST=localhost
- RABBITMQ_PORT=5672
- RABBITMQ_USER=user@123
- RABBITMQ_PASS=Test@123
- RABBITMQ_QUEUE=my_queue
- RABBITMQ_EXCHANGE=my_exchange

#### ⚠️ Adjust the values according to your RabbitMQ configuration. / Ajuste os valores conforme sua configuração do RabbitMQ.

---

## 📦 Installing dependencies / Instalação das dependências
- uv run 
- source .venv/bin/activate
- uv sync

---

## ▶️ Running your project / Executando seu projeto

This command / Esse comando:

#### 🔊 “Starts” the service that keeps listening to RabbitMQ. / “Liga” o serviço que fica ouvindo o RabbitMQ.

#### python consumer_main.py

You usually run this as a / Normalmente você roda isso como:

- service / serviço
- worker
- background process / processo em background



#### python publisher_main.py

It runs a one-off script that / Ele executa um script pontual, que:

- 1 Connects to RabbitMQ / Conecta no RabbitMQ
- 2 Publishes messages / Publica mensagens
- 3 Terminates the process / Encerra o processo

---

## 🐳 Running RabbitMQ with Docker / Executando o RabbitMQ com Docker

You can run RabbitMQ using Docker with the following service configuration / Você pode executar o RabbitMQ usando o Docker com a seguinte configuração de serviço:

```text
services:
  rabbitmq:
    image: rabbitmq:4.1.5-management
    container_name: rabbitmq
    restart: unless-stopped
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      RABBITMQ_DEFAULT_USER: ${RABBITMQ_USER}
      RABBITMQ_DEFAULT_PASS: ${RABBITMQ_PASS}
    volumes:
      - /home/opc/docker/volumes/rabbirmq:/var/lib/rabbitmq
```

### This setup / Esta configuração:

Exposes the AMQP port (5672) and the management UI (15672) / Expõe a porta AMQP (5672) e a interface de gerenciamento (15672)

Uses environment variables for credentials /  Utiliza variáveis ​​de ambiente para credenciais

Persists RabbitMQ data using a Docker volume / Persiste os dados do RabbitMQ usando um volume Docker

Includes the management plugin for easy monitoring via browser / Inclui o plugin de gerenciamento para facilitar o monitoramento via navegador

You can then start the service with / Você pode então iniciar o serviço com:

```text
docker compose up -d
```
