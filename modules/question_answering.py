# modules/question_answering.py

from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Load Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", framework="pt")


def answer_question(text, question):
    docs = split_into_chunks(text)

    best_answer = None
    best_score = 0
    best_source = ""

    for doc in docs:
        result = qa_pipeline(question=question, context=doc.page_content)
        if result['score'] > best_score:
            best_score = result['score']
            best_answer = result['answer']
            best_source = doc.page_content[:300]  # for justification

    return f"**Answer**: {best_answer}\n\n📌 *Justified from:* \"{best_source.strip()}...\""

def split_into_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([text])
    return chunks
