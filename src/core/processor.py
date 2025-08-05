# class SmartDocumentProcessor:
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
import re

class SmartDocumentProcessor:
    def __init__(self, embedding_model_name=None):
        self.embed_model = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            model_kwargs={
                "device": "cuda",
                "trust_remote_code": True},
            encode_kwargs={"batch_size": 16},
        )

    def _detect_content_type(self, text):
        if re.search(r'def |import |print\(|code', text):
            return "code"
        elif re.search(r'\|.+\|', text) or re.search(r'<table\b[^>]*>', text) or re.search(r'<table.*?>.*?</table>', text, re.DOTALL):
            return "table"
        elif re.search(r'https?://', text):
            return "url"
        return "normal"

    def process_documents(self):
        loaders = [
            DirectoryLoader("docs/materials_md/parsed/", glob="**/*.md", loader_cls=TextLoader),
            # DirectoryLoader("docs/materials/", glob="**/*.pdf", loader_cls=PyPDFLoader),
        ]

        documents = []
        for loader in loaders:
            documents.extend(loader.load())

        chunker = SemanticChunker(
            embeddings=self.embed_model,
            breakpoint_threshold_amount=82,
            add_start_index=True,
        )
        base_chunks = chunker.split_documents(documents)

        final_chunks = []
        for chunk in base_chunks:
            content_type = self._detect_content_type(chunk.page_content)
            if content_type == "code":
                splitter = RecursiveCharacterTextSplitter(chunk_size=384, chunk_overlap=128)
            elif content_type == "table":
                splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=128)
            elif content_type == "url":
                continue
            else:
                splitter = RecursiveCharacterTextSplitter(chunk_size=384, chunk_overlap=64)

            final_chunks.extend(splitter.split_documents([chunk]))

        for i, chunk in enumerate(final_chunks):
            chunk.metadata.update({
                "chunk_id": f"chunk_{i}",
                "content_type": self._detect_content_type(chunk.page_content)
            })

        return final_chunks
