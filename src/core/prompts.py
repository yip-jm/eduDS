# class PromptTemplateManager:
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import ast

class PromptTemplateManager:
    def __init__(self):
        self.rag_schemas = [
            ResponseSchema(
                name="Question",
                description="The original user question.",
                type="string"
            ),

            ResponseSchema(
                name="Knowledge_Topic",
                description=(
                    "A short, high-level topic category inferred from the question, like 'Computer Architecture'."
                ),
                type="string"
            ),

            ResponseSchema(
                name="Core_Concepts",
                description=(
                    "This field is mandatory. If you cannot find core concepts from the context, you MUST return empty list []."
                    "A list of extracted concepts, each with 6 keys:\n"
                    "Concept: the concept name\n"
                    "Definition: a concise explanation of the concept\n"
                    "Key_Points: List. Extract and list the primary facts, ideas, or components that define this concept. You may use direct quotes from the original text if they are clear and self-contained. Each point must be in a complete sentence and relevant to the topic. Include at least 3 points, if available.\n"
                    "Significance_Detail: mandatory. Clearly explain why this concept is important. You may quote or closely paraphrase relevant parts of the text, but ensure the explanation connects to the problem it solves, its impact, or its relevance. This answers the 'So what?' question. Use complete sentences. If not found, return null.\n"
                    "Strengths: mandatory. Identify one or more strengths or benefits of the concept. You may use direct quotes if appropriate, but provide context or brief explanation when needed. Write in complete sentences. If not found, return null.\n"
                    "Weaknesses: mandatory. Identify weakness, limitation, or challenge associated with the concept. Use direct evidence from the text where possible, with minimal interpretation. Complete sentences only. If not found, return null."
                )
            ),


            ResponseSchema(
                name="Overall_Summary",
                description=(
                    "This field is mandatory."
                    "A concise, one or two-sentence summarize the key points direct answer to the question, synthesized from the context."
                ),
                type="string"
            ),
            
        ]
        self.parser = StructuredOutputParser.from_response_schemas(self.rag_schemas)

        self.templates = {
            "rag_extract": {
                "system": (
                    "You are an expert AI assistant specializing in STEM education. "
                    "Your primary task is to understand the user's question, identify the relevant knowledge topic, and extract an accurate information from the provided context. "
                    "Extract information faithfully and precisely from the context. "
                    "IMPORTANT RULE: You MUST include exactly these 4 keys in your output: 'Question', 'Knowledge_Topic', 'Core_Concepts', 'Overall_Summary'."
                ),
                "user": (
                    "Question:\n{question}\n\n"
                    "Context:\n{context}\n\n"
                    "{format_instructions}"
                )
            },

            # story_generation: 
            # --- DATA STORYTELLING PIPELINE PROMPTS ---
            # TASK 2: Generate a high-level lesson plan outline.
            "lesson_plan_outline": {
                "system": (
                    "You are a Master Educator and Curriculum Designer. Your task is to create a high-level, logical lesson plan outline based on a structured knowledge summary. The plan should be intuitive for a teacher to follow."
                ),
                "user": (
                    "# INPUT KNOWLEDGE SUMMARY:\n"
                    "- Original Question: {question}\n"
                    "- Knowledge Topic: {knowledge_topic}\n"
                    "- Overall Summary: {overall_summary}\n"
                    "- Core Concepts to cover: {concept_names_list}\n\n"
                    "# TASK:\n"
                    "Based on the input summary, generate a concise lesson plan outline in Markdown format. For each section, provide a one-sentence objective.\n\n"
                    "1.  **Lesson Title**: A compelling title based on the Knowledge Topic.\n"
                    "2.  **Introduction (Hook)**: Objective: How to grab students' attention using the original question or a real-world problem.\n"
                    "3.  **Core Content Delivery**: Objective: A numbered list of the core concepts, arranged in a logical teaching order.\n"
                    "4.  **Key Activity/Discussion**: Objective: A placeholder for an interactive segment to reinforce learning.\n"
                    "5.  **Conclusion & Synthesis**: Objective: How to wrap up the lesson, connecting back to the Overall Summary."
                )
            },

            # TASK 3: Generate a story module for a SINGLE core concept.
            "core_concept_story": {
                "system": (
                    "You are an Expert Storyteller for Education. You will create a 'story module' for a single core concept to help a teacher explain it engagingly. Your story must be structured and practical."
                ),
                "user": (
                    "# INPUT CORE CONCEPT:\n"
                    "```json\n{core_concept_json}\n```\n\n"
                    "# TASK:\n"
                    "Generate a teaching story for the concept '{concept_name}'. Structure your output into these three sections using Markdown:\n\n"
                    "### 1. The Story (Problem -> Solution -> Impact)\n"
                    "- **The Problem (Event)**: Based on `Significance_Detail`, describe the situation or challenge that existed *before* this concept.\n"
                    "- **The 'Aha!' Moment (Experience)**: Narrate the discovery of the concept. Use `Definition` and `Key_Points` to explain what it is and how it works.\n"
                    "- **The Impact (Meaning)**: Explain *why* it matters. Use `Strengths`, `Weaknesses`, and `Significance_Detail` to discuss its importance and trade-offs.\n\n"
                    "### 2. Storytelling Hooks\n"
                    "- **Dramatic Question**: A compelling question that frames the story (e.g., 'Could making a computer dumber actually make it smarter?').\n"
                    "- **Point of View**: Suggest a narrative perspective (e.g., 'From the perspective of an engineer facing a challenge.').\n\n"
                    "### 3. Classroom Delivery Tips\n"
                    "- **Pacing**: Suggest where to pause or ask a question.\n"
                    "- **Analogy**: Provide a simple, relatable analogy for the concept."
                )
            },

            # TASK 4: Generate interactive activities for a SINGLE core concept.
            "activity_discussion": {
                "system": (
                    "You are an Educational Activity Designer. You create interactive classroom elements to foster critical thinking."
                ),
                "user": (
                    "# INPUT DATA:\n"
                    "- Concept: {concept_name}\n"
                    "- Strengths: {strengths}\n"
                    "- Weaknesses: {weaknesses}\n\n"
                    "# TASK:\n"
                    "Generate two distinct items based on the provided strengths and weaknesses:\n\n"
                    "1.  **A 'Debate Topic'**: Frame a clear, debatable statement that pits the strengths against the weaknesses.\n"
                    "2.  **A 'What If' Scenario Question**: Create a short, hypothetical scenario that forces students to apply the concept and justify their choice based on its trade-offs."
                )
            }
        }



    def get_prompt(self, task: str, **kwargs) -> str:
        if task not in self.templates:
            raise ValueError(f"Task '{task}' not defined in prompt templates.")
        
        format_instructions = self.parser.get_format_instructions()
        kwargs["format_instructions"] = format_instructions

        system_prompt = self.templates[task]["system"]
        user_prompt_template = self.templates[task]["user"]
        filled_user_prompt = user_prompt_template.format(**kwargs)
        return f"{system_prompt}\n\n{filled_user_prompt}"
    

    def parse(self, output_text: str) -> dict | None:
        try:
            return self.parser.parse(output_text)
        except Exception as e:
            print(f"[Parser error] {e}")
            data_dict  = ast.literal_eval(output_text)
            output_data = {
                "Question": data_dict.get("Question", ""),
                "Knowledge_Topic": data_dict.get("Knowledge_Topic", "null"),
                "Core_Concepts": data_dict.get("Core_Concepts", "[]"),
                "Overall_Summary": data_dict.get("Overall_Summary", "null"),
            }
            return output_data
