# Utility functions (JSON parse etc)
import re
import json
import base64
from typing import List, Dict

def extract_json_from_llm(response_text: str) -> str | None:
    match = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", response_text, re.DOTALL)
    json_str_to_parse = match.group(1).strip() if match else None
    if not json_str_to_parse:
        first, last = response_text.find('{'), response_text.rfind('}')
        if first != -1 and last != -1 and last > first:
            json_str_to_parse = response_text[first:last + 1].strip()
        else:
            json_str_to_parse = response_text.strip()
    try:
        return json_str_to_parse
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}\nSnippet: {json_str_to_parse[:100]}")
        return None
    


def reconstruct_core_concepts(raw_concepts: list) -> list:
    reconstructed = []
    for idx, item in enumerate(raw_concepts):
        if not isinstance(item, dict):
            print(f"[Warning] Skipping invalid concept at index {idx} (not a dict).")
            continue

        reconstructed_item = {
            "Concept": item.get("Concept", ""),
            "Definition": item.get("Definition", ""),
            "Key_Points": item.get("Key_Points", []) if isinstance(item.get("Key_Points"), list) else [],
            "Significance_Detail": item.get("Significance_Detail") if item.get("Significance_Detail") is not None else None,
            "Strengths": item.get("Strengths") if item.get("Strengths") is not None else None,
            "Weaknesses": item.get("Weaknesses") if item.get("Weaknesses") is not None else None
        }

        # Ensure Key_Points is a list of strings
        if not all(isinstance(kp, str) for kp in reconstructed_item["Key_Points"]):
            reconstructed_item["Key_Points"] = []

        # Optionally validate Concept and Definition are strings
        if not isinstance(reconstructed_item["Concept"], str):
            reconstructed_item["Concept"] = ""
        if not isinstance(reconstructed_item["Definition"], str):
            reconstructed_item["Definition"] = ""

        reconstructed.append(reconstructed_item)

    return reconstructed


def reconstruct_specific_json(parsed_data: dict | None, indent_level: int = 4) -> str:
    output_data = {
        "Question": "",
        "Knowledge_Topic": "",
        "Core_Concepts": [],
        "Overall_Summary": "",
        "Source_Context": []
    }

    print("I'm reconstructing the JSON...\n")

    if isinstance(parsed_data, dict):
        output_data["Question"] = parsed_data.get("Question") or None
        output_data["Knowledge_Topic"] = parsed_data.get("Knowledge_Topic") or None
        output_data["Overall_Summary"] = parsed_data.get("Overall_Summary", None)

        core_concepts = parsed_data.get("Core_Concepts")
        if isinstance(core_concepts, list):
            output_data["Core_Concepts"] = reconstruct_core_concepts(parsed_data.get("Core_Concepts", []))


        source_context = parsed_data.get("Source_Context")
        if isinstance(source_context, list):
            output_data["Source_Context"] = source_context

    return output_data, json.dumps(output_data, ensure_ascii=False, indent=indent_level)


def sanitize_json_string(json_str):
    return re.sub(r'\\(?![\"/bfnrtu])', r'\\\\', json_str)

def encode_image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")
    
def contexts_extraction(docs):
    source_context = []
    for doc in docs:
        entry = {
            "source": doc.metadata['source'],
            "content_type": doc.metadata['content_type'],
            "page_content": doc.page_content
        }
        source_context.append(entry)

    return source_context



