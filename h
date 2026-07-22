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
