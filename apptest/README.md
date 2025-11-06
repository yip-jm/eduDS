# eduDS Project including WEB GUI


1. PDF to Markdown: [MinerU](https://github.com/opendatalab/MinerU)
2. RAG-based Knowledge Extraction
3. Data Stotytelling Pipeline

## Installation for Web GUI

### 1. Create and Activate a Virtual Environment
```
python3 -m venv ~/.venv
# macOS/Linux
source ~/.venv/bin/activate
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

## How to Use

1. Run the script from your terminal:
    ```
    sbatch run.sh
    ```

2. Once the job starts, the script (in `apptest/log/app_xxxx.out`) in will output connection instructions similar to:
    ```yaml
    #####################################################################
    ###           YOUR INTERACTIVE APP IS READY TO CONNECT            ###
    #####################################################################

    Job is running on compute node: gpu-node-12
    Streamlit will run on port: 57029

    STEP 1: From your LOCAL machine, open a new terminal and run:
    ssh -L 8501:gpu-node-12:57029 {yourusername}@snellius.surf.nl

    STEP 2: Open your browser and go to:
    http://localhost:8501
    ```


3. Accessing the Web Interface

    From your local machine, establish an SSH tunnel:
    ```bash
    ssh -L 8501:<HOSTNAME>:<PORT> <yourusername>@snellius.surf.nl
    ```
    After running this command, you will be prompted to enter your HPC account password. Once authentication is successful, the SSH tunnel will remain open as long as the terminal stays running.
    
    Then open your browser:
    ```
    http://localhost:8501
    ```

    This connects your local browser to the Streamlit app running inside the HPC compute node.


4. Stopping the Application

    Closing the browser does not stop the job.

    To stop the app and release GPU resources:
    ```
    scancel <JOB_ID>
    ```





