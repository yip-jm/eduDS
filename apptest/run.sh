#!/bin/bash
#SBATCH --job-name=interactive_app
#SBATCH --output=log/app_%j.out
#SBATCH --error=log/app_%j.err
#SBATCH --time=04:00:00        # Max runtime (e.g., 4 hours)
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1             # Request 1 GPU
#SBATCH --cpus-per-task=8
#SBATCH --mem=32GB
#SBATCH --partition=gpu_h100         # Use a general GPU partition like 'gpu' or 'gpu_shared'

echo "Starting job on $(hostname) at $(date)"
mkdir -p log # Ensure log directory exists

# --- 1. Load required modules & Activate Environment ---
module load 2023
module load Python/3.11.3-GCCcore-12.3.0
module load CUDA/12.1.1

# Activate your Python virtual environment
if [[ -f "${HOME}/.venv/bin/activate" ]]; then
  source "${HOME}/.venv/bin/activate"
else
  echo "ERROR: virtualenv not found at ${HOME}/.venv" >&2
  exit 1
fi
echo "Using python: $(which python)"

# --- 2. Define Models and Ports ---
# Models needed for the application
declare -a MODELS_TO_PULL=("phi4:14b" "qwen2.5:7b" "BAAI/bge-large-en-v1.5")

# Dynamically find unused ports for Ollama and Streamlit
OLLAMA_PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
STREAMLIT_PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
HOSTNAME=$(hostname)

# Set the OLLAMA_HOST environment variable for Python scripts to use
export OLLAMA_HOST="http://127.0.0.1:${OLLAMA_PORT}"

# --- 3. Start Ollama Server in Singularity ---
echo "Starting Ollama server on port ${OLLAMA_PORT}..."
OLLAMA_DIR="$HOME/OLLAMA_DIR/ollama_app_$SLURM_JOB_ID"
mkdir -p "$OLLAMA_DIR"

# Set Singularity environment variables to pass the port and other settings
# Start the server in the background (&)
SINGULARITYENV_OLLAMA_HOST="0.0.0.0:${OLLAMA_PORT}" \
singularity exec --nv \
  --bind "$OLLAMA_DIR":/root/.ollama \
  ollama_latest.sif ollama serve &

# Save the Process ID (PID) of the Ollama server to kill it later
OLLAMA_PID=$!

# Define a cleanup function to be called on job exit
cleanup() {
    echo "Cleaning up... Killing Ollama server (PID: $OLLAMA_PID)"
    kill $OLLAMA_PID
    wait $OLLAMA_PID 2>/dev/null
    echo "Cleanup complete."
}
trap cleanup EXIT # Register the cleanup function

# Wait for the Ollama server to be ready
echo "Waiting for Ollama server to become available..."
until curl -s -o /dev/null -w "%{http_code}" "http://localhost:${OLLAMA_PORT}" | grep -q "200"; do
    echo -n "."
    sleep 2
done
echo "Ollama server is ready!"

# --- 4. Pull all required models ---
for model in "${MODELS_TO_PULL[@]}"; do
    echo "Pulling model: $model"
    ollama --host "http://localhost:${OLLAMA_PORT}" pull "$model"
done
echo "All models are pulled and ready."

# --- 5. Print Connection Instructions ---
echo ""
echo "#####################################################################"
echo "###           YOUR INTERACTIVE APP IS READY TO CONNECT            ###"
echo "#####################################################################"
echo ""
echo "Job is running on compute node: ${HOSTNAME}"
echo "Streamlit will run on port:   ${STREAMLIT_PORT}"
echo ""
echo "STEP 1: From your LOCAL machine, open a NEW terminal and run this command:"
echo "ssh -L 8501:${HOSTNAME}:${STREAMLIT_PORT} jye@snellius.surf.nl"
echo ""
echo "STEP 2: After the tunnel is active, open your web browser and go to:"
echo "http://localhost:8501"
echo ""
echo ">>> This job will run for 4 hours. Press Ctrl+C in this terminal or use 'scancel ${SLURM_JOB_ID}' to stop it."
echo "#####################################################################"
echo ""

# --- 6. Run the Streamlit Application ---
# The script will now wait here until Streamlit is closed or the job is cancelled.
streamlit run /home/jye/apptest/src/app.py \
  --server.port ${STREAMLIT_PORT} \
  --server.headless true \
  --server.address 0.0.0.0 \
  --server.enableCORS false

# The cleanup function will automatically run when the script exits.
