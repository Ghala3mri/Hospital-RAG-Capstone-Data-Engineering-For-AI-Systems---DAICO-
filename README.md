#🏥 Hospital RAG & Data Quality Pipeline
 Project Overview
This project demonstrates an end-to-end AI Data Engineering pipeline for healthcare data.
The pipeline simulates real-time patient data ingestion, validates data quality, stores clean data in a Delta Lakehouse architecture, and builds a Retrieval-Augmented Generation (RAG) system that answers healthcare-related questions from medical documents.
This project was developed as a Capstone Project covering modern Data Engineering and Generative AI concepts.

```text
Kafka Producer
      │
      ▼
Kafka Consumer
      │
      ▼
Data Quality Validation
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Quarantine Bronze
              │
              ▼
         Silver Layer
              │
              ▼
        Quality Gate
          │       │
          ▼       ▼
   Gold Layer   RAG Pipeline
              │
              ▼
          Groq LLM
              │
              ▼
        Final AI Answer
/

```

👩‍💻 Developed By:
-Ghala Alamri
-Ghaida Alwasel
-Sara Al-Sa'ed



