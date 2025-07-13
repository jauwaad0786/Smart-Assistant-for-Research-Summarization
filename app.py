import streamlit as st
from dotenv import load_dotenv
import os

from modules import document_loader, summarizer, question_answering, challenge_mode, evaluate_response

# Load environment variables
load_dotenv()

# Load CSS with utf-8 encoding
with open("UI/styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load assistant HTML with utf-8 encoding
with open("UI/assistant.html", encoding="utf-8") as f:
    st.markdown(f.read(), unsafe_allow_html=True)

# Start of main content section
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ✅ SINGLE LINE Animated Title Banner
st.markdown('''
    <div class="animated-banner single-line" style="text-align:center; font-size: 30px; font-weight: bold; margin-bottom: 2rem;">
        ✨ Welcome to AI Smart Document Assistant 🤖 ✨
    </div>
''', unsafe_allow_html=True)

# File upload
uploaded_file = st.file_uploader("📄 Upload PDF or TXT", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("📚 Reading your document..."):
        text = document_loader.load_document(uploaded_file)
        summary = summarizer.generate_summary(text)

    st.success("✅ Document processed successfully!")

    # Summary display
    st.markdown('<div class="glass-box"><h3>📝 Summary</h3>', unsafe_allow_html=True)
    st.markdown(f"<p class='summary-text'>{summary}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Tabs
    tab1, tab2, tab3 = st.tabs(["❓ Ask Anything", "🧠 Challenge Me", "📊 Evaluate Answer"])

    # Tab 1: Ask Questions
    with tab1:
        question = st.text_input("Ask a question based on the document")

        # 🟡 Custom yellow text on Get Answer button
        st.markdown('''
            <style>
            div.stButton > button {
                background-color: #1e3c72 !important;
                color: #ffd700 !important;
                border-radius: 10px;
                font-weight: bold;
                font-size: 16px;
                padding: 0.5rem 1.2rem;
            }
            </style>
        ''', unsafe_allow_html=True)

        if st.button("💬 Get Answer"):
            if question:
                answer = question_answering.answer_question(text, question)
                st.markdown('<div class="glass-box">', unsafe_allow_html=True)
                st.markdown(f"<b>Answer:</b> {answer}", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("Please ask a question.")

    # Tab 2: Challenge Mode
    with tab2:
        if st.button("Generate Questions"):
            questions = challenge_mode.generate_challenge_questions(text)
            for i, q in enumerate(questions):
                st.markdown(f"**Q{i+1}. {q['question']}**")
                user_ans = st.text_input("Your Answer:", key=f"user_answer_{i}")
                if user_ans:
                    correct = challenge_mode.evaluate_user_answer(q['answer'], user_ans)
                    feedback = "✅ Correct!" if correct else "❌ Incorrect"
                    st.markdown(f"{feedback}<br><b>Justification:</b> {q['justification']}", unsafe_allow_html=True)

    # Tab 3: Evaluate Answers
    with tab3:
        st.subheader("📊 Evaluate Model vs. Ground Truth Answer")
        true_answer = st.text_area("✅ Ground Truth Answer", height=150)
        predicted_answer = st.text_area("🤖 Model Answer", height=150)

        if st.button("🔍 Evaluate Accuracy"):
            if true_answer and predicted_answer:
                scores = evaluate_response.evaluate(predicted_answer, true_answer)

                st.markdown('<div class="glass-box">', unsafe_allow_html=True)
                st.subheader("📈 Evaluation Results")
                for metric, value in scores.items():
                    st.markdown(f"<div class='result-box'><b>{metric}:</b> {value:.2f}%</div>", unsafe_allow_html=True)
                    st.progress(int(value))
                st.markdown('</div>', unsafe_allow_html=True)

                verdict = "⚠️ Needs Improvement"
                sbert_score = scores.get("Semantic Similarity (SBERT)", 0)
                if sbert_score > 85:
                    verdict = "🌟 Excellent"
                elif sbert_score > 70:
                    verdict = "✅ Good"

                st.markdown(f"<div class='verdict'>Final Verdict: {verdict}</div>", unsafe_allow_html=True)
            else:
                st.warning("Please provide both answers for evaluation.")

# End of main content
st.markdown('</div>', unsafe_allow_html=True)
