import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util
from rouge_score import rouge_scorer
from bert_score import score as bert_score

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load semantic model once
sbert_model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')  # Better than mpnet for QA

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    stop_words = set(stopwords.words('english'))
    return " ".join([word for word in word_tokenize(text) if word not in stop_words])

def semantic_similarity_sbert(predicted, reference):
    emb1 = sbert_model.encode(predicted, convert_to_tensor=True)
    emb2 = sbert_model.encode(reference, convert_to_tensor=True)
    similarity_score = util.cos_sim(emb1, emb2).item()
    return round(similarity_score * 100, 2)

def rouge_score(predicted, reference):
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(reference, predicted)
    return round(scores['rougeL'].fmeasure * 100, 2)

def bert_f1(predicted, reference):
    P, R, F1 = bert_score([predicted], [reference], lang="en", verbose=False)
    return round(F1[0].item() * 100, 2)

def evaluate(predicted_answer, true_answer):
    pred_clean = clean_text(predicted_answer)
    true_clean = clean_text(true_answer)

    return {
        "Semantic Similarity (SBERT)": semantic_similarity_sbert(predicted_answer, true_answer),
        "ROUGE-L Score": rouge_score(predicted_answer, true_answer),
        "BERTScore (F1)": bert_f1(predicted_answer, true_answer)
    }
