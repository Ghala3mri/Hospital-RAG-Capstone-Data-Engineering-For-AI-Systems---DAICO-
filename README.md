🏥 Hospital RAG & Data Quality Pipeline
 Project Overview
This project demonstrates an end-to-end AI Data Engineering pipeline for healthcare data.
The pipeline simulates real-time patient data ingestion, validates data quality, stores clean data in a Delta Lakehouse architecture, and builds a Retrieval-Augmented Generation (RAG) system that answers healthcare-related questions from medical documents.
This project was developed as a Capstone Project covering modern Data Engineering and Generative AI concepts.


⸻


📂 Project Structure
Hospital-RAG-Capstone
│
├── Hospital_Capstone.ipynb
├── README.md
├── requirements.txt
├── data/
│   └── healthcare_dataset.csv
├── pdf/
│   └── diabetes_guide.pdf
├── images/
│   └── architecture.png
└── output/


⸻


🏗️ Architecture
Healthcare Dataset
        │
        ▼
Kafka Producer
        │
        ▼
Kafka Consumer
        │
        ▼
Quality Validation
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
Delta Lake     Quarantine
(Bronze)
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ▼
Chunking
        │
        ▼
Embeddings
        │
        ▼
ChromaDB
        │
        ▼
Hybrid Search
        │
        ▼
LLM Response


⸻




⸻


▶️ How to Run
Open the notebook in Google Colab.
Install the required libraries.
Upload the healthcare dataset.
Execute the notebook cells from top to bottom.
Upload the PDF document.
Ask questions through the RAG pipeline.


⸻


👩‍💻 Developed By
Ghala Alamri
Ghaida Alwasel
Sara Al-Sa'ed
King Saud University
Information Technology

