# Small Language Models for Educational Data Storytelling
This project is an advanced AI-driven content generation system designed to transform unstructured educational materials, such as PDF documents, into structured and engaging lesson packages. It transcends a standard RAG (Retrieval-Augmented Generation) system by implementing a complete "Knowledge-to-Curriculum" pipeline, centered around a unique Data Storytelling Engine.

## Key Features
- Converts PDF files into Markdown
- Advanced Hybrid Retrieval (BM25 + vector search)
- Structured Knowledge Extraction (based on RAG)
- Data Storytelling & Lesson Generation (Lesson Plan Outline -> Core Concept Story Module -> Interactive Activity Module)
- Modular and Extensible

## System Architecture & Workflow
[Raw PDF] -> [Stage 1: Preprocessing] -> [Stage 2: Knowledge Extraction] -> [Structured Knowledge JSON] -> [Stage 3: Lesson Generation] -> [Complete Lesson Package]


1. PDF to Markdown: [MinerU](https://github.com/opendatalab/MinerU)
2. RAG-based Knowledge Extraction
3. Data Stotytelling Pipeline

## Installation

### 1. Clone the Repository
```
git clone https://github.com/yip-jm/eduDS
cd eduDS
```

### 2. Create and Activate a Virtual Environment
```
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

## How to Use

1. Place your  files (**markdown format**) in the `/docs/materials_md/parsed` directory.
2. Place query (**JSON format**) in the`/docs/query`.
3. Run the script from your terminal:
    ```
    sbatch run_ke.sh
    ```
    and then:
    ```
    sbatch run_sg.sh
    ```


