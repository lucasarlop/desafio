from json  import loads
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'test-topic',
    group_id           = 'my-group',
    bootstrap_servers  = ['localhost:9092'],
    auto_offset_reset  = 'earliest',
    enable_auto_commit = True,
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)

for message in consumer:
    print ("""Mensagem recebida:\n\tTópico: %s\n\tPartição: %d\n\tOffset: %d\n\tChave: %s\n\tValor: %s\n\tTipo de Dado: %s\n""" % (
            message.topic,
            message.partition,
            message.offset,
            message.key,
            message.value,
            type(message.value)
        )
    )