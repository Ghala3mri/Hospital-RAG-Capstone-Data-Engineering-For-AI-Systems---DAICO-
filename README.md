# Hospital RAG Pipeline
## Project Overview


This project demonstrates an end-to-end AI Data Engineering pipeline for healthcare data.
The pipeline simulates real-time patient data ingestion, validates data quality, stores clean data in a Delta Lakehouse architecture, and builds a Retrieval-Augmented Generation (RAG) system that answers healthcare-related questions from medical documents.
This project was developed as a Capstone Project covering modern Data Engineering and Generative AI concepts.


---
## Project Objectives
- Stream healthcare data using Kafka
- Validate data quality
- Store data in Delta Lake
- Build a RAG pipeline
- Orchestrate using Apache Airflow
---
## Technologies
---
## Project Structure
---
## Pipeline Workflow
1. Healthcare dataset ingestion
2. Kafka Producer
3. Kafka Consumer
4. Data Quality Validation
5. Quarantine invalid records
6. Bronze Layer
7. Silver Layer
8. Gold Layer
9. Document Chunking
10. Embedding Generation
11. ChromaDB Vector Database
12. Hybrid Search
13. Groq LLM
14. Final AI Response
---
## Data Quality

The pipeline validates:

- Schema Validation
- Null Values
- Data Types
- Duplicate Records
- Range Validation

Invalid records are redirected to a Quarantine Zone.
---
## RAG Pipelin
The RAG system includes:

- PDF document loading
- Chunking
- Embeddings
- ChromaDB
- Hybrid Search
- Cross-Encoder Re-ranking
- LLM Answer Generation
---
## How to Run
1. Open the notebook in Google Colab.
2. Install the required libraries.
3. Upload the healthcare dataset.
4. Upload medical PDF documents.
5. Run all notebook cells.
6. Ask questions through the RAG pipeline.
---
## Pipeline Archietcture
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
---
## 👩‍💻 Developed By:
Ghala Alamri - 
Ghaida Alwasel - 
Sara Al-Sa'ed



