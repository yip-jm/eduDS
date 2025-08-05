# Small Language Models for Educational Data Storytelling


## Key Features

- PDF parsing with structured Markdown conversion
- Hybrid retrieval (semantic embedding + BM25)
- Context aggregation across documents
- Integration with local LLMs (via Ollama)
- Supports narrative-driven data storytelling

## System Architecture & Workflow

### Document Preprocessing & Content Enhancement 
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

1. Place your  files (**md format**) in the `/docs/materials_md/parsed` directory.

2. Place query (**JSON format**) in the`/docs/query`.

3. Run the script from your terminal:
    ```
    sbatch run_ke.sh
    ```
    and then:
    ```
    sbatch run_sg.sh
    ```


