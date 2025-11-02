
from langchain.schema import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama

class ParserImage:
    def __init__(self):
        self.model = ChatOllama(
            model="qwen2.5vl:7b",
            temperature=0.05,
            max_tokens=2048,
        )

    def convert_image_to_md(self, image_base64):
        messages = [
            SystemMessage(content=(
                "You are an AI specialized in analyzing and describing images, especially document-style images. "
                "Your task is to extract and describe the visual content of the image as precisely and completely as possible. "
                "Avoid adding interpretations, assumptions, or subjective language."
            )),
            HumanMessage(content=[{"type": "image_url", "image_url": {"url": image_base64}}])
        ]
        response = self.model.invoke(messages)
        return response.content