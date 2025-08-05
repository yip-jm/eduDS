from langchain_ollama import ChatOllama
import json
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from core.prompts import PromptTemplateManager
from .utils import extract_json_from_llm

class DataStorytellingEngine:
    def __init__(self, model_name=None):
        self.prompt_manager = PromptTemplateManager()
        self.model = ChatOllama(
            model=model_name,
            temperature=0.7,
            top_p=0.9,
            max_new_tokens=4096,
        )



    def generate_lesson_package(self, knowledge_base: dict) -> str:
        """
        Orchestrates the new multi-step pipeline to generate a full "lesson package"
        containing an outline, story modules for each concept, and activities.
        
        Args:
            knowledge_base (dict): The structured knowledge from the RAG system.

        Returns:
            str: A complete, teacher-facing lesson package in a single Markdown string.
        """
        print("\n--- Starting Lesson Package Generation Pipeline ---")
        
        # 用于最终拼接成一个Markdown文件的组件列表
        final_document_parts = []
        
        # === STEP 1: Generate the Lesson Plan Outline ===
        print("\n[PIPELINE STEP 1/3] Generating Lesson Plan Outline...")
        try:
            # 准备Prompt所需的参数
            concept_names = [concept.get('Concept', 'Unnamed Concept') for concept in knowledge_base.get('Core_Concepts', [])]
            
            outline_prompt = self.prompt_manager.get_prompt(
                task="lesson_plan_outline",
                question=knowledge_base.get('Question', 'N/A'),
                knowledge_topic=knowledge_base.get('Knowledge_Topic', 'N/A'),
                overall_summary=knowledge_base.get('Overall_Summary', 'N/A'),
                concept_names_list=", ".join(concept_names)
            )
            
            response = self.model.invoke(outline_prompt)
            lesson_outline_md = response.content
            
            final_document_parts.append(lesson_outline_md)
            print("✅ Lesson Plan Outline created successfully.")

        except Exception as e:
            print(f"❌ ERROR in Step 1 (Outline): {e}")
            return "Error: Failed to create the lesson plan outline."

        # === STEP 2 & 3: Loop through each Core Concept to generate its Story and Activities ===
        print(f"\n[PIPELINE STEP 2 & 3] Generating modules for {len(knowledge_base.get('Core_Concepts', []))} core concepts...")
        
        core_concepts = knowledge_base.get('Core_Concepts', [])
        if not core_concepts:
            print("⚠️  Warning: No core concepts found in the knowledge base.")

        for i, concept in enumerate(core_concepts):
            concept_name = concept.get('Concept', f'Concept {i+1}')
            print(f"\n  -> Processing Concept: {concept_name}")
            
            # --- Sub-step 2: Generate Core Concept Story Module ---
            try:
                print(f"    - Generating story module...")
                story_prompt = self.prompt_manager.get_prompt(
                    task="core_concept_story",
                    core_concept_json=json.dumps(concept, indent=2),
                    concept_name=concept_name
                )
                response = self.model.invoke(story_prompt)
                story_module_md = response.content
                
                # 添加一个清晰的标题，以便在最终文档中区分
                final_document_parts.append(f"\n\n---\n\n## Teaching Module: {concept_name}")
                final_document_parts.append(story_module_md)
                print(f"    ✅ Story module for '{concept_name}' created.")

            except Exception as e:
                print(f"❌ ERROR generating story for '{concept_name}': {e}")
                final_document_parts.append(f"\n\n> *Error: Could not generate story module for {concept_name}.*")

            # --- Sub-step 3: Generate Activity & Discussion Module ---
            try:
                print(f"    - Generating activity module...")
                activity_prompt = self.prompt_manager.get_prompt(
                    task="activity_discussion",
                    concept_name=concept_name,
                    strengths=concept.get('Strengths', 'N/A'),
                    weaknesses=concept.get('Weaknesses', 'N/A')
                )
                response = self.model.invoke(activity_prompt)
                activity_module_md = response.content
                
                final_document_parts.append(f"\n### Interactive Activities for {concept_name}")
                final_document_parts.append(activity_module_md)
                print(f"    ✅ Activity module for '{concept_name}' created.")
                
            except Exception as e:
                print(f"❌ ERROR generating activities for '{concept_name}': {e}")
                final_document_parts.append(f"\n\n> *Error: Could not generate activities for {concept_name}.*")
        
        print("\n--- Lesson Package Generation Finished ---")
        
        # 将所有生成的Markdown片段组合成一个连贯的文档
        return "\n".join(final_document_parts)
            
    

