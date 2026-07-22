🏥 Hospital RAG & Data Quality Pipeline
 Project Overview
This project demonstrates an end-to-end AI Data Engineering pipeline for healthcare data.
The pipeline simulates real-time patient data ingestion, validates data quality, stores clean data in a Delta Lakehouse architecture, and builds a Retrieval-Augmented Generation (RAG) system that answers healthcare-related questions from medical documents.
This project was developed as a Capstone Project covering modern Data Engineering and Generative AI concepts.

flowchart TD
A[Healthcare Dataset]
B[Kafka Producer]
C[Kafka Consumer]
D[Data Quality Validation]
E{Valid?}
F[Quarantine]
G[Bronze]
H[Silver]
I[Quality Gate]
J[Gold]
K[RAG Pipeline]
L[Groq LLM]
M[Final AI Answer]

A --> B --> C --> D --> E
E -->|No| F
E -->|Yes| G --> H --> I
I --> J
I --> K
K --> L --> M


👩‍💻 Developed By
Ghala Alamri
Ghaida Alwasel
Sara Al-Sa'ed



