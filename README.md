# 🛡️ Sentinel

Ferramenta para **validação de dados baseada em Schema**
------------------------------------------------------------------------

## 🚀 Visão Geral

O Sentinel recebe dados (via fila ou entrada direta), identifica o
schema correto pela assinatura e valida o conteúdo.

### Fluxo:

Queue → Observer → UseCase → Repository → Factory → Tester → Notifier

------------------------------------------------------------------------

## 🧱 Arquitetura

### Core

-   Entidades (Schema, SchemaVersion)
-   UseCases (AnalyzeData)
-   Protocolos:
    -   SchemasRepository
    -   SchemaTester
    -   QueueProtocol
    -   AnomalyNotifier

### Infra

-   Repositórios:
    -   InMemory
    -   SQLite
    -   MySQL
-   Testers:
    -   XSD (XML)
    -   JSON Schema
-   Notificadores:
    -   Logging
    -   SMTP
-   Filas:
    -   FakeQueue
    -   RedisQueue

------------------------------------------------------------------------

## 🐳 Infraestrutura de teste (Docker)

Serviços: - MySQL - Redis - MailHog

------------------------------------------------------------------------

## 🧪 Executando

python main.py

------------------------------------------------------------------------

## 🧪 População de Cache

python environment/development/seeders/redis/populate_queue.py

------------------------------------------------------------------------

### For victory we ride, fury of the storm.