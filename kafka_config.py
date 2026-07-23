#   KAFKA CONFIGURATION

BOOTSTRAP_SERVER = "pkc-921jm.us-east-2.aws.confluent.cloud:9092"
API_KEY = "YTKW4FZCW6HJWJDB"
API_SECRET = "cfltaQnaWNomnajyBw0dvpk4ph88RzI61F2xJKQZ8bcXgvW+49DXM+fg8/W84eqg"

TOPIC = "hospital.records"
DLQ_TOPIC = "hospital.records.dlq"
DATASET = "C:\Users\arwa_\OneDrive\Desktop\Hospital_Project\data\healthcare_dataset.csv"
# Common Kafka settings
KAFKA_CONF = {
    "bootstrap.servers": BOOTSTRAP_SERVER,
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": API_KEY,
    "sasl.password": API_SECRET,
}