# Desafio

## 1. Criação de um ambiente em notebook próprio
Atualização no Ubuntu
Instalação do Java

## 2. Instalação do Kafka 2.7.0
`wget https://archive.apache.org/dist/kafka/2.7.0/kafka-2.7.0-src.tgz`


## 3. Configuração do Zookeeper via Systemd do Linux
`sudo vim /etc/systemd/system/zookeeper.service`

## 4. Configuração do Broker via Systemd do Linux
`sudo vim /etc/systemd/system/kafka.service`

## 5. Criação de Tópico de nome "test-topic"
`cd /usr/local/kafka-server/`
`bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 3 --topic test-topic`

## 6. Criação de produtor de mensagens em Shell/Python e geração de mensagens para o Tópico "test-topic"
producer.py

## 7. Criação de consumidor de mensagens em Shell/Python e consumo de mensagens para o Tópico "test-topic"
consumer.py

# Bônus

## Configuração de CMAK
Configuração do CMAK
Apresentação de Interface do CMAK

## Prometheus JMX Exporter
Acompanhamento de Métricas com Prometheus e Grafana