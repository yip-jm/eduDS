# class HybridRetriever:
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from sentence_transformers import CrossEncoder
import torch


class HybridRetriever:
    def __init__(self, chunks, embedding_model_name=None, persist_dir="../../vector_db"):

        self.vector_db = Chroma.from_documents(
            chunks,
            embedding =  HuggingFaceEmbeddings(
                model_name=embedding_model_name,
                model_kwargs={
                    "device": "cuda",
                    "trust_remote_code": True},
                encode_kwargs={"batch_size": 16},
            ),
            persist_directory=persist_dir
        )
        self.bm25_retriever = BM25Retriever.from_documents(chunks, k=16)

        self.ensemble_retriever = EnsembleRetriever(
            retrievers=[
                self.vector_db.as_retriever(search_kwargs={"k": 8}),
                self.bm25_retriever
            ],
            weights=[0.6, 0.4]
        )

        self.reranker = CrossEncoder(
            "BAAI/bge-reranker-v2-m3",
            device="cuda" if torch.cuda.is_available() else "cpu"
        )

    def retrieve(self, query, top_k=5):
        docs = self.ensemble_retriever.get_relevant_documents(query)
        pairs = [[query, doc.page_content] for doc in docs]
        scores = self.reranker.predict(pairs)
        ranked_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in ranked_docs[:top_k]]
