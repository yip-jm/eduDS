from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="enhanced_rag_olmo",
    version="0.1.0",
    author="Junming Ye",
    author_email="j.ye2@student.uva.nl",
    description="An enhanced RAG system for Data Storytelling in Education.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
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
        "accelerate",
        "ollama",
    ],
    entry_points={
        "console_scripts": [
            "run_rag_olmo=main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    include_package_data=True,
)
