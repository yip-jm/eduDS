import json
import requests
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from core.prompts import PromptTemplateManager
from core.utils import extract_json_from_llm
from core.rag import EnhancedRAG
from core.utils import reconstruct_specific_json, sanitize_json_string
from core.myPDFparser import PDF2MarkdownConverter
from core.DataStorytellingEngine import DataStorytellingEngine
import os
import json
import shutil
import argparse
from glob import glob

# ========== STEP 1: DeepSeek API Wrapper ==========
class DeepSeekLLM:
    def __init__(self, api_key, api_url, temperature=0.7, max_tokens=4096, top_p=0.9):
        self.api_key = api_key
        self.api_url = api_url
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p

    def invoke(self, prompt: str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "deepseek-chat",  # 修改为你使用的 deepseek 模型名（如 "deepseek-coder"）
            "messages": [{"role": "user", "content": prompt}],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        return type("Response", (), {"content": result["choices"][0]["message"]["content"]})

# ========== STEP 2: DataStorytellingEngine ==========
class DataStorytellingEngine:
    def __init__(self):
        self.prompt_manager = PromptTemplateManager()
        self.model = DeepSeekLLM(
            api_key="sk-a6b95d2bc4644d04b760bce359c47674",  # ✅ 替换为你的真实 Key
            api_url="https://api.deepseek.com/v1/chat/completions",
            temperature=0.7,
            top_p=0.9,
            max_tokens=4096
        )

    def generate_story_lesson_plan(self, knowledge_base: dict) -> str:
        print("\n--- Starting Data Storytelling Pipeline ---")

        # STEP 1: Story Foundation
        print("\n[STEP 1/4] Generating Story Foundation...")
        try:
            foundation_prompt = self.prompt_manager.get_prompt(
                task="story_foundation",
                knowledge_base=json.dumps(knowledge_base, indent=2)
            )
            response = self.model.invoke(foundation_prompt)
            story_foundation_str = response.content
            print(f"🔵 Raw story foundation: {story_foundation_str}")
            story_foundation = extract_json_from_llm(story_foundation_str)
            print("✅ Story Foundation created successfully.")
        except Exception as e:
            print(f"❌ ERROR in Step 1: Could not generate or parse story foundation. {e}")
            return "Error: Failed to create the story's foundation."

        # STEP 2: Narrative Segments
        print("\n[STEP 2/4] Generating Narrative Segments...")
        story_segments = []
        stages = {
            "Descriptive": "Introduce the characters in the specified setting. Clearly describe the conflict they are facing.",
            "Diagnostic": "The characters analyze *why* the problem is happening. The mentor character should introduce the Core_Concepts by name, explaining their relevance.",
            "Predictive": "The characters debate the pros and cons of the concepts. Use their Strengths and Weaknesses to predict outcomes.",
            "Prescriptive": "The characters reach a resolution, choosing the best solution. The mentor summarizes the lesson, reinforcing the story's Theme."
        }

        for i, (stage_name, instruction) in enumerate(stages.items()):
            print(f"  - Generating segment {i+1}/4: {stage_name}...")
            try:
                segment_prompt = self.prompt_manager.get_prompt(
                    task="story_segment",
                    story_foundation=json.dumps(story_foundation, indent=2),
                    knowledge_base=json.dumps(knowledge_base, indent=2),
                    previous_segments="".join(story_segments),
                    current_stage=stage_name,
                    stage_instruction=instruction
                )
                response = self.model.invoke(segment_prompt)
                story_segments.append(response.content)
            except Exception as e:
                print(f"❌ ERROR in Step 2 ({stage_name}): Could not generate story segment. {e}")
                return f"Error: Failed during the '{stage_name}' part of story generation."

        raw_story_text = "\n\n".join(story_segments)
        print("✅ All narrative segments created.")

        # STEP 3: Polish
        print("\n[STEP 3/4] Polishing the story...")
        try:
            polish_prompt = self.prompt_manager.get_prompt(
                task="story_polish",
                story_foundation=json.dumps(story_foundation, indent=2),
                raw_story_text=raw_story_text
            )
            response = self.model.invoke(polish_prompt)
            final_story_text = response.content

            print(f"🔵 Polished story text: {final_story_text}")

            print("✅ Story polished successfully.")
        except Exception as e:
            print(f"❌ ERROR in Step 3: Could not polish the story. {e}")
            final_story_text = raw_story_text

        # STEP 4: Final Lesson Plan
        print("\n[STEP 4/4] Generating the final lesson plan...")
        try:
            lesson_plan_prompt = self.prompt_manager.get_prompt(
                task="lesson_plan",
                knowledge_base=json.dumps(knowledge_base, indent=2),
                final_story_text=final_story_text,
                final_story_text2=final_story_text,
                knowledge_topic=knowledge_base.get("Knowledge_Topic", "Lesson")
            )
            response = self.model.invoke(lesson_plan_prompt)
            final_lesson_plan = response.content
            print("✅ Final lesson plan generated.")
        except Exception as e:
            print(f"❌ ERROR in Step 4: Could not generate the lesson plan. {e}")
            return "Error: Failed to generate the final lesson plan."

        print("\n--- Data Storytelling Pipeline Finished ---")
        return final_lesson_plan





def main(rag_model: str, story_model: str):  
    # ROOT_DIR = os.environ.get("ROOT_DIR")
    # if ROOT_DIR is None:
    #     raise EnvironmentError("Environment variable ROOT_DIR not set")

    ROOT_DIR = "/home/jye/dse"  # 获取当前脚本所在目录
    print(f"Using ROOT_DIR: {ROOT_DIR}")



    # construct output directories
    output_dir_ke = os.path.join(ROOT_DIR, "result", f"{rag_model.replace('/', '_').replace(':', '_')}", "knowledge_extraction")
    output_dir_sg = os.path.join(ROOT_DIR, "result", f"{rag_model.replace('/', '_').replace(':', '_')}", "story_generation", f"{story_model.replace('/', '_').replace(':', '_')}")

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

            engine = DataStorytellingEngine()
            lesson_plan_markdown = engine.generate_story_lesson_plan(knowledge_base)
            

            output_story_filename = f"story_{ke_prefix}.md"  # 如 story_q01.md
            output_story_file_path = os.path.join(output_subdir_sg, output_story_filename)
            
            with open(output_story_file_path, "w", encoding="utf-8") as f_story:
                f_story.write(lesson_plan_markdown)
            print(f"    🟢 Story saved to: {output_story_file_path}")

        


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Run EnhancedRAG with specific models")

    # parser.add_argument("--rag_model", type=str, required=True,
    #                     help="LLM model name, e.g. qwen/Qwen2.5-7B, meta-llama/Meta-Llama-3-8B, gemma-7b")
    # parser.add_argument("--sy_model", type=str, required=True,
    #                     help="LLM model name, e.g. qwen/Qwen2.5-7B, meta-llama/Meta-Llama-3-8B, gemma-7b")

    # args = parser.parse_args()

    main("gemma:7b", "dk")
