import streamlit as st
import os
from core.rag import EnhancedRAG
from core.DataStorytellingEngine import DataStorytellingEngine

# --- CONFIGURATION ---
UPLOAD_DIR = "docs/materials_md/parsed/"
# Define the models the app will use. These should match the models pulled in run_app.sh
RAG_MODEL = "phi4:14b"
STORY_MODEL = "qwen2.5:7b"
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"

# --- BACKEND INITIALIZATION (CACHED) ---
@st.cache_resource
def setup_backend():
    """
    Initializes the RAG and Storytelling engines.
    This function is cached, so it only runs once.
    """
    st.info("Initializing backend systems... This may take a moment.")
    
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if not any(f.endswith('.md') for f in os.listdir(UPLOAD_DIR)):
         st.warning("No documents found. Please upload documents before asking a question.", icon="⚠️")
         return None, None

    # Initialize the RAG system
    # The OLLAMA_HOST is automatically read inside the EnhancedRAG class now
    rag_system = EnhancedRAG(
        embedding_model_name=EMBEDDING_MODEL,
        model_name=RAG_MODEL,
        persist_dir="vector_db_app"
    )

    # Initialize the Data Storytelling Engine
    story_engine = DataStorytellingEngine(model_name=STORY_MODEL)
    
    st.success("Backend systems are ready!")
    return rag_system, story_engine

# --- STREAMLIT UI ---
def main():
    st.set_page_config(page_title="Edu-Genius", layout="wide")
    st.title("📚 Edu-Genius: From Documents to Lesson Plans")
    st.markdown("Upload markdown files, ask a question, and generate a structured knowledge base and an engaging lesson plan.")

    # --- SIDEBAR FOR FILE MANAGEMENT ---
    with st.sidebar:
        st.header("⚙️ Setup")
        st.subheader("1. Upload Documents")
        uploaded_files = st.file_uploader(
            "Upload .md files",
            type=["md"],
            accept_multiple_files=True
        )

        if uploaded_files:
            for uploaded_file in uploaded_files:
                with open(os.path.join(UPLOAD_DIR, uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getbuffer())
            st.success(f"{len(uploaded_files)} file(s) saved to `{UPLOAD_DIR}`!")

        st.subheader("2. Initialize System")
        if st.button("Process Documents & Load Models"):
            # Clear cache to force re-initialization with new files
            st.cache_resource.clear()
            st.success("System will re-index documents and reload models on the next action.")
            st.rerun()
            
        st.warning("Click this after uploading new files to make them available.")

        # --- NEW: FILE DELETION SECTION ---
        st.divider()
        st.subheader("3. Manage Uploaded Files")
        
        # Ensure the upload directory exists before listing files
        if os.path.exists(UPLOAD_DIR):
            try:
                # List only .md files in the directory
                files_in_dir = [f for f in os.listdir(UPLOAD_DIR) if f.endswith('.md') and os.path.isfile(os.path.join(UPLOAD_DIR, f))]
                
                if not files_in_dir:
                    st.info("No files to delete.")
                else:
                    files_to_delete = st.multiselect(
                        "Select files to delete:",
                        options=files_in_dir
                    )
                    
                    if st.button("Delete Selected Files", type="primary"):
                        if not files_to_delete:
                            st.warning("Please select at least one file to delete.")
                        else:
                            deleted_count = 0
                            for filename in files_to_delete:
                                try:
                                    os.remove(os.path.join(UPLOAD_DIR, filename))
                                    deleted_count += 1
                                except Exception as e:
                                    st.error(f"Error deleting {filename}: {e}")
                            
                            if deleted_count > 0:
                                st.success(f"Successfully deleted {deleted_count} file(s).")
                                # IMPORTANT: Clear cache and rerun to reflect changes
                                st.cache_resource.clear()
                                st.rerun()
            except Exception as e:
                st.error(f"Error reading directory {UPLOAD_DIR}: {e}")


    # --- MAIN CONTENT AREA ---
    rag_system, story_engine = setup_backend()

    if rag_system and story_engine:
        st.header("💬 Ask Your Question")
        query = st.text_input(
            "Enter your question about the uploaded content:",
            placeholder="e.g., 'What are the main differences between RISC and CISC architectures?'"
        )

        if st.button("Generate Lesson Plan"):
            if not query:
                st.error("Please enter a question.")
            else:
                with st.spinner("🧠 Generating... This can take a few minutes..."):
                    try:
                        # Step 1: Extract knowledge
                        st.write("Step 1/2: Extracting knowledge from documents...")
                        knowledge_base = rag_system.ask(query)
                        st.session_state['knowledge_base'] = knowledge_base

                        # Step 2: Generate lesson plan
                        st.write("Step 2/2: Generating the data story and lesson plan...")
                        lesson_plan = story_engine.generate_lesson_package(knowledge_base)
                        st.session_state['lesson_plan'] = lesson_plan
                        
                        st.success("Generation Complete!")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                        st.exception(e) # Also print the full traceback for debugging
    else:
        st.info("Please upload documents and click 'Process Documents & Load Models' in the sidebar to begin.")

    # --- DISPLAY RESULTS ---
    if 'lesson_plan' in st.session_state:
        st.divider()
        st.header("🎉 Your Generated Content")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔬 Extracted Knowledge Base")
            st.json(st.session_state.get('knowledge_base', {}))
        with col2:
            st.subheader("📖 Generated Lesson Plan")
            st.markdown(st.session_state.get('lesson_plan', ''))

if __name__ == "__main__":
    main()