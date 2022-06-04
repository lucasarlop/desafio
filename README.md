# desafio


## LEGEND
KAFKA_PATH='/usr/local/kafka-server'

## 1. Criação de um ambiente em notebook próprio
Atualização no Ubuntu
Instalação do Java

## 2. Instalação do Kafka 2.7.0
Scala 2.12
Kafka 2.7.0

ONDE FIZ O DOWNLOAD?
kafka_2.12-2.7.0.tgz

Baixar arquivos em:
`wget https://downloads.apache.org/kafka/2.7.0/kafka_2.12-2.7.0.tgz`


## 3. Configuração do Zookeeper via Systemd do Linux
`sudo vim /etc/systemd/system/zookeeper.service`

## 4. Configuração do Broker via Systemd do Linux
`sudo vim /etc/systemd/system/kafka.service`

## 5. Criação de Tópico de nome "test-topic"
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test-topic`

## 6. Criação de produtor de mensagens em Shell/Python e geração de mensagens para o Tópico "test-topic"
producer.py

## 7. Criação de consumidor de mensagens em Shell/Python e consumo de mensagens para o Tópico "test-topic"
consumer.py

# Bônus

## Configuração de CMAK
Configuração do CMAK
Apresentação de Interface do CMAK







# Dúvidas
O que é serializar?