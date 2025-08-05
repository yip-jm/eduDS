from core.rag import EnhancedRAG
from core.utils import reconstruct_specific_json, sanitize_json_string
from core.myPDFparser import PDF2MarkdownConverter
from core.DataStorytellingEngine import DataStorytellingEngine
import os
import json
import shutil
import argparse
from glob import glob


def main(rag_model: str, story_model: str):  
    ROOT_DIR = os.environ.get("ROOT_DIR")
    if ROOT_DIR is None:
        raise EnvironmentError("Environment variable ROOT_DIR not set")





    # construct output directories
    output_dir_ke = os.path.join(ROOT_DIR, "results", f"{rag_model.replace('/', '_').replace(':', '_')}", "knowledge_extraction")
    output_dir_sg = os.path.join(ROOT_DIR, "results", f"{rag_model.replace('/', '_').replace(':', '_')}", "story_generation", f"{story_model.replace('/', '_').replace(':', '_')}")




    if os.path.exists(output_dir_sg):
        shutil.rmtree(output_dir_sg, ignore_errors=True)
    os.makedirs(output_dir_sg, exist_ok=True)


    ke_folders = [ folder for folder in os.listdir(output_dir_ke)]



    for ke_folder in ke_folders:
        ke_files = glob(os.path.join(output_dir_ke, ke_folder, "*.json"))
        output_subdir_sg = os.path.join(output_dir_sg, ke_folder)
        os.makedirs(output_subdir_sg, exist_ok=True)
        for kfile in ke_files:
            with open(kfile, "r", encoding="utf-8") as f:
                knowledge_base = json.load(f)

            input_filename = os.path.basename(kfile)
            ke_prefix = input_filename.replace(".json", "")

            ds = DataStorytellingEngine(model_name=story_model)
            story = ds.generate_lesson_package(knowledge_base=knowledge_base)

            output_story_filename = f"story_{ke_prefix}.md"  # 如 story_q01.md
            output_story_file_path = os.path.join(output_subdir_sg, output_story_filename)
            
            with open(output_story_file_path, "w", encoding="utf-8") as f_story:
                f_story.write(story)
            print(f"    🟢 Story saved to: {output_story_file_path}")

        




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run EnhancedRAG with specific models")

    parser.add_argument("--rag_model", type=str, required=True,
                        help="LLM model name, e.g. qwen/Qwen2.5-7B, meta-llama/Meta-Llama-3-8B, gemma-7b")
    parser.add_argument("--sy_model", type=str, required=True,
                        help="LLM model name, e.g. qwen/Qwen2.5-7B, meta-llama/Meta-Llama-3-8B, gemma-7b")

    args = parser.parse_args()

    main(args.rag_model, args.sy_model)
