from time  import sleep
from json  import dumps

from kafka import KafkaProducer

MORSE_CODE = {
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

def morse_code(n):
    if n < 10:
        return MORSE_CODE[str(n)]
    else:
        morse = ""
        for np in str(n):
            morse += MORSE_CODE[str(np)] + " "
        
        return morse[:-1]

producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer  = lambda x: dumps(x).encode('utf-8')
)

for n in range(10000):
    data = {
        'Número': n,
        'Morse': morse_code(n)
    }
    producer.send('test-topic', value = data)
    # sleep(1)