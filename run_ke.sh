#!/bin/bash
#SBATCH --job-name=ollama_gpu_job  # Job name
#SBATCH --output=log/%j.out
#SBATCH --error=log/%j.err
#SBATCH --time=3-00:00:00        # Max runtime (3 days)
#SBATCH --nodes=1                # Use #number physical machines
#SBATCH --ntasks=1               # 🔥 Run #number parallel python scripts when you have different settings
#SBATCH --gres=gpu:1             # Request #number GPU, when you need more control over GPU type or specific features  (A100)
#SBATCH --cpus-per-task=8        # 🔥 Assign #number CPUs per task; Match with args.processes=8; If inference is GPU-bound, having too many CPU processes won't help.

#SBATCH --mem=32GB               # Request of memory
#SBATCH --partition=gpu_a100     # Use the GPU partition

echo "Starting job on $(hostname) at $(date)"
echo "Total CPUs allocated: $SLURM_JOB_CPUS_PER_NODE"
echo "Number of CPUs allocated by Slurm=$SLURM_CPUS_PER_TASK"

# --- 1. Load required modules ---
module load 2023
module load Python/3.11.3-GCCcore-12.3.0
module load CUDA/12.1.1
module load cuDNN/8.9.2.26-CUDA-12.1.1

source ~/.bashrc
source /home/jye/dse2/init.sh

# source activate worldtaskeval
if [[ -f "${HOME}/.venv/bin/activate" ]]; then
  source "${HOME}/.venv/bin/activate"
else
  echo "ERROR: virtualenv not found at ${HOME}/.venv" >&2
  exit 1
fi

echo "Using python: $(which python)"

# ----------- MinerU: Download Models -----------
# wget https://github.com/opendatalab/MinerU/raw/master/scripts/download_models_hf.py -O download_models_hf.py
# python download_models_hf.py

# sed -i 's|cpu|cuda|g' ~/magic-pdf.json
# pip install paddlepaddle-gpu==2.6.0 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
pip install -r requirements.txt


# --- 2. Set Environment Variables (for GPU) ---
export PATH="${HOME}/.venv/bin:$PATH"
# GPU Optimization
export CUDA_VISIBLE_DEVICES=0  # Use the allocated GPU
export OLLAMA_FORCE_CUDA=1
export OLLAMA_NUM_GPU=1        # Match the number of requested GPUs
# export CUDA_VISIBLE_DEVICES=0,1,2,3
# export OLLAMA_NUM_GPU=4
export OLLAMA_ACCELERATE=1
export OLLAMA_LLM_LIBRARY=cublas  # Use cuBLAS for acceleration
# export OLLAMA_LLM_LIBRARY=flash-attn
export OLLAMA_PRECISION=fp16  # Enable 16-bit floats for Tensor Cores # A100 GPUs perform best with mixed precision:
export OLLAMA_BATCH_SIZE=32  # Adjust based on GPU memory
export OLLAMA_NUM_THREAD=16
export OMP_NUM_THREADS=16
export MKL_NUM_THREADS=16
export OLLAMA_USE_CUDA_GRAPHS=1
export OLLAMA_CONTEXT_SIZE=8192  # Increase from default (~2048)
export OLLAMA_KEEP_LOADED=1
export OLLAMA_PORT=11434
export OLLAMA_MAX_LOADED_MODELS=4

# --- 4. Singularity and GPU Access ---
# 4.1 Verify
singularity --version
# Check If Singularity Detects GPUs
singularity pull ollama_latest.sif docker://ollama/ollama
singularity exec --nv ollama_latest.sif nvidia-smi
echo "Checking available executables inside Singularity:"
singularity exec --nv ollama_latest.sif echo $LD_LIBRARY_PATH
singularity exec --nv ollama_latest.sif which python
singularity exec --nv ollama_latest.sif which ollama

# 4.2 Start and test Ollama with GPU Support ---





