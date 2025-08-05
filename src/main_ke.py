from core.rag import EnhancedRAG
from core.utils import reconstruct_specific_json, sanitize_json_string
from core.myPDFparser import PDF2MarkdownConverter
from core.DataStorytellingEngine import DataStorytellingEngine
import os
import json
import shutil
import argparse
from glob import glob


def main(rag_model: str):  

    embedding_model = "BAAI/bge-large-en-v1.5"  # Default embedding model
    # # obtain the ROOT_DIR from environment variable
    ROOT_DIR = os.environ.get("ROOT_DIR")
    if ROOT_DIR is None:
        raise EnvironmentError("Environment variable ROOT_DIR not set")

    # 1. Parse the PDF document and extract images

    material_pdf_dir = os.path.join(ROOT_DIR, "docs", "materials")
    material_md_dir = os.path.join(ROOT_DIR, "docs", "materials_md")

    if not os.path.exists(material_md_dir):
        print(f"📄 Converting PDF files in {material_pdf_dir} to Markdown in {material_md_dir}...")
        os.makedirs(material_md_dir, exist_ok=True)
        pdf2md = PDF2MarkdownConverter(pdf_root_dir=material_pdf_dir, output_dir=material_md_dir)
        pdf2md.convert()



    # construct output directories
    output_dir_ke = os.path.join(ROOT_DIR, "results", f"{rag_model.replace('/', '_').replace(':', '_')}", "knowledge_extraction")
    
    persist_dir = os.path.join(ROOT_DIR, "vector_db", embedding_model.replace('/', '_').replace(':', '_'))



    if os.path.exists(output_dir_ke):
        shutil.rmtree(output_dir_ke, ignore_errors=True)
    os.makedirs(output_dir_ke, exist_ok=True)


    if os.path.exists(persist_dir):
        shutil.rmtree(persist_dir, ignore_errors=True)

    # 初始化 RAG
    rag = EnhancedRAG(
        embedding_model_name=embedding_model,
        model_name=rag_model,
        persist_dir=persist_dir
    )

   

    input_dir = os.path.join(ROOT_DIR, "docs", "query")
    query_files = glob(os.path.join(input_dir, "query*.json"))


    for qfile in query_files:
        with open(qfile, "r", encoding="utf-8") as f:
            querys_data = json.load(f)

        print(f"\n🟢 Processing file: {os.path.basename(qfile)}")

        input_filename = os.path.basename(qfile)
        ques_prefix = input_filename.replace(".json", "")

        output_subdir_ke = os.path.join(output_dir_ke, ques_prefix)
        os.makedirs(output_subdir_ke, exist_ok=True)


        if os.path.exists(output_subdir_ke):
            shutil.rmtree(output_subdir_ke, ignore_errors=True)
        os.makedirs(output_subdir_ke, exist_ok=True)

        for idx, item in enumerate(querys_data):
            query = item.get("Question", "")
            print(f"🟠  - Q{idx + 1}: {query}")

            try:
                parsed_data = rag.ask(query)
                knowledge_base, final_json = reconstruct_specific_json(parsed_data)
                # safe_json = sanitize_json_string(final_json)
                print(f"    🟢 Safe JSON: {final_json}")
                answer_json = json.loads(final_json)  # 确保 JSON 字符串是合法的
            except Exception as e:
                print(f"  main.py ⚠️ Error: {e}")
                

            # 输出为 /results/ques1/q1.json
            output_filename = f"q{idx + 1:02d}.json"  # 如 q01.json
            output_file_path = os.path.join(output_subdir_ke, output_filename)

            with open(output_file_path, "w", encoding="utf-8") as f_out:
                json.dump(answer_json, f_out, indent=2, ensure_ascii=False)


            

        print(f"✅ Saved individual answers to: {output_subdir_ke}")



    # output_dir_sg = os.path.join(ROOT_DIR, "result", f"{embedding_model.replace('/', '_').replace(':', '_')}__{rag_model.replace('/', '_').replace(':', '_')}__{story_model.replace('/', '_').replace(':', '_')}", "story_generation")
    # if os.path.exists(output_dir_sg):
    #     shutil.rmtree(output_dir_sg, ignore_errors=True)
    # os.makedirs(output_dir_sg, exist_ok=True)

    # ke_files = glob(os.path.join(output_dir_ke, "*", "*.json"))

    # story_models = ["deepseek-llm:7b", "gemma:7b", "qwen2.5:7b", "openchat:7b", "llama3.1:8b", "olmo2:7b", "phi4:14b"]

    # if bool_story:
    #     for story_model in story_models:
    #         for kfile in ke_files:
    #             with open(kfile, "r", encoding="utf-8") as f:
    #                 knowledge_base = json.load(f)

    #             input_filename = os.path.basename(kfile)
    #             ke_prefix = input_filename.replace(".json", "")

    #             output_subdir_sg = os.path.join(output_dir_sg, ke_prefix)
    #             os.makedirs(output_subdir_sg, exist_ok=True)

    #             ds = DataStorytellingEngine(
    #                 model_name=story_model,
    #             )

    #             story = ds.generate_story_lesson_plan(
    #                 knowledge_base=knowledge_base,
    #             )
    #             print(f"    🟢 Story:\n{story}")

    #             output_story_filename = f"story_q{idx + 1:02d}.md"  # 如 story_q01.md
    #             output_story_file_path = os.path.join(output_subdir_sg, output_story_filename)
                
    #             with open(output_story_file_path, "w", encoding="utf-8") as f_story:
    #                 f_story.write(story)
    #             print(f"    🟢 Story saved to: {output_story_file_path}")

        




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run EnhancedRAG with specific models")

    # parser.add_argument("--embedding_model", type=str, required=True,
    #                     help="Huggingface embedding model name, e.g. BAAI/bge-large-en-v1.5")
    parser.add_argument("--rag_model", type=str, required=True,
                        help="LLM model name, e.g. qwen/Qwen2.5-7B, meta-llama/Meta-Llama-3-8B, gemma-7b")

    args = parser.parse_args()

    main(args.rag_model)
