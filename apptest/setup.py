from setuptools import setup, find_packages

setup(
    name="enhanced_rag_olmo",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List key dependencies from requirements.txt or read from it
        "langchain>=0.1.0,<0.2.0",
        "langchain-experimental",
        "langchain-huggingface",
        "langchain-community",
        "sentence-transformers",
        "transformers>=4.30.0",
        "torch>=2.0.0",
        "huggingface-hub",
        "chromadb>=0.4.0,<0.5.0",
        "pypdf",
        "rank_bm25",
        "accelerate"
    ],
    entry_points={
        "console_scripts": [
            "run_rag_olmo=main:main",
        ],
    },
    author="Junming Ye",
    author_email="j.ye2@student.uva.nl",
    description="An enhanced RAG system.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/enhanced_rag_olmo", # Replace with your repo URL
)