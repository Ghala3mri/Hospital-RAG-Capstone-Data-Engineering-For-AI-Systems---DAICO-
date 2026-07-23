from confluent_kafka import Consumer
import json
from config import (
    BOOTSTRAP_SERVER,
    API_KEY,
    API_SECRET,
    TOPIC
)

# إعدادات Confluent Cloud
conf = {
    "bootstrap.servers": BOOTSTRAP_SERVER,
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": API_KEY,
    "sasl.password": API_SECRET,
    "group.id": "healthcare-consumer-group",
    "auto.offset.reset": "earliest"
}

# إنشاء consumer
consumer = Consumer(conf)

# الاشتراك في التوبك
consumer.subscribe([TOPIC])

print(f"Consumer is now listening on topic: {TOPIC}")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Error:", msg.error())
        continue

    # فك الرسالة
    record = json.loads(msg.value().decode("utf-8"))

    print("Consumed record:", record)