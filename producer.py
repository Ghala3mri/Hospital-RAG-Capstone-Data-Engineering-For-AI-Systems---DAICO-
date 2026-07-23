import json
import pandas as pd
from confluent_kafka import Producer
from pydantic import ValidationError
from contract import HealthcareRecord
from config import (
    BOOTSTRAP_SERVER,
    API_KEY,
    API_SECRET,
    TOPIC,
    DLQ_TOPIC,
    DATASET
)

# إعدادات Confluent Cloud
conf = {
    "bootstrap.servers": BOOTSTRAP_SERVER,
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": API_KEY,
    "sasl.password": API_SECRET
}

producer = Producer(conf)

# قراءة ملف CSV
df = pd.read_csv(DATASET)

# إعادة تسمية الأعمدة لتطابق الـ Schema
df = df.rename(columns={
    "Blood Type": "Blood_Type",
    "Medical Condition": "Medical_Condition",
    "Date of Admission": "Date_of_Admission",
    "Insurance Provider": "Insurance_Provider",
    "Billing Amount": "Billing_Amount",
    "Room Number": "Room_Number",
    "Admission Type": "Admission_Type",
    "Discharge Date": "Discharge_Date",
    "Test Results": "Test_Results"
})

# دالة تقرير الإرسال
def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed:", err)
    else:
        print(f"Message delivered to {msg.topic()}")

# إرسال البيانات
for _, row in df.iterrows():
    row_dict = row.to_dict()

    try:
        validated = HealthcareRecord(**row_dict)

        producer.produce(
            TOPIC,
            json.dumps(validated.dict()).encode("utf-8"),
            callback=delivery_report
        )

    except ValidationError as e:
        error_payload = {
            "raw_row": row_dict,
            "error": str(e)
        }

        producer.produce(
            DLQ_TOPIC,
            json.dumps(error_payload).encode("utf-8"),
            callback=delivery_report
        )

producer.flush()