# embedding_models=("BAAI/bge-large-en-v1.5" "Qwen/Qwen3-Embedding-0.6B" "mixedbread-ai/mxbai-embed-large-v1")
# llm_models=("deepseek-llm:7b" "gemma:7b"  "qwen2.5:7b" "openchat:7b" "llama3.1:8b" "olmo2:7b" "phi4:14b")



rag_models=("deepseek-llm:7b" "gemma:7b" "qwen2.5:7b" "openchat:7b" "llama3.1:8b" "olmo2:7b" "phi4:14b")
story_models=("deepseek-llm:7b" "gemma:7b" "qwen2.5:7b" "openchat:7b" "llama3.1:8b" "olmo2:7b" "phi4:14b")




for llm in "${rag_models[@]}"; do
  
  echo "================================================================="
  echo "Starting Experiment with:"
  echo "  LLM Model: $llm"
  echo "================================================================="

  echo "Starting Ollama server..."


  #  ---------------- load LLM Model --------------------
  RAG_MODEL_NAME=$llm  
  PORT=$((11434 + ($SLURM_JOB_ID % 1000)))
  OLLAMA_DIR="~/OLLAMA_DIR/ollama_$SLURM_JOB_ID"

  # Create isolated model/data directory
  mkdir -p "$OLLAMA_DIR"

  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama serve&

  OLLAMA_PID=$!
  until curl -s http://localhost:$PORT/api/tags > /dev/null; do
      sleep 5
  done
  echo "Ollama for RAG server is ready!"

  # ------------------------------------------------------------------

  # SY_MODEL_NAME=$syllm  
  # OLLAMA_DIR="~/OLLAMA_DIR/ollama_$SLURM_JOB_ID"

  # # Create isolated model/data directory
  # mkdir -p "$OLLAMA_DIR"

  # SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
  #   --bind "$OLLAMA_DIR":/root/.ollama \
  #   ollama_latest.sif ollama serve&

  # OLLAMA_PID=$!
  # until curl -s http://localhost:$PORT/api/tags > /dev/null; do
  #     sleep 5
  # done
  # echo "Ollama for SYLLM server is ready!"


  # -------------------------------------------------------------------------
  # Pull qwen2.5vl:7b to convert image ---
  

  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama serve&

  OLLAMA_PID=$!
  until curl -s http://localhost:$PORT/api/tags > /dev/null; do
      sleep 5
  done
  echo "Ollama for VL-LLM server is ready!"


  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama pull "qwen2.5vl:7b"
  echo "Ollama model -- qwen2.5vl:7b is downloaded!"

  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama run "qwen2.5vl:7b" --verbose

  # -------------------------------------------------------------------------


  # 4.4 Pull LLM Model (Ensure Model is Downloaded) ---
  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama pull $RAG_MODEL_NAME
  echo "Ollama RAG model is downloaded!"

  SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
    --bind "$OLLAMA_DIR":/root/.ollama \
    ollama_latest.sif ollama run $RAG_MODEL_NAME --verbose


  # SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
  #   --bind "$OLLAMA_DIR":/root/.ollama \
  #   ollama_latest.sif ollama pull $SY_MODEL_NAME
  # echo "Ollama SYLLM model is downloaded!"

  # SINGULARITYENV_OLLAMA_HOST=0.0.0.0:$PORT singularity exec --nv \
  #   --bind "$OLLAMA_DIR":/root/.ollama \
  #   ollama_latest.sif ollama run $SY_MODEL_NAME --verbose


  # --- 5. Run the Python Script with Correct Python Path ---
  export PYTHONPATH=$PWD  # Ensure Python finds your package
  export OLLAMA_HOST="http://127.0.0.1:${PORT}"

  echo "Running Python script with models: $llm"

  python src/main_ke.py --rag_model "$llm"



  # --- 6. Cleanup: Kill Ollama Server ---
  echo "Job completed at $(date)"
  kill $OLLAMA_PID
done



echo "All jobs completed at $(date)"