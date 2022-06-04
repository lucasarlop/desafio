from time  import sleep
from json  import dumps

from kafka import KafkaProducer

MORSE_CODE = {
    1: '.----', 2: '..---', 3: '...--',
    4: '....-', 5: '.....', 6: '-....',
    7: '--...', 8: '---..', 9: '----.',
    0: '-----'
}

producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer  = lambda x: dumps(x).encode('utf-8')
)

for n in range(100):
    data = {
        'Número': n,
        'Morse': MORSE_CODE[n]
    }
    producer.send('test-topic', value = data)
    sleep(5)