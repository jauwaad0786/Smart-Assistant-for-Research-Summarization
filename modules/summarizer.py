# modules/summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")



def generate_summary(text, max_words=150):
    # Truncate long text
    text = text[:3000]  # adjust for tokenizer limit

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    
    return summary
