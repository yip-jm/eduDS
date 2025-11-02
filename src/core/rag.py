# class EnhancedRAG:
from ollama import chat
from core.prompts import PromptTemplateManager
from core.processor import SmartDocumentProcessor
from core.retriever import HybridRetriever
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import hashlib
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from core.utils import contexts_extraction, reconstruct_specific_json


class EnhancedRAG:
    def __init__(self, embedding_model_name=None, model_name=None, persist_dir=None):
        self.prompt_manager = PromptTemplateManager()
        processor = SmartDocumentProcessor(embedding_model_name=embedding_model_name)
        chunks = processor.process_documents()
        self.retriever = HybridRetriever(chunks, embedding_model_name=embedding_model_name, persist_dir=persist_dir)

        
        self.model = ChatOllama(
            model=model_name,
            temperature=0,
            top_p=0.95,
            max_new_tokens=2048,
            format="json",
        )

    # def deduplicate_contexts(self, contexts):
    #     seen_hashes = set()
    #     deduped = []
    #     for doc in contexts:
    #         content_hash = hashlib.md5(doc.page_content.encode()).hexdigest()
    #         if content_hash not in seen_hashes:
    #             seen_hashes.add(content_hash)
    #             deduped.append(doc)
    #     return deduped

    def ask(self, question):
        contexts = self.retriever.retrieve(question)
        # contexts = self.deduplicate_contexts(contexts)[:]


        prompt = self.prompt_manager.get_prompt(
            task="rag_extract",
            question=question,
            context="\n\n".join([
                f"[Source: {doc.metadata['source']}, Type: {doc.metadata['content_type']}]\n{doc.page_content}"
                for doc in contexts
            ])
        )


        response = self.model.invoke(prompt)
        answer_text = response.content
        print(f"🔵 Raw answer: {answer_text}")
        parsed_data = self.prompt_manager.parse(answer_text)
        print(f"🟢 Parsed data: {parsed_data}")
        parsed_data["Source_Context"] = contexts_extraction(contexts)

        return parsed_data
  